import requests
card_number= "BT1-010"
url=("http://digimoncard.io/api-public/search.php?card=(card_number)")

response= requests.request(
    method="GET",
    url=url,
    headers= {"Content-Type":"aplication/json"},
    data={}
)
print(response.text)