#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module for test results
from selenium import selenium

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "The Feed Module"

DATA = open('../data/vulture.home.thefeed.css.txt', 'r').readlines()

L = Logger.MainLogger(BASEURL, TEST)
x = 0

# This test opens www.vulture.com and does the following:

#	Asserts the presence of the "The Feed" logo and "Read More" logos
#	Verifies that each article in "The Feed" contains a timestamp

	

class TheFeed(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]

    def test_presence(self):

        sel = self.selenium
	sel.open("/")
	sel.wait_for_page_to_load("5000")

	# First, verify that the elements in the module are present on the page

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
	        
    def test_content(self):      
    	    
    	sel = self.selenium
	sel.open("/")
	sel.wait_for_page_to_load("5000")

        count = sel.get_css_count("css=a[class=\"permalink\"][name=\"&lpos=Vulture: HomePage: The Feed: Stories\"]")
        timestamp = sel.get_css_count("css=li.timestamp")
        if count != timestamp:
	    L.log(BROWSERS[x], TEST, "FAIL", "The Feed module is missing timestamps")
	else:  
       	    L.log(BROWSERS[x], TEST, "PASS", "The Feed module articles all contain timestamps")

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(TheFeed)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()