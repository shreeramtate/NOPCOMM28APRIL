import pytest
from selenium import webdriver
import html


@pytest.fixture
def setup(browser):
    url="https://admin-demo.nopcommerce.com/"
    if browser=='firefox':
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        return driver
    elif browser=='edge':
        driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver
    elif browser=='ie':
        driver = webdriver.Ie()
        driver.get(url)
        driver.maximize_window()
        return driver
    else:
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        return driver

def pytest_addoption(parser):     #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):      # This will return the broswer value to setup method
    return request.config.getoption("--browser")


#To generate HTMLS Report Add customized information to report
# It is hook for adding environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester Name'] = 'Shriram'
#
# # It is hook to delete/Modify Environment info to HTML Report
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
#



#It is hook for delete/modify Environment info o HTML Report
