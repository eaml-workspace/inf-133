import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

# POST /deliveries
new_vehicle_data = {
    "chocolate_type": "tableta",
    "peso": "123",
    "sabor": "BLANCO"
}
response = requests.post(url=url, json=new_vehicle_data, headers=headers)
print(response.json())

new_vehicle_data = {
    "chocolate_type": "trufa",
    "peso": "932",
    "sabor": "CACAOO",
    "relleno":"CAFE"
}
response = requests.post(url=url, json=new_vehicle_data, headers=headers)
print(response.json())


# GET /deliveries
response = requests.get(url=url)
print(response.json())

# PUT /deliveries/{vehicle_id}
vehicle_id_to_update = 1
updated_vehicle_data = {
    "sabor": "CACAOOOOO"
}
response = requests.put(f"{url}/{vehicle_id_to_update}", json=updated_vehicle_data)
print("Chocolate actualizado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())

# DELETE /deliveries/{vehicle_id}
vehicle_id_to_delete = 1
response = requests.delete(f"{url}/{vehicle_id_to_delete}")
print("Chocolate eliminado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())