import requests

response = requests.get("http://127.0.0.1:5000/random")
data = response.text
list = data.split(":")
print(list[0])
print(list[1])