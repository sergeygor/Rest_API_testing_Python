import requests
import json
import jsonpath

# API Base URL: # https://reqres.in/
# API Relative URL: # /api/users
url = "https://reqres.in/api/users"

# Read input json file
file = open("/Users/sergeygordeev/Desktop/EDU/Python/Rest_API_testing_Python/new_user_creation.json", 'r')
json_input = file.read()
request_json = json.loads(json_input)

file.close()
# Using POST: Create new resource on the server
# Make POST request with Json Input body
response = requests.post(url, request_json)
# print(response.content)

# Validating Response Code
assert response.status_code == 201

# Fetch header form response
print(response.headers)

# Fetch particular header
print(response.headers.get('Content-Length'))

# Parse response to JsonFormat
response_json = json.loads(response.text)

# Pick ID using Json path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])




# Using PUT: Update data on the server

