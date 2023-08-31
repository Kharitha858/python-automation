from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("launching chrome browser...")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("launching Firefox browser...")
    else:
        driver=webdriver.Ie()

    return driver


def pytest_addoption(parser):    #this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):         #this will return the browser value to setup method
    return request.config.getoption("--browser")

###############PyTest HTML Report####################
#**It is hook for adding environment info to HTML Report

def pytest_configure(config):
    config._metadata['project name']="medifit"
    config._metadata["Module name"]="client side"
    config._metadata["tester"]="Haritha"

#*** It is hook for Delete/Modify environment info to HTML  Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("python_Home",None)
    metadata.pop("plugins",None)

