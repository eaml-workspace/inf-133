import requests

url='http://localhost:5000/'

ruta_query= "saludar?nombre=Emanuel"
get_response=requests.request(method='GET', url=url+ruta_query)
print(get_response.text)

ruta_suma= "sumar?num1=2&num2=3"
get_response=requests.request(method='GET', url=url+ruta_suma)
print(get_response.text)

ruta_suma= "sumar?num1=2"
get_response=requests.request(method='GET', url=url+ruta_suma)
print(get_response.text)

ruta_palin= "palindromo?cadena=reconocer"
get_response=requests.request(method='GET', url=url+ruta_palin)
print(get_response.text)

ruta_palin= "palindromo?cadena=papas"
get_response=requests.request(method='GET', url=url+ruta_palin)
print(get_response.text)

ruta_palin= "palindromo"
get_response=requests.request(method='GET', url=url+ruta_palin)
print(get_response.text)

ruta_contar= "contar?cadena=exepciones&vocal=e"
get_response=requests.request(method='GET', url=url+ruta_contar)
print(get_response.text)

ruta_contar= "contar?cadena=exepciones"
get_response=requests.request(method='GET', url=url+ruta_contar)
print(get_response.text)