#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox', 'safari')
TEST = "Media Kit Module"

CSS = ('html.js body#nymag.vulture div#wrap-wrap div#wrap div#content div#content-secondary div.parsys div.parbase section.vulture-network a img')

L = Logger.MainLogger(BASEURL, TEST)
x = 0

# This test opens www.vulture.com and does the following:
#	ENTER INFORMATION
	

class MediaKit(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
	
	########################################################################

    def test_a(self):

    # Tests for the presence of elements in the module using CSS locators
    # This test is an 'assert' test: if any element is not present, the test fails
	
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        # Loops through the data in the CSS file asserting each element is on the page
        
	try:
            self.failUnless(sel.is_element_present("css=" + CSS))
                
        except AssertionError, e:
            print "FAILURE " + CSS
            self.verificationErrors.append(str(e))
            L.log(BROWSERS[x], TEST, "FAIL, ELEMENT NOT FOUND", str(e) + CSS)
            
        else:
            L.log(BROWSERS[x], TEST, "PASS, ELEMENT FOUND", CSS)
               
        ########################################################################
	    
    def test_bc(self):
    	    
    # Tests for the correct content within the module
    # This is a 'verify' test, it will not fail the whole test if one item fails
    	
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        self.failUnless(sel.is_element_present("//img[@src='http://images.nymag.com/images/2/promos/10/09/vulture_network_banner.gif']"))
        
        # Click on the link and verify that the correct page loads
        
        try:
            sel.click("//a[@href='http://nymag.com/newyork/mediakit/#/Vulture?d1=untitled&d1m1=vultureMgr&d1m1e=The%20Vulture%20Network']")
            sel.wait_for_page_to_load("50000")
            
        except AssertionError, e:
            print "link not clickable"
            self.verificationErrors.append(str(e))
            L.log(BROWSERS[x], TEST, "FAIL, cannot click on the link/page does not load", str(e))
          
        else:
            try:
                self.assertEqual(sel.get_title(), "New York Media")
            except AssertionError, e:
                L.log(BROWSERS[x], TEST, "FAIL, title is incorrect/incorrect page loads", str(e))
            else:
            	L.log(BROWSERS[x], TEST, "PASS, page loads, OK", "New York Media")

        ########################################################################  
    
    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(MediaKit)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()