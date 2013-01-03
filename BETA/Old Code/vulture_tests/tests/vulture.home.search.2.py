#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "Search Bar Test"

L = Logger.MainLogger(BASEURL, TEST)

CSS = open('../data/vulture.home.search.css.txt', 'r').readlines()

x = 0

"""This is a regression test for the searh bar on Vulture's home page"""
""" Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  The DATA file contains this data"""
"""IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!"""	

#########################################################################
#########################################################################
	

class Search(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
	
	########################################################################
    
    def test_a(self):

    # Tests for the presence of elements in the module using CSS locators
    # This test is an 'assert' test: if any element is not present, the test fails
	
	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
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
            
        ########################################################################
	    
    def test_c(self):
    	    
    # Tests for the module's functionality
    # Clicks on each link based on its address (href attribute)
    # Makes sure the page loads
    	
    	n = 0 
        sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        # First, check the functionality of the search bar
        # Click inside the box, select the NY Mag radio button/Vulture button as appropriate
        # Type something into the search bar
        # Click search
        # Make sure the searched-for phrase appears in the title of the page that loads
        
        try:
        	
            sel.click("id=txt-ny-search")
            sel.click("id=sc-all")
            sel.type("id=txt-ny-search", "test")
            sel.click("id=btn-ny-search")
            sel.wait_for_page_to_load("50000")
            title = sel.get_title()
            
        except AssertionError, e:
      
            print "FAILURE, error with the search bar: " + str(e)
            L.log(BROWSERS[x], TEST, "Error with the search bar", str(e))
            
        else:
	    L.log(BROWSERS[x], TEST, "PASS, search bar OK", "OK")
	    
	    if not re.search("test", title, re.I):
	    	print "FAIL, text not in title of search bar"
    
            sel.go_back()
	    sel.wait_for_page_to_load("50000")
        
        try:
        	
            sel.click("id=txt-ny-search")
            sel.click("id=sc-vulture")
            sel.type("id=txt-ny-search", "test")
            sel.click("id=btn-ny-search")
            sel.wait_for_page_to_load("50000")
            title = sel.get_title()
            
        except AssertionError, e:
      
            print "FAILURE, error with the search bar: " + str(e)
            L.log(BROWSERS[x], TEST, "Error with the search bar", str(e))
            
        else:
	    L.log(BROWSERS[x], TEST, "PASS, search bar OK", "OK")
	    
	    if not re.search("test", title, re.I):
	    	print "FAIL, text not in title of search bar"
    
            sel.go_back()
	    sel.wait_for_page_to_load("50000")

        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(Search)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()