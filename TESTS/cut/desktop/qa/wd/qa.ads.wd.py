#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import re
#import Logger

reload(sys)
sys.setdefaultencoding("utf-8")

chromedriver = '/Library/Python/2.7/site-packages/chromedriver'

"""
The below code is for the Internet Explorer remote driver; These tests were developed on a Mac :)

"""

PROXY = "localhost:8080"

webdriver.DesiredCapabilities.INTERNETEXPLORER['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}


BASEURL = raw_input("Please enter a BaseURL: ")
BROWSERS = ('chrome', 'firefox', 'ie')
TEST = "The Cut Article Pages - Desktop - Ads"

#L = Logger.MainLogger(BASEURL, TEST)

CSS = open('../data/text/ads.css.txt', 'r').readlines()
URLS = {}

keys = URLS.keys()
values = URLS.values()

x = 0

"""
This is a test for ads on The Cut's article pages


"""	

#########################################################################
#########################################################################

class Ads(unittest.TestCase):

    def setUp(self):
    	    
        if x == 0:
            self.driver = webdriver.Chrome(chromedriver)
            
        elif x == 1:    
            self.driver = webdriver.Firefox() 
            
        elif x == 2:
    	    self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.INTERNETEXPLORER)
        
        #elif x == 3:
	    #self.driver = webdriver.Remote(desired_capabilities = {}, command_executor = "http://localhost:8080/wd/hub")
        
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
	
    def test_ads(self):
        
        """
    	The fail test is meant to "fail", in the sense that the CSS elements should NOT be on the page after nav update.
    	The element not being found is considered a pass.
    	
    	PASSING CONDITIONS:  None of the elements are found on the page.
    	FAILING CONDITIONS:  Any of the elements are found on the page.
    	"""	
    
	n = 0
        driver = self.driver
        driver.get(BASEURL)
        test = "Test A - Presence of Elements via CSS"
        print test
        
        # Loops through the data in the CSS file asserting each element is on the page
        
        for each in CSS:

	    c = CSS[n].strip('\n')
            
            try:
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, c))
                
            except AssertionError, e:
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e))
                #L.log(BROWSERS[x], test, "FAIL, ELEMENT FOUND", c, exception=str(e))
            
            #else:
                #L.log(BROWSERS[x], test, "PASS, ELEMENT NOT FOUND", c)
                
            n += 1
	
	########################################################################
    	 
    def is_element_present(self, how, what):
    	    
        try: 
            self.driver.find_element(by=how, value=what)
        
        except NoSuchElementException, e: 
            return False
        
        return True
    
        ########################################################################
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for x in range(0,3):

    suite = unittest.TestLoader().loadTestsFromTestCase(GiantImage)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
