import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "https://localhost:8000/api/products/products/"

response = requests.get(endpoint)

print(response.text)
