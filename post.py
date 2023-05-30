import requests


URL='https://httpbin.org/post'
params={
    'name':'Joaquin',
    'Apellido':'Batallanes',
    'email':'emag@gmail.com'
}

response = requests.post(URL) #GET HTTP



if response.status_code == 200:
    payload=response.json()
    print(payload)