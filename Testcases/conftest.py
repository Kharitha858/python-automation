import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#
#

# [common info]
# baseURL='http://10.10.20.23:3001/'
# username='megha'
# password='megha@123'

@pytest.fixture
def setup():
    # driver = webdriver.Chrome(r'venv/chromedriver.exe')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

