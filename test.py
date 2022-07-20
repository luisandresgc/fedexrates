import requests
import json

url = "https://api.shipengine.com/v1/rates"

payload = json.dumps({
  "rate_options": {
    "carrier_ids": [
      "se-2634848"
    ]
  },
  "shipment": {
    "validate_address": "no_validation",
    "ship_to": {
      "name": "Amanda Miller",
      "phone": "555-555-5555",
      "address_line1": "525 S Winchester Blvd",
      "city_locality": "San Jose",
      "state_province": "CA",
      "postal_code": "95128",
      "country_code": "US",
      "address_residential_indicator": "yes"
    },
    "ship_from": {
      "company_name": "Example Corp.",
      "name": "John Doe",
      "phone": "111-111-1111",
      "address_line1": "4009 Marathon Blvd",
      "address_line2": "Suite 300",
      "city_locality": "Austin",
      "state_province": "TX",
      "postal_code": "78756",
      "country_code": "US",
      "address_residential_indicator": "no"
    },
    "packages": [
      {
        "weight": {
          "value": 1,
          "unit": "ounce"
        }
      }
    ]
  }
})
headers = {
  'Host': 'api.shipengine.com',
  'API-Key': 'TEST_DR6z1zWA0vFKnL+Znjk3FpRlLBEKGpKDg7N/yF7AShY',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


# quote_params = {
#     address_from: {
#         zip: "64000",
#         country: "MX"
#     },
#     address_to: {
#         zip: "64000",
#         country: "MX"
#     },
#     parcel: {
#         length: 25.0,
#         width: 28.0,
#         height: 46.0,
#         distance_unit: "cm",
#         weight: 6.5,
#         mass_unit: "kg"
#     }
# }