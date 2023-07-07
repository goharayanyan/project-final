from rest_framework import serializers
from .models import BidRequest
from .models import Notification
from .models import Creative

#______________________________________________________________________

import json, random
from .models import BidRequest, BidResponse

class BidRequestSerializer:
    def __init__(self, data):
        self.data = json.loads(data)
        self.errors = {}

    def is_valid(self):
        required_fields = ['ext_id', 'imp', 'click', 'conv', 'site', 'ssp', 'user']
        for field in required_fields:
            if field not in self.data:
                self.errors[field] = f'The field "{field}" is required.'
        
        if not self.data.get('imp', {}).get('banner', {}).get('w'):
            self.errors['imp.banner.w'] = 'The field "imp.banner.w" is required.'
        if not self.data.get('imp', {}).get('banner', {}).get('h'):
            self.errors['imp.banner.h'] = 'The field "imp.banner.h" is required.'
        if not self.data.get('click', {}).get('prob'):
            self.errors['click.prob'] = 'The field "click.prob" is required.'
        if not self.data.get('conv', {}).get('prob'):
            self.errors['conv.prob'] = 'The field "conv.prob" is required.'
        if not self.data.get('site', {}).get('domain'):
            self.errors['site.domain'] = 'The field "site.domain" is required.'
        if not self.data.get('ssp', {}).get('id'):
            self.errors['ssp.id'] = 'The field "ssp.id" is required.'
        if not self.data.get('user', {}).get('id'):
            self.errors['user.id'] = 'The field "user.id" is required.'
        
        return not bool(self.errors)

    def save(self):
        bcat = self.data.get('bcat')
        bid_request = BidRequest.objects.create(
            ext_id=self.data['id'],
            imp_banner_w=float(self.data['imp']['banner']['w']),
            imp_banner_h=float(self.data['imp']['banner']['h']),
            click_prob=float(self.data['click']['prob']),
            conv_prob=float(self.data['conv']['prob']),
            site_domain=self.data['site']['domain'],
            ssp_id=self.data['ssp']['id'],
            user_id=self.data['user']['id'],
            bcat=json.dumps(bcat) if bcat else None
        )
        creative = random.choice(creative)
        bid_response = BidResponse.objects.create(
            creative=creative,
            bid_request=bid_request,
            bid=1
        )
        return bid_response


#______________________________________________________________________


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

#______________________________________________________________________



class CreativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creative
        fields = '__all__'

#______________________________________________________________________

from .models import Campaign

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'


#______________________________________________________________________

from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

#______________________________________________________________________

from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

#______________________________________________________________________

class BidResponseSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Creative
        fields = ('id', 'image_url', 'price', 'categories')
