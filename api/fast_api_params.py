import requests


API_url = "http://localhost:8000/srull"


res = requests.get(API_url)
print(res)
print(res.url)
print(res.status_code)


