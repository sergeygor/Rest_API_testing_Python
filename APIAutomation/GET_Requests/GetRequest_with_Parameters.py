"""
API Testing using Python-Parameters
1. Creating Dictionary of Parameters
2. Send Parameters with Request
"""

import requests

param = {"name":"tester", "email":"tester@mytest.com", "number":"999-000-9999"}

response = requests.get("https://httpbin.org/get", params=param)
print(response.text)

