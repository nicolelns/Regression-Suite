#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "Test for 404/500 Errors"

DATA = pickle.load(open('../data/pickle/404.data.p', 'rb')) 	        # c = function; Does the module work?

L = Logger.MainLogger(BASEURL, TEST)
x = 0

# This test opens www.vulture.com and does the following:
	#	Opens each of the subdirectories in URLS (clickables, music, etc.)
	#	Verifies that each page loads
	#	Ensures that no pages get 404 or 500 errors
	#	Tests an intentionally incorrect URL (ex. www.vulture.com/music/1234abcd)
	#	Verifies that all incorrect URLs give 404 errors, not 500 errors
	
#########################################################################
#########################################################################
	

class Vulture404(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
	
	########################################################################

    def test_c(self):

	n = 0
	sel = self.selenium
	
	# Tests for the module's functionality
	# Make sure no subfolders (level 2 pages) return 404 or 500 errors
	
	# First, open each page in DATA:  ex. www.vulture.com/books/, www.vulture.com/movies/

	for each in DATA:
				
	    d = DATA[n].strip('\n')
	    
	    sel.open(BASEURL + d)
	    sel.wait_for_page_to_load("5000")

	# 	NO 404 or 500
	
	    try:
	        title = sel.get_title()
	        
	    except AssertionError, e:
	    	print "Failure, " + TEST
	    	L.log(BROSWSERS[x], TEST, "FAIL", BASEURL + d + " PAGE HAS NO TITLE", str(e))
	    	
	    else:
	    	if re.search("Page Not Found", title, re.I):
	            print "Failure, " + TEST
	    	    L.log(BROWSERS[x], TEST, "FAIL", BASEURL + d + " does not load: 404 error", title)
	    	    
	        elif re.search("Internal Server Error", title, re.I):
	            print "Failure, " + TEST
		    L.log(BROWSERS[x], TEST, "FAIL", BASEURL + d + " does not load: 500 error", title)
		    
	        else: 
		    L.log(BROWSERS[x], TEST, "PASS", BASEURL + d + " loads OK", title)

	# 	Make sure all subfolders with an incorrect, bogus url return 404 errors ex: www.vulture.com/tv/1234trees/ 

	    sel.open(BASEURL + d + "abcd1234")
	    sel.wait_for_page_to_load("5000")
	    
	#	404 Verification / NO 500 Errors
	
	    try:
	        title = sel.get_title()
	        print title, ": title for ", d
	        
	    except AssertionError, e:
	    	print "Failure, " + TEST
	    	L.log(BROSWSERS[x], TEST, BASEURL + d + " PAGE HAS NO TITLE", str(e))
	    	
	    if n < 9:
	    	if re.search("Page Not Found", title, re.I):
	    	    L.log(BROWSERS[x], TEST, "PASS", BASEURL + d + " intentional 404", title)
	    	    
	        elif re.search("Internal Server Error", title, re.I):
	            print "Failure, " + TEST
		    L.log(BROWSERS[x], TEST, "FAIL", BASEURL + d + " 500 error, should be 404", title)
		    
	        else: 
	            print "Failure, " + TEST
		    L.log(BROWSERS[x], TEST, BASEURL + d + " test has a bug", title)

	    n += 1
	    
	########################################################################
	
    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
	
#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(Vulture404)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()