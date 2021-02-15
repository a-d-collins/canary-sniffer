from pprint import pprint

import requests


# Case 1: Missing address or zipcode
params = {"zipcode": "94132"}

resp = requests.get("http://127.0.0.1:5000/api/v1/property/has-septic", params=params)

print("Case 1: missing address in call to flask endpoint.")
pprint(resp.json())

# Case 2: Successful request
params = {"address": "123 Not Main St",
          "zipcode": "94132"}

resp = requests.get("http://127.0.0.1:5000/api/v1/property/has-septic", params=params)

print("Case 2: successful call to flask endpoint.")
pprint(resp.json())
