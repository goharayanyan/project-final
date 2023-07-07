from django.contrib import admin
from .models import BidRequest, Notification, Creative, Campaign, Category, Game, BidResponse

#______________________________________________________________________

class BidRequestAdmin(admin.ModelAdmin):
    list_display = ('external_id','click_prob', 'conv_prob', 'name', 'message')

#______________________________________________________________________

class BidResponseAdmin(admin.ModelAdmin):
    list_display = ("__all__")
    
#______________________________________________________________________

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('external_id','win', 'price', 'click', 'conversion', 'revenue')
    
#______________________________________________________________________

class CreativeAdmin(admin.ModelAdmin):
    list_display = ('external_id','name', 'campaign')

#______________________________________________________________________

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'budget', 'status')

#______________________________________________________________________

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','code', 'name')
    
#______________________________________________________________________


class BidResponseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'bid','bid_req', 'creative')
    
#______________________________________________________________________

class GameAdmin(admin.ModelAdmin):
    list_display = ('id','impressions_total', 'auction_type', 'budget', 'impression_revenue', 'click_revenue', 'conversion_revenue', 'total_revenue')


#______________________________________________________________________


admin.site.register(BidRequest, BidRequestAdmin)
admin.site.register(BidResponse, BidResponseAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Creative, CreativeAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)

#______________________________________________________________________

