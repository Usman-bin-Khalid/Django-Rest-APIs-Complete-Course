import requests
endpoints = "http://127.0.0.1:8000/car/list"
getResponse = requests.get(endpoints)
print(getResponse.json())
print(getResponse.status_code)


