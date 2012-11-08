from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
#from selenium.common.action_chains import ActionChains
import unittest, time, re, sys
import cutSelectors


class HomePageUniversalNav(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
    
    def test_non_hover_links(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # For each static link, 
        # Find the element by css selector (in static_links - a tuple)
        # Click on each url and verify page load, go back
        
        for data in static_links:
            driver.find_element_by_css_selector(data[0]).click()
            time.sleep(1)
            self.assertEqual(driver.current_url, data[1])
            driver.back()
    """ 
    def test_hover_links(self):
        driver = self.driver
        driver.get(self.base_url)
    
        for data in hover_links:
            driver.find_element_by_css_selector(data[0]).click()
            time.sleep(1)
            self.assertEqual(driver.current_url, data[1])
            driver.back()
    """     
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
        
    def hover(self, locator):
        self.locator = locator
        driver = self.driver
        
        element = driver.find_element_by_css_selector(self.locator)
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    
    HomePage = cutSelectors.HomePage()
    Selectors = HomePage.universal_nav()
    
    static_links = Selectors[0]
    mouseover_menu = Selectors[1]
    
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageUniversalNav)
    unittest.TextTestRunner(verbosity=2).run(suite)

