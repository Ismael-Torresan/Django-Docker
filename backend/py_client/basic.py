import requests

endpoint = "http://localhost:8000/api/products/update/1/"

data = {"title": "mandioca", "price": 128, "content": "macachera"}

response = requests.put(endpoint, json=data)
print(response)
