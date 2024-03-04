import requests

response = requests.get(url="# https://api.sunrise-sunset.org/json?lat=-6.475967&lng=106.729292")
response.raise_for_status()
data = response.json()
print(data)
