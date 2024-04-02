import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

# GET /pizzas
response = requests.get(url)
print(response.json())

# POST /pizzas 
mi_taco = {
    "base": "Tortilla",
    "guiso": "Guiso de Carne",
    "salsa": "Salsa de Taco",
    "toppings": ["Jamon", "Queso"]
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())

# PUT /pizzas/1
url_put= "http://localhost:8000/tacos/1"
edit_taco = {
    "base": "Taco",
    "guiso": "Guiso",
    "salsa": "Salsa",
    "toppings": ["Pepperoni", "Queso"]
}
response = requests.put(url_put, json=edit_taco)
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())

# DELETE /pizzas/1

response = requests.delete(url + "/1")
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())