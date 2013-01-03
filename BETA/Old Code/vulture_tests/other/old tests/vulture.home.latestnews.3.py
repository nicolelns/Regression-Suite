#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module for test results
from selenium import selenium

BROWSERS = ('chrome', 'firefox')
BASEURL = "http://www.vulture.com"
TEST = "Latest News Module"

DATA = open('../data/vulture.home.latestnews.css.txt', 'r').readlines()

L = Logger.MainLogger(BASEURL, TEST)
x = 0

# This test opens www.vulture.com and does the following:
	#	Asserts the presence of the "Latest News" logo
	#	Tests to ensure that between 2 and 6 headlines appear in the module
	#	Clicks on the links to make sure pages load
	
	
class LatestNews(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL)
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
    
    def test_presence(self):
	
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
	
	# Verify that no less than 2 and no more than 6 headlines appear in the "Latest News" module
	
	count = sel.get_css_count('css=a[name=\"&lpos=Vulture: HomePage: Latest News\"]')

	if (count < 2) or (count > 6):
	    self.verificationErrors.append("Incorrect number of links, " + str(count) + " links found.")
	    L.log(BROWSERS[x], TEST, "FAIL", "Incorrect number of links in Latest News: " + str(count) + " links")
	else:
	    L.log(BROWSERS[x], TEST, "PASS", "Correct number of links in Latest News: " + str(count) + " links") 
	    
    def test_function(self):
    	    
        pass
    	    
    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
        
#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(LatestNews)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()