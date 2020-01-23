from selenium import webdriver
import pytest

@pytest.fixture(scope="module") # if need execute test fixture onese
def setPath():
    global driver
    driver = webdriver.Chrome()
    yield
    driver.close()
    driver.quit()


def test_registration_valid_data(setPath):
    baseURL = "http://www.thetestingworld.com/testings"
    driver.get(baseURL)
    driver.maximize_window()
    assert driver.title == "Login & Sign Up Forms"



def test_registration_invalid_data(setPath):
    baseURL = "http://www.thetestingworld.com/testings"
    driver.get(baseURL)
    driver.maximize_window()
    assert driver.current_url == "https://www.thetestingworld.com/testings/"


def test_invalid_data(setPath):
    baseURL = "http://www.thetestingworld.com/testings"
    driver.get(baseURL)
    driver.maximize_window()