
import requests
import json


ssp_url = "https://ssp-api.example.com"
dsp_url = "https://dsp-api.example.com"

ssp_data = requests.get(ssp_url).json()
dsp_data = requests.get(dsp_url).json()

ctr_weight = 0.6
conv_weight = 0.4


inventory_sources = {}
for source in ssp_data:
    if source in dsp_data:
        ctr = ssp_data[source]["clicks"] / ssp_data[source]["impressions"]
        conv_rate = dsp_data[source]["conversions"] / dsp_data[source]["clicks"]
        inventory_sources[source] = {
            "ctr": ctr,
            "conv_rate": conv_rate
        }

# Normalize the data to a range between 0 and 1
max_ctr = max([inventory_sources[source]["ctr"] for source in inventory_sources])
max_conv_rate = max([inventory_sources[source]["conv_rate"] for source in inventory_sources])
for source in inventory_sources:
    inventory_sources[source]["ctr"] /= max_ctr
    inventory_sources[source]["conv_rate"] /= max_conv_rate

# Apply the bidding strategy to determine the bid for each source
for source in inventory_sources:
    bid = ctr_weight * inventory_sources[source]["ctr"] + conv_weight * inventory_sources[source]["conv_rate"]
    bid = inventory_sources[source]["bid"] 

# Submit the bids to the DSP
for source in inventory_sources:
    data = {"source": source, "bid": inventory_sources[source]["bid"]}
    response = requests.post(dsp_url, data=json.dumps(data))

#_______________________________________________________________________________

# max_bid = (conversion_rate * avg_order_value) / conversion_goal