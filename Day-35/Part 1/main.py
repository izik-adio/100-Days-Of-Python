import requests

URL = "https://pro.openweathermap.org/data/2.5/forecast/hourly?"

parameters = {
    "appid": "b46a0926bc3a10498b5cc527f258143d",
    "lat": 6.493110,
    "lon": 3.384160
}

response = requests.get(url=URL, params=parameters)
status_code = response.status_code
response_data = response.json()

if status_code != 200:
    print(f'Error Code: {response_data["cod"]}, Error Message: {response_data["message"]}')
else:
    print(response_data)