#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys
import cutSelectors

reload(sys)
sys.setdefaultencoding("utf-8")


class HomePageSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
        
    def test_search(self):
    	driver = self.driver
    	driver.get(self.base_url)
    	
    	# For each search term, make sure user can click search box, enter term,
    	# click search button and search page appears
    	
    	search_terms = ('romney', 'balenciaga', 'gwyneth paltrow', '$3452qa;dfj', '4')
    	
    	for term in search_terms:
    	    print term
    	    driver.find_element_by_css_selector(search_bar).clear()
    	    driver.find_element_by_css_selector(search_bar).send_keys(term)
    	    driver.find_element_by_css_selector(search_button).click()
    	    time.sleep(1)
    	    self.assertEqual(driver.title, 'Sitewide Search - ' + term + ' -- New York Magazine')
    	    driver.back()
        
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
    Selectors = HomePage.search()
    
    search_bar = Selectors[0]
    search_button = Selectors[1]
    
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageSearch)
    unittest.TextTestRunner(verbosity=2).run(suite)
