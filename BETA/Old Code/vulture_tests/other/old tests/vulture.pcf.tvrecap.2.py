#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module for test results
import vultureSoup		# Crawler to scrape vulture.com for data and content
from selenium import selenium

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "TV Recap Module"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.tvrecap()

CSS = open('../data/vulture.pcf.tvrecap.css.txt', 'r').readlines()               # Contains CSS selectors for test 'a'
DATA = open('../data/vulture.pcf.tvrecap.data.txt', 'r').readlines()             # Contains links parsed using BeautifulSoup for test 'c'
CONTENT = open('../data/vulture.pcf.tvrecap.content.txt', 'r').readlines()       # Contains XPATH locators for test 'b'

# This test opens www.vulture.com and does the following:
#	Test a:  verifies that the TV Recap module and components exist on the page using CSS locators (CSS)
#       Test b:  verifies 
#       Test c:  asserts that all links can be clicked and do not return pages with 404 errors

x = 0


class TVRecap(unittest.TestCase):
    
    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
    
    def test_a(self):

    # Tests for the presence of elements in the module
	
	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("5000")
	
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
            
    def test_b(self):
    	    
    	n = 0
    	                     
    	pass

    def test_c(self):
    	    
    # Tests for the module's functionality
    	    
    	n = 0  
        sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
	
	for each in DATA:

	    d = DATA[n].strip('\n') 
        
            try:
            	sel.click("//a[@href='" + d + "']")
                sel.wait_for_page_to_load("50000")
            except Exception, e:
            	print "FAILURE " + d
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + d)
            else:
                L.log(BROWSERS[x], TEST, "PASS, PAGE LOADS", d)
                print "PASS " + d
                sel.go_back()
                sel.wait_for_page_to_load("50000")
                
    	    n += 1

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(TVRecap)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
