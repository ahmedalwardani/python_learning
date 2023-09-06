import requests
from datetime import datetime

USERNAME = "ahmedalwardani"
TOKEN = "abcdefghijklmnop"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
update_pixel_endpoint = f"{pixel_endpoint}/20230905"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response)

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today?: "),
}

# response = requests.post(pixel_endpoint, json=pixel_config, headers=headers)
# response.raise_for_status()
# print(response.text)

pixel_update_config = {
    "quantity": "300"
}

# response = requests.put(url=update_pixel_endpoint, json=pixel_update_config, headers=headers)
# response.raise_for_status()
# print(response.text)

response = requests.delete(url=update_pixel_endpoint, headers=headers)
response.raise_for_status()
print(response.text)
