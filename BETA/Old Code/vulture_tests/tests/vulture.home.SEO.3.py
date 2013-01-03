#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "Basic SEO Test"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.SEO()			       # Call the relevant BeautifulSoup function (usually same name as test)

CONTENT = open('../data/vulture.home.SEO.content.txt', 'r').readlines()
DATA = open('../data/vulture.home.SEO.data.txt', 'r').readlines()               # Link data - exception to normal DATA files - contains pages to test.

L = Logger.MainLogger(BASEURL, TEST)
      
x = 0

"""This is a regression test for SEO data for Vulture's pages"""
"""No test 'a'.  This is a test to make sure each page has SEO content, no elements are present, otherwise.
Test 'b' is a 'content' test:  Do the pages (from BeauvultifulSoup in the CONTENT file) contain the relevant data?
No test 'c'.  DATA file contains a list of links to run tests 'a' and 'b' against.  This is an exception to normal DATA files, which contain data for functional testing"""
"""IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!"""	

#########################################################################
#########################################################################
	

class SEO(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
	
	########################################################################
	    
    def test_b(self):
    	    
    	# Tests to see that SEO tags contain content (tags are non-empty)
    	
    	n = 0
    	sel = self.selenium
        sel.open("/")
	sel.wait_for_page_to_load("5000")
	
    	for each in DATA:
    		
    	    d = DATA[n].strip('\n')
    	    
    	    # The DATA file is organized as follows:
    	    # The BeautifulSoup parser finds all keywords and descriptions for all the pages in DATA and writes them to the CONTENT file
    	    # The parser writes 2 lines per page, keywords first, then description
    	    # keywords = n is 0 or even  
    	    # description = n is odd
    	    # Hence, n/2 % 1 (aka n/2 remainder 1, definition of even/odd numbers)
    	    
    	    sel.open(d)
    	    sel.wait_for_page_to_load("50000")
    	    
    	    #    Title
    	    
    	    title = sel.get_title()
    	    
    	    if len(title) > 0:
                L.log(BROWSERS[x], TEST, "PASS", BASEURL + " PAGE HAS TITLE", title)
            
            else:
                self.verificationErrors.append(title)
                L.log(BROWSERS[x], TEST, "FAIL", BASEURL + " TITLE TAG HAS NO CONTENTS", title)
                
            #    Description
                
            if n/2 % 1:
    	    	description = CONTENT[n].strip('\n')
    	    
    	        if len(description) > 0:
                    L.log(BROWSERS[x], TEST, "PASS", BASEURL + " PAGE HAS DESCRIPTION", description)
            
                else:
                    self.verificationErrors.append(description)
                    L.log(BROWSERS[x], TEST, "FAIL", BASEURL + " DESCRIPTION ATTR HAS NO CONTENTS", description)

            #    Keywords
           
            else:
            	keywords = CONTENT[n].strip('\n')
                
                if len(keywords) > 0:
                    L.log(BROWSERS[x], TEST, "PASS", BASEURL + " PAGE HAS KEYWORDS", keywords)
            
                else:
                    self.verificationErrors.append(keywords)
                    L.log(BROWSERS[x], TEST, "FAIL", BASEURL + " KEYWORD ATTR HAS NO CONTENTS", keywords)
            
        ########################################################################

            n += 1

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(SEO)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()