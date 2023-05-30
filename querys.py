import requests


URL='https://httpbin.org/get'
params={
    'name':'Joaquin',
    'Apellido':'Batallanes',
    'email':'emag@gmail.com'
}

response = requests.get(URL,params=params) #GET HTTP




if response.status_code==200:
    payload=response.json()
    print(payload)