from BasePage                import BasePage
from BasePage                import IncorrectPageException
from UIMap                   import LoginPageMap

class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
  

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10, 
                                           "xpath", 
                                           LoginPageMap['LoginButtonXpath']
            )
        except:   
            raise IncorrectPageException

    def login_button_click(self):
        self.click(10, 
            "xpath", 
             LoginPageMap['LoginButtonXpath']
        )
    
    def login_tutor(self):
        self.fill_out_field("xpath", 
                            LoginPageMap["EmailFieldXpath"], 
                            "12345@mailinator.com"
        )
        self.fill_out_field("xpath", 
                            LoginPageMap['PasswordFieldXpath'], 
                            "123"
        )
        self.click(10, 
                   "xpath", 
                   LoginPageMap['SubmitButtonXpath']
        )

    def login_user(self):
        self.fill_out_field("xpath", 
                            LoginPageMap["EmailFieldXpath"], 
                            "222@mailinator.com"
        )
        self.fill_out_field("xpath", 
                            LoginPageMap['PasswordFieldXpath'], 
                            "123"
        )
        self.click(10, 
                   "xpath", 
                   LoginPageMap['SubmitButtonXpath']
        )



