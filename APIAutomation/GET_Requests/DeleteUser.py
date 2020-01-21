import requests

# API URL
url = "https://reqres.in/api/user/2"

respone = requests.delete(url)

# Fetch Response code
print("Deleting user response code is: ", respone.status_code)

assert respone.status_code == 204