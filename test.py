#%%
from serpapi import GoogleSearch

params = {
  "api_key": "a7fb9738ac411e9813a404c20a8ac5bb70c0e15e840b95ccd5f85e1f66c71c8c",
  "engine": "google_flights",
  "hl": "zh-cn",
  "gl": "us",
  "departure_id": "LAX",
  "arrival_id": "BKK",
  "outbound_date": "2024-12-23",
  "return_date": "2024-12-31",
  "currency": "HKD",
  "stops": "3",
  "adults": "1",
  "children": "1",
  "infants_in_seat": "1",
  "travel_class": "3"
}

search = GoogleSearch(params)
results = search.get_dict()


import pprint
pprint.pp(results)

