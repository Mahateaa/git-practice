import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=17.3850&longitude=78.4867&current=temperature_2m"

response = requests.get(url)

print(response.json())