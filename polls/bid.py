from polls.api.bid_request import * 
from .models import Game


def optimal_bid(bid_request, previous_bid_request):
    game = Game.objects.order_by('id').last()
    budget = game.budget
    click_prob = bid_request.click_prob
    conv_prob = bid_request.conv_prob

    avg = budget / game.impressions_total
    if game.game_goal == "revenue":
        click_weight = game.click_revenue /(game.click_revenue + game.conversion_revenue+game.impression_revenue)
        conversion_weight = game.conversion_revenue /(game.click_revenue + game.conversion_revenue+game.impression_revenue)
        if avg>=2:
            res = avg*(click_prob * click_weight + conv_prob * conversion_weight)
        else:
            res = avg*(click_prob * click_weight + conv_prob * conversion_weight)/2
    else:
        res = click_prob*10/avg
    return round(res,2)

