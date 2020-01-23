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


def test_registration_invalid_data(setPath):
    baseURL = "http://www.thetestingworld.com/testings"
    driver.get(baseURL)
    driver.maximize_window()


def test_invalid_data(setPath):
    baseURL = "http://www.thetestingworld.com/testings"
    driver.get(baseURL)
    driver.maximize_window()
