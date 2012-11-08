#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys
import random
import cutSelectors

reload(sys)
sys.setdefaultencoding("utf-8")


class HomePageFindCollection(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
        
    def test_find_collection_content(self):
    	driver = self.driver
    	driver.get(self.base_url)
    	
    	# Fail unless the module is on the page
    	# Assert that the heading says FIND A COLLECTION 
    	# Assert that the first dropdown says Select a Season
    	# Assert that the second dropdown says Select a Designer
    	# Assert that all 8 seasons are in the module
    	
    	self.failUnless(driver.find_element_by_css_selector(collection_section))
    	self.assertEqual(driver.find_element_by_css_selector(collection_header).text, "FIND A COLLECTION")
    	self.assertEqual(len(driver.find_elements_by_css_selector(specific_season)), 8)
    	self.assertEqual(driver.find_element_by_css_selector(collection_season_dropdown).text, "Select a Season")
    	#self.assertEqual(driver.find_element_by_css_selector(collection_designer_dropdown).text, "Select a Designer")
    	
    def test_find_collection_functionality(self):
    	driver = self.driver
    	driver.get(self.base_url)
    	
    	# Select a random season (1-8) - will append ':nth-child(n)' to the selector
    	# Select a random designer (1-10) - ditto
    	# Verify the runway page loads
    	# Verify page title
    	
    	rand_season = random.randrange(1,8)
    	rand_designer = random.randrange(1,10)
    	
    	driver.find_element_by_css_selector(collection_season_dropdown).click()
    	driver.find_element_by_css_selector(specific_season + ':nth-child(' + str(rand_season) + ')').click()
    	#self.assertEqual(driver.find_element_by_css_selector(collection_designer_dropdown).text, "Select a Designer")
    	driver.find_element_by_css_selector(collection_designer_dropdown).click()
    	driver.find_element_by_css_selector(specific_designer + ':nth-child(' + str(rand_designer) + ') a').click()    
    	time.sleep(10)
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
        ########################################################################
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        

#########################################################################
#########################################################################

if __name__ == "__main__":
    
    HomePage = cutSelectors.HomePage()
    Selectors = HomePage.find_collection()
    
    collection_section = Selectors[0]
    collection_header = Selectors[1]
    collection_season_dropdown = Selectors[2]
    specific_season = Selectors[3]
    collection_designer_dropdown = Selectors[4]
    specific_designer = Selectors[5]
     
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageFindCollection)
    unittest.TextTestRunner(verbosity=2).run(suite)
