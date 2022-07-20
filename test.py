import requests
import json

url = "https://api.shipengine.com/v1/rates/estimate"

unit = {"kg":"kilogram", "cm":"centimeter"}
weight_unit = quote_params["parcel"]["mass_unit"]
if(unit[weight_unit]):
    weight_unit = unit[weight_unit]
dimensions_unit = quote_params["parcel"]["distance_unit"]
if(unit[dimensions_unit]):
    dimensions_unit = unit[dimensions_unit]

from_postal_code = quote_params["address_from"]["zip"]
from_country_code = quote_params["address_from"]["country"]
to_postal_code = quote_params["address_to"]["zip"]
to_country_code = quote_params["address_to"]["country"]
weight = {
    "value": quote_params["parcel"]["weight"],
    "unit": weight_unit
}
dimensions = {
    "unit": dimensions_unit,
    "length": quote_params["parcel"]["length"],
    "width": quote_params["parcel"]["width"],
    "height": quote_params["parcel"]["height"],
}

json_request = {
    "carrier_ids": ["se-2634847", "se-2634846", "se-2634848"],
    "from_country_code": from_country_code,
    "from_postal_code": from_postal_code,
    "to_country_code": to_country_code,
    "to_postal_code": to_postal_code, 
    "weight": weight,
    "dimensions": dimensions,
    "confirmation": "none",
    "address_residential_indicator": "unknown",
    "ship_date": "2022-08-08T15:00:00.000Z"
}
payload = json.dumps(json_request)
headers = {
  'Host': 'api.shipengine.com',
  'API-Key': 'TEST_DR6z1zWA0vFKnL+Znjk3FpRlLBEKGpKDg7N/yF7AShY',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)


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