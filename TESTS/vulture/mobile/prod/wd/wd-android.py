from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Webdrivertest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities = {}, command_executor = "http://localhost:8080/wd/hub")
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.vulture.com/"
        self.verificationErrors = []
    
    def test_webdriver(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("a[name=\"&lpos=Vulture: HomePage: Latest News\"]").click()
        driver.back()
        driver.implicitly_wait(30)
        driver.find_element_by_link_text("Fiona Apple Extends Her North American Tour").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
