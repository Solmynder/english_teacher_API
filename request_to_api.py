import requests

domain = "http://127.0.0.1:8000"
response = requests.get(domain + "/word/guess")
print(response.status_code)
print(response.json())