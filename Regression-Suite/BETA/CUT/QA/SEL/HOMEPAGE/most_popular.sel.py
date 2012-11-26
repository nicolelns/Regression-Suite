from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys
import cutSelectors


class HomePageMostPopular(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
    
    def test_mostpopular(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # Fail unless the Most Popular section is on the page
        # Assert that the MOST POPULAR heading is in the section
        # Assert that there are 5 numbered articles with links in the section

        self.failUnless(driver.find_element_by_css_selector(most_popular_section))
        self.assertEqual(driver.find_element_by_css_selector(most_popular_heading).text, "MOST POPULAR")
        self.assertEqual(len(driver.find_elements_by_css_selector(most_popular_link)), 5)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    
    HomePage = cutSelectors.HomePage()
    Selectors = HomePage.most_popular()
    
    most_popular_section = Selectors[0]
    most_popular_heading = Selectors[1]
    most_popular_link = Selectors[2]
    
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageMostPopular)
    unittest.TextTestRunner(verbosity=2).run(suite)
