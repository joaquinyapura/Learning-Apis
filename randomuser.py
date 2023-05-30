import requests

URL='https://randomuser.me/api/'

cant=int(input("ingrese la cantidad de usuarios"))

params={
    'results':cant
}

response=requests.get(URL,params=params)


if response.status_code==200:
    payload=response.json()
    results=payload.get('results')
    
    for u in results:
        name=u.get('name')
        print ("{title} {first} {last}".format (**name))