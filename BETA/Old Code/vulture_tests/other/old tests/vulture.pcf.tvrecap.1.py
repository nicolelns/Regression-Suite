#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module for test results
from selenium import selenium

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "TV Recap Module"

# DATA
#	DATA contains CSS locators for the following elements and in the following order:   (The long lines of CSS are difficult to read, refer to the next comment line)
#	TV Recap Module, Header, Title, Latest Tab, All Shows Tab, Content, Articles, Article Header, Image, Article Title, Article Text, More Shows Link
#	TV_DATA contains the list of links within the "All Shows" tab

DATA = open('../data/vulture.pcf.tvrecap.css.txt', 'r').readlines()
TV_DATA = open('../data/vulture.pcf.tvrecap.links.txt', 'r').readlines()

L = Logger.MainLogger(BASEURL, TEST)
x = 0

# This test opens www.vulture.com and does the following:
	#	Verifies the presence of the elements in the TV Recap module
	#	Verifies the content in the TV Recap module
	#	Tests the links to make sure they work


class TVRecap(unittest.TestCase):
    
    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
    
    def test_presence(self):

    # Tests for the presence of elements in the module
	
	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("5000")
	
	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("5000")
	
	for each in DATA:

	    d = DATA[n].strip('\n') 
        
            try:
                self.failUnless(sel.is_element_present("css=" + d))
            except AssertionError, e:
            	print "FAILURE " + d
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], TEST, "FAIL, ELEMENT NOT FOUND", str(e) + d)
            else:
                L.log(BROWSERS[x], TEST, "PASS, ELEMENT FOUND", d)
            n += 1
            
        # Second, verify that all of the links appear in the "All Shows" tab
        
        n = 0
        
        for line in TV_DATA:    
            
            t = TV_DATA[n].strip('\n')
            
        #	Is the element present and in the correct location?
            
            try:
            	sel.is_element_present('//a[@href=' + "'" + t + "]'")
            	print t
            except AssertionError, e:    
            	L.log(BROWSERS[x], TEST, "FAIL", BASEURL + " ELEMENT MISSING", str(e) + ", " + t)
            else:
            	L.log(BROWSERS[x], TEST, "PASS", BASEURL + " ELEMENT FOUND", t)
            n += 1
            
    def test_content(self):
    	    
    	n = 0
    	
    	pass

    def test_function(self):
        
        pass

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(TVRecap)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
