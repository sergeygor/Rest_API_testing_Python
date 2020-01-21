"""
API Testing using Python - Headers
1. Create Dictionary of Request - Headers
2. Send Headers with Request
"""


import requests


# Custom Header
headerdata = {"T1":"First_Header", "T2":"Second_Header"}

response = requests.get("https://httpbin.org/get", headers=headerdata)
print(response.text)