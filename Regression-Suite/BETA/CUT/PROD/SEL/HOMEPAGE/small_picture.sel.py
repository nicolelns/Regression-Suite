from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys
import cutSelectors

class HomePageSmallPicsModule(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
        
    def test_small_pictures_module(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # Fail unless the small Pictures section is on the page
        # Assert that the PICTURES heading is in the section
        # Assert that there is a link, image and excerpt

        self.failUnless(driver.find_element_by_css_selector(small_pictures_section))
        self.assertEqual(driver.find_element_by_css_selector(small_pictures_heading).text, "PICTURES")
        
        driver.find_element_by_css_selector(small_pictures_link)
        
    def test_small_pictures_function(self):
    	driver = self.driver
    	driver.get(self.base_url)
    	
    	# Click on the heading link and the image to verify article loads
        
        links = (small_pictures_description, small_pictures_image)
        
        for each in links:
            driver.find_element_by_css_selector(each).click()
            driver.back()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	
    # Grab selectors and assign to variables from homepageSelectors
    
    HomePage = cutSelectors.HomePage()
    Selectors = HomePage.small_pictures_module()
    
    small_pictures_section = Selectors[0]
    small_pictures_heading = Selectors[1]
    small_pictures_link = Selectors[2]
    small_pictures_image = Selectors[3]
    small_pictures_description = Selectors[4]
    
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageSmallPicsModule)
    unittest.TextTestRunner(verbosity=2).run(suite)
