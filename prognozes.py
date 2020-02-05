import requests
r = requests.get(url='https://api.meteo.lt/v1/places/vilnius/forecasts/long-term')
print(r.json())
