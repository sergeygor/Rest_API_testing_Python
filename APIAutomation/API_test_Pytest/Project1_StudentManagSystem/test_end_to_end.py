"""
1. Add new student
2. Add technical skills
3. Add address
4. Fetch complete details
"""
import requests
import json
import jsonpath


# Add new student (POST)
def test_add_new_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("/Users/sergeygordeev/Desktop/EDU/Python/Rest_API_testing_Python/APIAutomation/"
                "API_test_Pytest/Project1_StudentManagSystem/RequestJson.json", "r")
    request_json = json.loads(file.read())
    response = requests.post(API_URL, request_json)
    print("Add New student response: {0}".format(response.text))
    id = jsonpath.jsonpath(response.json(), "id")
    print("The ID is: {0}".format(id[0]))

    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    f = open("/Users/sergeygordeev/Desktop/EDU/Python/Rest_API_testing_Python/APIAutomation/"
                "API_test_Pytest/Project1_StudentManagSystem/technical_skills.json", "r")
    request_json = json.loads(f.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url, request_json)
    print(response, response.text)

    address_api_url = "http://thetestingworldapi.com/api/addresses"
    f = open("/Users/sergeygordeev/Desktop/EDU/Python/Rest_API_testing_Python/APIAutomation/API_test_Pytest"
             "/Project1_StudentManagSystem/addressJson.json", "r")
    request_json = json.loads(f.read())
    request_json["stId"] = id[0]
    print(id[0])
    response = requests.post(address_api_url, request_json)
    print(response, response.text)
    

    # final_details_url = "http://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    # print(str(id[0]))
    # response = requests.get(final_details_url)
    # print(response)
