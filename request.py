import requests

headers={
    'curso': 'python', 
    'version': '2.0',
    'autor':'joaquin'
}


params={
    'name':'nombre'
}

URL='https://httpbin.org/post'

response = requests.post(URL,headers=headers,params=params) #GET HTTP


#query => GET
#Cuerpo de peticion => POST
#Encabezado

if response.status_code==200:
    print(response.text)