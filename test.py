import requests
import json

url = "https://api.shipengine.com/v1/rates/estimate"

payload = json.dumps({
    "carrier_ids": ["se-2634847", "se-2634846", "se-2634848"],
    "from_country_code": "MX",
    "from_postal_code": "64000",
    "to_country_code": "MX",
    "to_postal_code": "64000 ", 
    "weight": {
        "value": 6.5,
        "unit": "kilogram"
    },
    "dimensions": {
        "unit": "centimeter",
        "length": 25.0,
        "width": 28.0,
        "height": 46.0
    },
    "confirmation": "none",
    "address_residential_indicator": "unknown",
    "ship_date": "2022-08-08T15:00:00.000Z"
})
headers = {
  'Host': 'api.shipengine.com',
  'API-Key': 'TEST_DR6z1zWA0vFKnL+Znjk3FpRlLBEKGpKDg7N/yF7AShY',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.json())
response_json = response.json()
new_response = []
for i in response_json:
    if(i['error_messages']==[]):
        price = 0
        price+=i["shipping_amount"]["amount"]
        price+=i["insurance_amount"]["amount"]
        price+=i["confirmation_amount"]["amount"]
        price+=i["other_amount"]["amount"]

        service_level = {
            "name":i["service_type"],
            "token":i["service_code"]
        }
        json = {
            "price":price,
            "currency":i["shipping_amount"]["currency"].upper(),
            "service_level":service_level
        }
        new_response.append(json)
print(new_response)

#** ORIGINAL
# {
#   "carrier_id": "se-2634848",
#   "from_country_code": "US",
#   "from_postal_code": "78756",
#   "to_country_code": "US",
#   "to_postal_code": "95128", 
#   "weight": {
#     "value": 1,
#     "unit": "pound"
#   },
#   "dimensions": {
#     "unit": "inch",
#     "length": 0,
#     "width": 0,
#     "height": 0
#   },
#   "confirmation": "none",
#   "address_residential_indicator": "unknown",
#   "ship_date": "2022-08-08T15:00:00.000Z"
# }