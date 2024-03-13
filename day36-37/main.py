import requests
import datetime as dt
from config import *


user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": graph_id,
    "name": "Pages Graph",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

now = dt.datetime.now()
today = (now.strftime("%Y%m%d"))

pixel_data_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
pixel_data = {
    "date": today,
    "quantity": input("How many pages did you read today? "),
}

response = requests.post(url=pixel_data_endpoint, json=pixel_data, headers=headers)
print(response.text)
