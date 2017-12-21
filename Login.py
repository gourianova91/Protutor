import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Protutor(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()

	def test_LoginTutor(self):
		driver = self.driver
		driver.get("http://admin:AdminTut432@www.protutor-dev.com/")
		element = driver.find_element_by_xpath("//*[@id='navbar']/ul[2]/noindex[1]/a")
		element.click()
		time.sleep(0.5)
		email = driver.find_element_by_xpath("//*[@id='form-modal-loginForm']/div[1]/input[1]")
		psw = driver.find_element_by_xpath("//*[@id='form-modal-loginForm']/div[1]/input[2]")
		email.send_keys("12345@mailinator.com")
		psw.send_keys("123")
		login = driver.find_element_by_xpath("//*[@id='form-modal-loginForm']//button")
		login.click()


	def test_LoginUser(self):
		driver = self.driver
		driver.get("http://admin:AdminTut432@www.protutor-dev.com/")
		element = driver.find_element_by_xpath("//*[@id='navbar']/ul[2]/noindex[1]/a")
		element.click()
		time.sleep(0.5)
		email = driver.find_element_by_xpath("//*[@id='form-modal-loginForm']/div[1]/input[1]")
		psw = driver.find_element_by_xpath("//*[@id='form-modal-loginForm']/div[1]/input[2]")
		email.send_keys("222@mailinator.com")
		psw.send_keys("123")
		login = driver.find_element_by_xpath("//*[@id='form-modal-loginForm']//button")
		login.click()


	def tearDown(self):
		self.driver.quit()



if __name__ == "__main__":
    unittest.main()