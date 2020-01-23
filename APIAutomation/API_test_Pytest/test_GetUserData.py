import requests
import json
import jsonpath
import pytest

@pytest.mark.Smoke
def test_fetch_user_details():
# API URL
    url = "https://reqres.in/api/users?page=2"
# Send Get Request
    response = requests.get(url)
# Parse Json format
    json_response = json.loads(response.text)
# Fetch value using Json Path
    for i in range(0, 3):
        first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].fist_name')
        print(first_name)