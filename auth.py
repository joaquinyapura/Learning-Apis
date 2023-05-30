import requests

URL='https://httpbin.org/basic-auth/admin/admin'


session=requests.Session()
session.auth=('asd','admin')
response=session.get(URL)

if response.status_code==200: 
    print(response.json())
else:
    print("autenticacion fallida")