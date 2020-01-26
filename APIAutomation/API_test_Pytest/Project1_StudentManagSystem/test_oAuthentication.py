"""
oAuthentication
1. Send request and generate authentication talking
2. Pick this talking and make variables
3. Pass this talking as a header in further request
"""

import json
import jsonpath
import requests

def test_oauth_api():
    token_url = "http://thetestingworldapi.com/Token"
    data = {
        "grand":"password",
        "username":"admin",
        "password":"password"
    }
    response = requests.post(token_url, data)
    token_value = jsonpath.jsonpath(response.json(), "access_token")

    auth = {
        "Authorization": "Bearer" + token_value[0]
    }
    API_URL = "http://thetestingworldapi.com/api/StDetails/1104"
    respond = requests.get(API_URL, headers=auth)
    print(respond.text)