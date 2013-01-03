#! /usr/bin/python

import unittest
import time, datetime
import re
import pickle     
import Logger                   # Logging module (for test results, outputs results to a .txt file)
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox', 'safari')
TEST = "Test for 404/500 Errors - Desktop - Vulture"

DATA = open('../data/text/404.data.txt', 'r').readlines() 	        

L = Logger.MainLogger(BASEURL, TEST)
x = 0

"""
This is a regression test for 404/500 errors on Vulture's pages:
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  
The DATA file is a hand-coded text file, customized for this module.

IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!
"""
	
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
	
	"""
	Tests for the module's functionality
	This test opens each page and verifies that no subfolders (level 2 pages) return 404 or 500 errors
	"""

	for each in DATA:
				
	    d = DATA[n].strip('\n')
	    
	    sel.open(BASEURL + d)
	    sel.wait_for_page_to_load("5000")

	# 	NO 404 or 500
	
	    try:
	        title = sel.get_title()
	        
	    except AssertionError, e:
	    	L.log(BROWSERS[x], "Test C - Functionality", "FAIL, PAGE DOES NOT HAVE A TITLE", d , exception=str(e))
	    	
	    else:
	    	if re.search("Page Not Found", title, re.I):
	    	    L.log(BROWSERS[x], "Test C - Functionality", "FAIL, 404 ERROR", title)
	    	    
	        elif re.search("Internal Server Error", title, re.I):
	            print "Failure, " + TEST
		    L.log(BROWSERS[x], "Test C - Functionality", "FAIL, 500 ERROR", title)
		    
	        else: 
		    L.log(BROWSERS[x], "Test C - Functionality", "PASS, PAGE LOADS OK", title)

	# 	Make sure all subfolders with an incorrect, bogus url return 404 errors ex: www.vulture.com/tv/1234trees/ 

	    sel.open(BASEURL + d + "abcd1234")
	    sel.wait_for_page_to_load("5000")
	    
	#	404 Verification / NO 500 Errors
	
	    try:
	        title = sel.get_title()
	        
	    except AssertionError, e:
	    	L.log(BROWSERS[x], "Test C - Functionality", "FAIL, PAGE DOES NOT HAVE A TITLE", d + "abcd")
	    	
	    if n < 9:
	    	if re.search("Page Not Found", title, re.I):
	    	    L.log(BROWSERS[x], "Test C - Functionality", "PASS, INTENTIONAL 404", d + "abcd")
	    	    
	        elif re.search("Internal Server Error", title, re.I):
		    L.log(BROWSERS[x], "Test C - Functionality", "FAIL, 500 ERROR, SHOULD BE 404", d + "abcd")
		    
	        else: 
		    L.log(BROWSERS[x], "Test C - Functionality", "FAIL, BUG", d + "abcd")

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