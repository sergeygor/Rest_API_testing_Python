import requests
import json
import jsonpath

# API Base URL: # https://reqres.in/
# API Relative URL: # /api/users/2
url = "https://reqres.in/api/users/2"

# Read input Json file
file = open("/Users/sergeygordeev/Desktop/EDU/Python/Rest_API_testing_Python/updated_user.json", 'r')
json_input = file.read()
request_json = json.loads(json_input)

file.close()

# Make PUT request with Json input body
response = requests.put(url, request_json)
print(response.headers)

# Validating response code
assert response.status_code == 200

# Parse response content
response_json = json.loads(response.text)
print(response_json)

updated = jsonpath.jsonpath(response_json, 'name')
print(updated[0])
