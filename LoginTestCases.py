from BaseTestCase import BaseTestCase
from Properties   import Protutor_Properties
from Login        import LoginPage
import unittest
import time

class LoginTestCases(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(LoginTestCases, self).setUp()
        loginPageURL = Protutor_Properties['Base_URL']
        self.navigate_to_page(loginPageURL)

    def test_LoginTutor(self):
        login_page_obj = LoginPage(self.driver)
        time.sleep(2)
        login_page_obj.login_button_click()
        time.sleep(2)
        login_page_obj.login_tutor()
        time.sleep(5)

    def test_LoginUser(self):
        login_page_obj = LoginPage(self.driver)
        time.sleep(2)
        login_page_obj.login_button_click()
        time.sleep(2)
        login_page_obj.login_user()
        time.sleep(5)

    def tearDown(self):
        super(LoginTestCases, self).tearDown()

if __name__ == "__main__":
    unittest.main()