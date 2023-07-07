import json
from django.views.generic import View
from data_status import data_status_notif
# from polls.api.bid_request import prev_data,prev_results,won_bids
from ..models import Notification, BidResponse,Game


#_____________________________________________________________________________________________

class NotificationView(View):

    
    def get(self, request):    
        nts = Notification.objects.all()
        data = []
        for nt in nts:
            data.append({'id': nt.ext_id,
                         'win': nt.win,
                         'price': nt.price,
                         'click': nt.click,
                         'conversion': nt.conversion,
                         'revenue': nt.revenue
                         
                         
                         })
        return data_status_notif(data)
    
    
    
#_____________________________________________________________________________________________



    def post(self, request):
        data = json.loads(request.body)
        bid_response = BidResponse.objects.get(external_id=data['id'])
        if data['win']:
            notification = Notification.objects.create(
                external_id=data['id'],
                win = data['win'],
                price=data['price'],
                click=data['click'],
                conversion=data['conversion'],
                revenue=data['revenue']
            )
        else:
            notification = Notification.objects.create(
                external_id=data['id'],
                win = data['win'])


        notification.save()
        g = Game.objects.first().id
        game = Game.objects.get(id=g)
        #game.budget -= float(data['price'])
        game.save()


        if notification.win:
            print("win")
            data = {
                "win": True,
                "id": notification.external_id,
                "price": notification.price,
                "click": notification.click,
                "conversion": notification.conversion,
                "revenue": notification.revenue
            }

            game.total_revenue += (game.impression_revenue + game.click_revenue*data['click']+ game.conversion_revenue*data['conversion'])
            game.impressions_total -= 1
        #TODO sort by id
        #get the current, retrive game instance
        
        

            
        else:
            print("loss")
            data = {
                "win": False,
                "id": notification.external_id
            }
        
            
        data = {
             'id': notification.external_id,
             'win': notification.win,
             'price': notification.price,
             'click': notification.click,
             'conversion': notification.conversion,
             'revenue': notification.revenue
         }

        return data_status_notif(data)

