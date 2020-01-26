import json
import jsonpath
import requests


def test_add_new_student():
    global id
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open("/Users/sergeygordeev/Desktop/EDU/Python/Rest_API_testing_Python/APIAutomation/API_test_Pytest"
             "/Project1_StudentManagSystem/RequestJson.json", "r")
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    id = jsonpath.jsonpath(response.json(), "id")
    print("< ID is: {0} >".format(id[0]), response, response.text)

def test_get_details():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/" +str(id[0])
    response = requests.get(API_URL)
    print(response, response.text)
