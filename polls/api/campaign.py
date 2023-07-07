import json

from django.views.generic import View
from data_status import data_status_campaign

from ..models import Campaign


class CampaignView(View):
    
    def get(self, request):    
        cvs = Campaign.objects.all()
        data = []
        for cv in cvs:
            data.append({'id': cv.id, 'name' : cv.name, 'budget' : str(cv.budget)})

        return data_status_campaign(data)
    
    
    
    def post(self, request):
        data = json.loads(request.body)

        campaign = Campaign.objects.create(
            name=data['name'],
            budget=data['budget'],
            start_date=data.get('start_date'),
            end_date=data.get('end_date'),
            status=data.get('status'),
            targeting=data.get('targeting')
        )

        campaign.save()

        data = {
            'id': campaign.id,
            'name': campaign.name,
            'budget': campaign.budget,
        }

        return data_status_campaign(data)