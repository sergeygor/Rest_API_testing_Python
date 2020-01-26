import requests
import json
import jsonpath

# Add New student in the system (POST)
def test_add_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("/Users/sergeygordeev/Desktop/EDU/Python/Rest_API_testing_Python/APIAutomation/"
                "API_test_Pytest/Project1_StudentManagSystem/RequestJson.json", "r")
    json_request = json.loads(file.read())
    response = requests.post(API_URL, json_request)
    print("Add New student response: {0}".format(response.text))


# Fetch Student Details(GET)
def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/155727"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)  # or json_response = response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response, "data.id")
    print("Student ID: {0}".format(id))
    assert id[0] == 155727
#
# Student detail update (PUT)
def test_update_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/155727"
    file = open("/Users/sergeygordeev/Desktop/EDU/Python/Rest_API_testing_Python/APIAutomation/API_test_Pytest"
                "/Project1_StudentManagSystem/RequestJsonUpdated.json", "r")
    json_request = json.loads(file.read())
    response = requests.put(API_URL, json_request)
    print("Response after update: {0}".format(response.text))


# Validate the Student Detail Updated
def test_get_validate_student_data_updated():  # Validate the data was updated
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/155727"
    print("******")
    response = requests.get(API_URL)
    print("Response request.get: ", response.text)
    json_response = json.loads(response.text)  # or json_response = response.json()
    print("Response json_response: ", json_response)
    id = jsonpath.jsonpath(json_response, "data.id")
    print("Student ID: ", id)
    assert id[0] == 155727
#
# Delete student (DELETE)
def test_delete_student():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/155727"
    response = requests.delete(API_URL)
    print("Deleted data response: ", response.text)
#
def test_get_student_data(): # The test should be fail becouse data deleted
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/155727"
    response = requests.get(API_URL)
    print(response.text)
    json_response = json.loads(response.text)  # or json_response = response.json()
    id = jsonpath.jsonpath(json_response, "data.id")
    print(id)
    assert id[0] == 155727


