#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox', 'safari')
TEST = "Keep Up with Vulture Module - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)

CSS = open('../data/text/keepup.css.txt', 'r').readlines()		
DATA = []
        
x = 0

"""
Regression test for vulture.com's home page.  Keep Up with Vulture module
"""

#########################################################################
#########################################################################
	

class KeepUp(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
    
    def test_keepup(self):
	
	n = 0
	sel = self.selenium
        sel.open(BASEURL)
        sel.wait_for_page_to_load("50000")
        test = "Test A - Presence of Elements via CSS"
        print test
        
        # Loops through the data in the CSS file asserting each element is on the page
        
	for each in CSS:

	    c = CSS[n].strip('\n') 
        
            try:
                self.failUnless(sel.is_element_present("css=" + c))
                
            except AssertionError, e:
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], TEST, "FAIL, ELEMENT NOT FOUND", str(e) + c)
            
            else:
                L.log(BROWSERS[x], TEST, "PASS, ELEMENT FOUND", c)
                
            n += 1
            
        #self.c_click_test()
            
        ########################################################################
        
    def b_facebook_test(self):
    	    
    	pass

        ########################################################################

    def c_click_test(self):
    
    	n = 0 
        sel = self.selenium
        test = "Test C - Click on Links"
        print test
        
        """
        Webdriver will fix the bug with this section of the test
        
        # First, make sure each link can be clicked on and that the page loads
        
        for n in range(0,2):
        	
            if n == 0:
            	d = CSS[7].strip('\n')
            else:
            	d = CSS[8].strip('\n')
        	
            try:
            	sel.click("css=" + d)
                sel.wait_for_page_to_load("50000")
                
	    except Exception, e:
		print "FAILURE " + d, " does not load" + str(e)
		L.log(BROWSERS[x], test, "FAIL, PAGE DOES NOT LOAD", d, exception=str(e))
		
	    else:
	    	L.log(BROWSERS[x], TEST, "PASS, PAGE LOADS", d)
		sel.go_back()
	        sel.wait_for_page_to_load("50000")
	    
            n += 1
           
           
        """

        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(KeepUp)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()