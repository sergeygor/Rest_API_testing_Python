import requests
import json
import jsonpath
import pytest

# API URL
url = "https://reqres.in/api/users"

@pytest.fixture(scope="module")
def start_exec():
    global file
    file = open("/Users/sergeygordeev/Desktop/EDU/Python/Rest_API_testing_Python/new_user_creation.json", "r")

# a = 9
#v@pytest.mark.skipif(a >= 10, reason="Condition is not satisfied")
@pytest.mark.Smoke
def test_Create_New_User(start_exec):
# Read input json file

    json_input = file.read()
    request_json = json.loads(json_input)
# Make POST request with Json input body
    response = requests.post(url, request_json)
# Validating Response code
    assert response.status_code == 201

@pytest.mark.Sanity
def test_Create_Other_User(start_exec):
    # Read input json file
    file = open("/Users/sergeygordeev/Desktop/EDU/Python/Rest_API_testing_Python/new_user_creation.json", "r")
    json_input = file.read()
    file.close()
    request_json = json.loads(json_input)
    # Make POST request with Json input body
    response = requests.post(url, request_json)
    # Parse response from Json format
    response_json = json.loads(response.text)
    # Pick ID using Json Path
    id = jsonpath.jsonpath(response_json, "id")
    print(id[0])
