from selenium import webdriver
import pytest



@pytest.mark.Smoke
def test_registration_valid_data():
    driver = webdriver.Chrome()
    baseURL = "http://www.thetestingworld.com/testings"
    driver.get(baseURL)
    driver.maximize_window()

    driver.close()
    driver.quit()


@pytest.mark.Sanity
def test_registration_invalid_data():
    driver = webdriver.Chrome()
    baseURL = "http://www.thetestingworld.com/testings"
    driver.get(baseURL)
    driver.maximize_window()

    driver.close()
    driver.quit()

@pytest.mark.Smoke
def test_invalid_data():
    driver = webdriver.Chrome()
    baseURL = "http://www.thetestingworld.com/testings"
    driver.get(baseURL)
    driver.maximize_window()

    driver.close()
    driver.quit()