import requests
import json


base_url = "http://127.0.0.1:8000/"
Sec_url = "api/Common/"
data = {
    "user": "2",
    "id": "3",
    "State": "Its Karnataka",
    "Address": "something"
}
# it should be a json not a python dictionary#so dump the dictionary to jsnoString
data = json.dumps(data)
r = requests.put(base_url+Sec_url, data=data)
# print(r)
# print(type(r))
# print(r.text)
print(r.json())
# data = json.dumps(r.text)
# print(type(r.text))
# print(data)
# print(type(data))
