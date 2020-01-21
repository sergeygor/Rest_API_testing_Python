import requests
import json
import jsonpath


# https://reqres.in/
# http://jsonpath.com/?

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
# print(response.content)
# print(response.headers)

# Validate status code
print("The status code is:", response.status_code)
assert response.status_code == 200

# Fetch response header
print("The header is:", response.headers)

# Fetch specific headers content
print("The header specific content Date:", response.headers.get('Date'))
print("The header specific content Server:", response.headers.get('Server'))

# Fetch cookies
print("The cookies:", response.cookies)

# Fetch encoding
print("The Encoding:", response.encoding)

# Fetch time taken between request send and response from server
print("The Elapsed: ", response.elapsed)

# Parse response from Json Format
json_response = json.loads(response.text)
print(json_response)

# Fetch value using json path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print("Total pages: {0}".format(pages[0]))
assert pages[0] == 2

first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
print("First name = {}".format(first_name[0]))
assert first_name[0] == 'Michael'


print("**************************************************")
for i in range(0, 6):
    first_nameAll = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print("First name all = {}".format(first_nameAll[0]))
    print(type(first_nameAll[0]))





