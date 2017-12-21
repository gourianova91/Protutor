from selenium import webdriver

class BaseTestCase(object):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def navigate_to_page(self, url):
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()
