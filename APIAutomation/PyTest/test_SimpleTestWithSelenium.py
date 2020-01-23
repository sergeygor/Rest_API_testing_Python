from selenium import webdriver
import pytest

a = 101

# @pytest.mark.skip("Don't execute on current build...")
def test_registration_valid_data():
    driver = webdriver.Chrome()
    baseURL = "http://www.thetestingworld.com/testings"
    driver.get(baseURL)
    driver.maximize_window()

    driver.close()
    driver.quit()


@pytest.mark.skipif(a > 100, reason="Don't run test as soon as a greater then 100")
def test_registration_invalid_data():
    driver = webdriver.Chrome()
    baseURL = "http://www.thetestingworld.com/testings"
    driver.get(baseURL)
    driver.maximize_window()

    driver.close()
    driver.quit()

def test_invalid_data():
    driver = webdriver.Chrome()
    baseURL = "http://www.thetestingworld.com/testings"
    driver.get(baseURL)
    driver.maximize_window()

    driver.close()
    driver.quit()






