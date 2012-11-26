from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys
import cutSelectors


class HomePageLookBook(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
    
    def test_look_book_content(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # Fail unless the look book section is on the home page
        # Assert that the heading is in the look book section
        
        # Assert that there are an equal number of images and links in the module
        # Assert that there are 15 look books in the module

        self.failUnless(driver.find_element_by_css_selector(look_book_section))
        self.assertEqual(driver.find_element_by_css_selector(look_book_heading).text, "LOOK BOOKS")
        
        imgs = driver.find_elements_by_css_selector(look_book_image)
        links = driver.find_elements_by_css_selector(look_book_link)
        
        self.assertEqual(len(imgs), len(links))
        self.assertEqual(len(links), 15)
        
    def test_look_book_scrolling(self):
    	driver = self.driver 
    	driver.get(self.base_url) 
    	
    	# Click the next arrow 4 times
    	# Click the prev arrow 4 times
    	 
    	for n in range(4):
            driver.find_element_by_css_selector(look_book_next_arrow).click()
            time.sleep(1)
            
        for n in range(4):
            driver.find_element_by_css_selector(look_book_prev_arrow).click()
            time.sleep(1)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	
    HomePage = cutSelectors.HomePage()
    Selectors = HomePage.lookbook()	
    
    look_book_section = Selectors[0]
    look_book_heading = Selectors[1]
    look_book_image = Selectors[2]
    look_book_link = Selectors[3]
    look_book_next_arrow = Selectors[4]
    look_book_prev_arrow = Selectors[5]
    
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageLookBook)
    unittest.TextTestRunner(verbosity=2).run(suite)
