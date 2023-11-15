from selenium.webdriver.common.by import By

class S:
    def __init__(self, driver):
        self.driver = driver
class New(S):
    def __init__(self, driver):
        self.driver = driver

    def click_on_homepage(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Home']").click()

    @staticmethod
    def click_on_register(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()

    @staticmethod
    def click_on_login(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()

    def click_on_cart(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Cart']").click()


class New1(S):
    @staticmethod
    def login(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='LOGIN']").click()
