#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module for test results
from selenium import selenium

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "Facebook Module - Not logged in"

DATA = open('../data/vulture.home.facebook.css.txt', 'r').readlines()

L = Logger.MainLogger(BASEURL, TEST)
x = 0

# This test opens www.vulture.com and does the following:
#	Tests the various Facebook app elements - not logged in
	

class Facebook(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]

    def test_presence(self):

    # Tests the Facebook application - not logged in
    # Test includes elements within the pop-up dialogue box to log in to Facebook
	
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
    	    
    # Tests for the correct content within the module
    	    
    	pass

    def test_function(self):
    	    
    # Tests for the module's functionality
    	    
    	pass

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(Facebook)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()