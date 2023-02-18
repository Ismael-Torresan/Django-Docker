import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "https://localhost:8000/api/products/products/"

response = requests.post(endpoint, json={"title": "kalsdhfjk"})

print(response.text)
