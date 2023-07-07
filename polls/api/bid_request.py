import json, random 
from data_status import data_status_bid
from django.views.generic import View
from ..models import BidRequest, BidResponse, Creative, Category
from ..bid import optimal_bid
from polls.api.configuration import Game



#_____________________________________________________________________________________________

class BidRequestView(View):

#_____________________________________________________________________________________________

    def get(self, request):    
        bids = BidRequest.objects.all()
        data = []
        for bid in bids:
            data.append({
                'external_id': bid.external_id,
                'click_prob' : bid.click_prob,
                "conv_prob" : bid.conv_prob,
                "user_id" : bid.user_id
                
                })
        return data_status_bid(data)
    
#_____________________________________________________________________________________________       
        
    def post(self, request):
        data = json.loads(request.body)
    
        #bcat = data['bcat']

        previous_bid_request = BidRequest.objects.order_by('created_at').last()


        bid_request = BidRequest.objects.create(
            external_id = data['id'],
            imp_banner_w = float(data["imp"]["banner"]['w']),
            imp_banner_h = float(data["imp"]["banner"]['h']),
            click_prob = float(data['click']['prob']),
            conv_prob = float(data['conv']['prob']),
            site_domain = data['site']['domain'],
            ssp_id = data['ssp']['id'],
            user_id = data['user']['id'],
            bcat = data['bcat']
        )

        
        # Check if SSP ID exists in the given list
        ssp_address = request.META.get('REMOTE_ADDR')
        SSP_LIST = []
        SSP_LIST.append(ssp_address)

        # Check if SSP ID exists in the given list
        if bid_request.ssp_id in SSP_LIST:
            impression_revenue = Game.impression_revenue
        else:
            impression_revenue = 0

        Game.impression_revenue = impression_revenue
        bid_request.save()
        creative = random.choice(Creative.objects.all())
        bid_request.save()





        creative = random.choice(Creative.objects.all())
        
        bid_response = BidResponse.objects.create(
            external_id = data['id'],
            creative = creative,
            bid_req = bid_request,
            bid = optimal_bid(bid_request, previous_bid_request)
        )

        bid_response.save()

        data = {
                'external_id': creative.external_id,
                'price':bid_response.bid,
                'image_url': "https://theprivatetherapyclinic.co.uk/wp-content/uploads/2018/12/Weaponisation-768x384.jpg",#bid_response.creative.url+ f"?width={creative.width}&height={creative.height}" ,
                'cat':[category.code for category in bid_response.creative.category.all()]
                }

        return data_status_bid(data)