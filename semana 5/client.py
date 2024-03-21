import requests
url = "http://localhost:8000"
headers = {'Content-type': 'application/json'}


response = requests.get(f"{url}/posts")
print(response.text)

url_post = url+"/posts"
nuevo_post={
        "title":"Mi experiencia como dev",
        "content":"Esta tremendo, dificil",
}

response =requests.post(url=url_post, data=nuevo_post, headers=headers)#el parametro para enviar la informacion no es json
print(response.text)

response = requests.get(f"{url}/posts")
print(response.text)

