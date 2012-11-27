from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys
import cutSelectors


class HomePageLede(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
    
    def test_lede(self):
        driver = self.driver
        driver.get(self.base_url)
        n = 0

        # For each article in lede,
        # Assert there is an image and a link
        # Click the next arrow
        
        # Finally, make sure the previous arrow works, click 10 times

        for each in driver.find_elements_by_css_selector(lede_article):
           
            try: 
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, lede_img))
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, lede_link))
                driver.find_element_by_css_selector(next_arrow).click()

            except AssertionError as e: 
                self.verificationErrors.append(str(e))
            
        for n in range(10):
            driver.find_element_by_css_selector(prev_arrow).click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    
    HomePage = cutSelectors.HomePage()
    Selectors = HomePage.lede()
    
    lede_article = Selectors[0]
    lede_img = Selectors[1]
    lede_link = Selectors[2]
    next_arrow = Selectors[3]
    prev_arrow = Selectors[4]

    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageLede)
    unittest.TextTestRunner(verbosity=2).run(suite)
