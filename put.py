import requests


#GET = get
#POST= post
#PUT = put
#DELETE = delete


URL='https://httpbin.org/put'
response= requests.put(URL, params={'name':'eduardo'})


if response.status_code==200: 
    print(response.text)