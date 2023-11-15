from selenium import  webdriver
import  pytest

driver=None
@pytest.fixture(scope='class')
def setup(request):
    global driver
    driver=webdriver.Chrome()
    request.cls.driver = driver
    driver.get('https://thankful-crow-visor.cyclic.app/')
    yield
    driver.close()

