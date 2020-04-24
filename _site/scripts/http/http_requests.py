import requests

# Prepare HTTP request headers
headers = {
    'User-agent': 'Mozilla/5.0'
}

# URL to which request is sent
url = "http://www.google.com.hk"

# Send HTTP request
response = requests.get(url, headers=headers)

# Print out response
print("Status code: {}".format(response.status_code))
print("Content:")
print(response.text[:200])
