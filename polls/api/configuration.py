import json,random
from django.views.generic import View
from data_status import ok_status, status_configue
from ..models import Game,Creative,Campaign, BidRequest, BidResponse, Notification
# from django.http import JsonResponse
from .reading import *


#_____________________________________________________________________________________________


class GameView(View):

    def get(self, request):    
        gms = Game.objects.all()
        data = []
        for gm in gms:
            data.append({ 'impressions_total': gm.impressions_total,
                        'auction_type': gm.auction_type,
                         'mode': gm.mode,
                         'budget': gm.budget,
                         'impression_revenue': gm.impression_revenue,
                         'click_revenue': gm.click_revenue,
                         'conversion_revenue': gm.conversion_revenue                         
                         })
        return ok_status(data)
    

#_____________________________________________________________________________________________
    def post(self, request):
        data = json.loads(request.body)
        
        if Game.objects.exists():
            game = Game.objects.first()
            last = game.id
            Game.objects.filter(id = last).update(
                impressions_total = data['impressions_total'],
                auction_type = data['auction_type'],
                mode = data['mode'],
                budget = data['budget'],
                impression_revenue = data['impression_revenue'],
                click_revenue = data['click_revenue'],
                conversion_revenue = data['conversion_revenue'],
                frequency_capping = data['frequency_capping'],
                total_revenue = 0
            )
            
            game = Game.objects.get(id=last)

            if game.mode == "script":
                Creative.objects.all().delete()
                Campaign.objects.all().delete()
                BidRequest.objects.all().delete()
                BidResponse.objects.all().delete()
                Notification.objects.all().delete()
            elif game.mode == "free":
                campaign = Campaign.objects.create(
                    name = "new_campaign",
                    budget = data['budget'],
                )
                campaign.save()

                objects = Creative.objects.all()
                id_list = [obj.external_id for obj in objects]
                new_id = 1
                while True:
                    if str(new_id) in id_list:
                        new_id += 1
                    else:
                        break
                

    #__________________________________________________________________________________________

                creative = Creative.objects.create(
                    external_id = new_id,
                    name = 'new_creative',
                    campaign_id = random.choice(Campaign.objects.all()).id,
                    url = "creative/FfTcjdrDpw.png",
                    width = 200,
                    height = 400
                )
                creative.save()
        else:
            game = Game.objects.create(
                impressions_total = data['impressions_total'],
                auction_type = data['auction_type'],
                mode = data['mode'],
                budget = data['budget'],
                impression_revenue = data['impression_revenue'],
                click_revenue = data['click_revenue'],
                conversion_revenue = data['conversion_revenue'],
                frequency_capping = data['frequency_capping'],
                total_revenue = 0
            )
            game.save()


    #_____________________________________________________________________________________________
            reading()

            data = {
                'id': game.pk,
                'impressions_total': game.impressions_total,
                'auction_type': game.auction_type,
                'mode': game.mode,
                'budget': game.budget,
                'impression_revenue': game.impression_revenue,
                'click_revenue': game.click_revenue,
                'conversion_revenue': game.conversion_revenue,
                'frequency_capping': game.frequency_capping
            }

            
            print("game_started")
            print("auction-{},  mode-{},  freq- {}".format(data['auction_type'],data['mode'],data['frequency_capping']))
            print("rounds-{},  bugdet-{}".format(data['impressions_total'],data['budget']))
            print("revenues {}-{}-{}".format(data['impression_revenue'],data['click_revenue'],data['conversion_revenue']))
            
        return status_configue(data)
    