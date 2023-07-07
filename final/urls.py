from django.contrib import admin
from django.urls import path
from polls import views
from polls.api.bid_request import *
from polls.api.creative import *
from polls.api.notification import *
from polls.api.campaign import *
from polls.api.category import *
from polls.api.configuration import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path('rtb/bid/', BidRequestView.as_view()),
    path('rtb/notify/', NotificationView.as_view()),
    path('api/creatives/', CreativeView.as_view()),
    path('api/campaigns/', CampaignView.as_view()),
    path('api/categories/', CategoryView.as_view()),
    path('game/configure/', GameView.as_view()),
    path('bidcreatives/', views.BidResponseList.as_view()),
]




