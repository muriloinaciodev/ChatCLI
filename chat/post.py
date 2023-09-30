import requests

url = 'http://127.0.0.1:5000/'
endpoint = input()
response = requests.post(url+endpoint, json={"username":"Bianca", "password":"senhabianca"})

