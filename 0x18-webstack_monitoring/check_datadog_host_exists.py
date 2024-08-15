import requests

api_key = 'your_datadog_api_key'
app_key = 'your_datadog_application_key'
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key,
}

response = requests.get('https://api.datadoghq.com/api/v1/hosts', headers=headers)
hosts = response.json().get('host_list', [])

if any('XX-web-01' in host['name'] for host in hosts):
    print("Host exists")
else:
    print("Host not found")
