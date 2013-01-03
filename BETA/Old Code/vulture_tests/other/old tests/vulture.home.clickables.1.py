#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module for test results
from selenium import selenium

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "Clickables Module"

CSS = open('../data/vulture.home.clickables.css.txt', 'r').readlines()
DATA = open('../data/vulture.home.clickables.data.txt', 'r').readlines()

L = Logger.MainLogger(BASEURL, TEST)
x = 0

# This test opens www.vulture.com and does the following:
#	Tests the Clickables module for the presence of integral elements
	

class Clickables(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]

    def test_a(self):

	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("5000")
	
	for each in CSS:

	    c = CSS[n].strip('\n') 
        
            try:
                self.failUnless(sel.is_element_present("css=" + c))
            except AssertionError, e:
            	print "FAILURE" + d
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], TEST, "FAIL, ELEMENT NOT FOUND", str(e) + c)
            else:
                L.log(BROWSERS[x], TEST, "PASS, ELEMENT FOUND", c)
            n += 1
	    	
    def test_b(self):
    	    
    # Tests for the correct content within the module
    	    
    	pass

    def test_c(self):
    	    
    # Tests for the module's functionality
    	 
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("5000")
	
	for n in range(0,8):

	    d = DATA[n].strip('\n') 
        
            try:
                self.failUnless(sel.click("xpath=//href=" + d))
                sel.wait_for_page_to_load("5000")
            except AssertionError, e:
            	print "FAILURE" + d
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + d)
            else:
                L.log(BROWSERS[x], TEST, "PASS, PAGE LOADS", d)
                print "PASS" + d
            n += 1
	    	
    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(Clickables)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
