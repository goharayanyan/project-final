import json

from django.views.generic import View
from data_status import ok_status, status_configue

from ..models import Category


class CategoryView(View):

    def get(self, request):    
        cats = Category.objects.all()
        data = []
        for cat in cats:
            data.append({'id': cat.int_id, 'name' : cat.name, 'code' : cat.code})
        return ok_status(data)
        
        
    
    def post(self, request):
        data = json.loads(request.body)

        category = Category.objects.create(
            code=data['code'],
            name=data['name']
        )

        category.save()

        data = {
            'id': category.int_id,
            'code': category.code,
            'name': category.name
        }

        return status_configue(data)