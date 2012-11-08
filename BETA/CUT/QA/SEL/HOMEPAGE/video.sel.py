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


class HomePageVideo(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
        
    def test_video(self):
    	driver = self.driver
    	driver.get(self.base_url)
    	
    	# Fail unless the video module is on the page
    	# Find the video headline and url
    	# Click the url to test page load
    	
    	self.failUnless(driver.find_element_by_css_selector(video_section))
    	
    	driver.find_element_by_css_selector(video_headline)
    	driver.find_element_by_css_selector(video_url).click()
        
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
    Selectors = HomePage.video_module()
    
    video_section = Selectors[0]
    video_url = Selectors[1]
    video_headline = Selectors[2]
    
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageVideo)
    unittest.TextTestRunner(verbosity=2).run(suite)
