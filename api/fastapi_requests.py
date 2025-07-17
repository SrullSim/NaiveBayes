import requests


API_url = "http://localhost:8000/srull"
api_req_full = "http://localhost:8000{path}"

res = requests.get(api_req_full)
print(res)
print(res.url)
print(res.status_code)


