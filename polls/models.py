from django.db import models


#______________________________________________________________________
class BidRequest(models.Model):
    external_id = models.CharField(max_length=255, primary_key=True)
    imp_banner_w = models.IntegerField()
    imp_banner_h = models.IntegerField()
    click_prob = models.FloatField()
    conv_prob = models.FloatField()
    site_domain = models.CharField(max_length=255)
    ssp_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    bcat = models.JSONField(default=list)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.external_id)

#______________________________________________________________________

class Notification(models.Model):
    external_id = models.CharField(max_length=255, primary_key=True)
    win = models.BooleanField(default=False)
    price = models.FloatField(null = True)
    click = models.BooleanField(null = True)
    conversion = models.BooleanField(null = True)
    revenue = models.IntegerField(null = True)
    # change1 float-integer


#______________________________________________________________________

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    budget = models.IntegerField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    targeting = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
#______________________________________________________________________

class Category(models.Model):


    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    #parent = models.ForeignKey("self"~Q(bcat),blank=True, null = True, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name



#______________________________________________________________________

class Creative(models.Model):
    external_id = models.CharField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    category = models.ManyToManyField(Category)
    campaign = models.ForeignKey('Campaign', on_delete = models.CASCADE, blank = True, null = True)
    image = models.ImageField(upload_to = "creative/", blank = True, null = True)
    url = models.CharField(max_length = 255, blank = True, null = True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.name

#______________________________________________________________________

class BidResponse(models.Model):
    external_id = models.CharField(max_length=255, primary_key=True)
    bid = models.FloatField()
    bid_req = models.ForeignKey(BidRequest, on_delete=models.CASCADE)
    creative= models.ForeignKey(Creative, on_delete=models.CASCADE)
    #categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.external_id

#______________________________________________________________________

class Game(models.Model):
    impressions_total = models.IntegerField()
    auction_type = models.IntegerField(choices=[(1, 'First Price Auction'), (2, 'Second Price Auction')])
    mode = models.CharField(max_length=10, choices=[('free', 'Free'), ('script', 'Script')])
    budget = models.FloatField()
    impression_revenue = models.IntegerField()
    click_revenue = models.IntegerField()
    conversion_revenue = models.IntegerField()
    frequency_capping = models.IntegerField()
    game_goal = models.CharField(max_length=50, default = "revenue", choices=[('CPC', 'cpc'), ('revenue', 'Revenue')])
    total_revenue = models.IntegerField(default = 0)
    # change2 added game_goal