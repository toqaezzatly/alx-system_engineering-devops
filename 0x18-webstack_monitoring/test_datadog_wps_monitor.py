#!/usr/bin/python3
import requests

api_key = 'your_datadog_api_key'
app_key = 'your_datadog_application_key'
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key,
}

# Query the Datadog API for write requests per second
response = requests.get(
    'https://api.datadoghq.com/api/v1/query?query=avg:system.diskio.writes{*}by{host}&from=now-5m&to=now',
    headers=headers
)
data = response.json()

if 'series' in data and len(data['series']) > 0:
    print("WPS is monitored")
else:
    print("WPS is not monitored")