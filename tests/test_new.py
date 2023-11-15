import time

import pytest
from pageobject.homepage import Homepage


@pytest.mark.usefixtures('setup')
class Test1:
    password = 'shubham1'

    def test1(self):
        self.a = Homepage(self.driver)

        self.a.fill_the_form_for_user(self.password)

        time.sleep(10)
        self.driver.delete_all_cookies()
        self.a.check_same_login(self.password)
        time.sleep(10)
