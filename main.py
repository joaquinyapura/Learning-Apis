import requests


URL='https://httpbin.org/get'

response = requests.get(URL) #GET HTTP

payload=response.json()

print(payload.get('origin'))
print(payload.get('headers'))