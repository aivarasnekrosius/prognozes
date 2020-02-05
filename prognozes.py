import requests
response = requests.get(url='https://api.meteo.lt/v1/places/vilnius/forecasts/long-term')
data = response.json()
visos_prgnozes = data['forecastTimestamps'][0]["airTemperature"]
print('Oro temperatura: ', visos_prgnozes, 'C')
