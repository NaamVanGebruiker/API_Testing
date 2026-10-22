

import requests

baseUrl = "https://en.wikipedia.org/api/rest_v1/"
# baseUrl = "https://webhook.site/e4d48aa9-14ad-4d38-8d65-bc11705dfde3/"

headers = {"accept": "*/*", "accept-encoding": "gzip, deflate, br", "cache-control": "no-cache"}

response = requests.get(f"{baseUrl}page/summary/Earth", headers=headers)

if response.status_code == 200:
    print("success")
else:
    print(f"false: {response.status_code}")
    print(response.reason)