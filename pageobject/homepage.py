from selenium.webdriver.common.by import By
import random
import string
from faker import Faker
from pageobject.common_methods import New,New1

fake = Faker()

cc = ["New York", "Los Angeles", "Chicago", "Houston", "Miami", "San Francisco", "Seattle", "Boston", "Dallas",
      "Denver"]


class DATA:
    @staticmethod
    def generate_random_username(length=8):
        letters = string.ascii_letters
        username = ''.join(random.choice(letters) for _ in range(length))
        return username

    @staticmethod
    def generate_random_email():
        return fake.email()

    @staticmethod
    def generate_random_phone_number():
        # Generate a random 10-digit number without leading zero
        number = ''.join([str(random.randint(1, 9)) for _ in range(9)])
        # Add a random digit at the beginning to avoid numbers that start with zero
        number = str(random.randint(1, 9)) + number
        return number

    @staticmethod
    def get_random_city(city_list=None):
        if city_list is None:
            city_list = cc
        return random.choice(city_list)





class Homepage(New):
    city = DATA.get_random_city()
    random_username = DATA.generate_random_username()
    random_email = DATA.generate_random_email()
    phone_number = DATA.generate_random_phone_number()

    def __init__(self, driver):
        self.driver = driver

    def fill_the_form_for_user(self, password):
        New.click_on_register(self)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys(self.random_username)

        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Email ']").send_keys(self.random_email)
        self.driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys(password)

        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Phone']").send_keys(self.phone_number)

        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Address']").send_keys(self.city)
        self.driver.find_element(By.XPATH, "//input[@placeholder='What is Your Favorite sports']").send_keys('cricket')
        self.driver.find_element(By.XPATH,"//button[normalize-space()='REGISTER']").click()

    def check_same_login(self, password):
        New.click_on_login(self)
        self.driver.find_element(By.XPATH, "//input[@id='exampleInputEmail1']").send_keys(self.random_email)
        self.driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys(password)
        New1.login(self)

