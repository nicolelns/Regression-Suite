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


class HomePageGiantImage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
        
    def test_giant_image_content(self):
    	driver = self.driver
    	driver.get(self.base_url)
    	
    	# Fail unless the module is on the page
    	# Verify that the PICTURES button is in the module and has the right text
    	#  
    	
    	self.failUnless(driver.find_element_by_css_selector(giant_img_section))
    	self.assertEqual(driver.find_element_by_css_selector(giant_img_pics_button).text, "PICTURES")
    	driver.find_element_by_css_selector(giant_img_excerpt)
    	driver.find_element_by_css_selector(giant_img_headline)
    	
    def test_giant_image_functionality(self):
    	driver = self.driver
    	driver.get(self.base_url)
    	
    	# Click on the image, headline and PICTURES button
    	# Verify the article page loads
    	
    	links = (giant_img_image, giant_img_headline, giant_img_pics_button)
    	
    	for each in links:
    	    driver.find_element_by_css_selector(each).click()
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
    Selectors = HomePage.giant_image()
    
    giant_img_section = Selectors[0]
    giant_img_image = Selectors[1]
    giant_img_headline = Selectors[2]
    giant_img_excerpt = Selectors[3]
    giant_img_pics_button = Selectors[4]
     
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageGiantImage)
    unittest.TextTestRunner(verbosity=2).run(suite)
