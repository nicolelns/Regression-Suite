#! /usr/bin/python

import unittest
import time, datetime
import re
import pickle
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox', 'safari')
TEST = "Masthead Module (Links to Editorial Biographies) - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.masthead()

CSS = open('../data/text/masthead.css.txt', 'r').readlines()		# a = presence; Is it there?
DATA = pickle.load(open('../data/pickle/masthead.data.p', 'rb')) 	# c = function; Does the module work?

x = 0

"""This is a regression test for the Masthead module on Vulture's home page - links to the editors' biographies"""
""" Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  The DATA file contains this data"""
"""IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!"""	

#########################################################################
#########################################################################
	

class MastHead(unittest.TestCase):

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
	    
    def test_bc(self):
    	    
    # Tests for the correct content and tests for functionality within the module
    # This is a 'verify' test, it will not fail the whole test if one item fails
    	
    # Makes sure the correct number of links are in the Editorial Masthead	
    # Tests for the module's functionality
    # Clicks on each link based on its link text
    # Makes sure the page loads
    	
    	n = 0 
        sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        # First, make sure each link can be clicked on and that the page loads
        
        for each in DATA:
        	
            d = DATA[n]
            print d
        	
            try:
                sel.click("//a[@href='" + d)
                sel.wait_for_page_to_load("50000")
                
	    except Exception, e:
		print "FAILURE " + d, " does not load"
		L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + d)
		
	    else:
	    	L.log(BROWSERS[x], TEST, "PASS, Page loads", d)
		
	    try:
	    	title = sel.get_title()
	
            except AssertionError, e:
            	L.log(BROWSERS[x], TEST, "FAIL, Cannot open page and get title", d)
                print "FAILURE, can't open page and get title " + d
                self.verificationErrors.append(str(e))
                
            else:
            	L.log(BROWSERS[x], TEST, "PASS, page opens and title has been acquired", d)
            	
                if re.search(d, title, re.I):
                    L.log(BROWSERS[x], TEST, "PASS, Correct page loads", d)
                        
                elif re.search("not found", title, re.I):
                    L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", d)
                    	
                else:
                    print "Test has a bug / exception", d
		
                sel.go_back()
	        sel.wait_for_page_to_load("500000")
            
            n += 1
            
        count_links = sel.get_css_count("css=" + CSS[4])
        count_entries = sel.get_css_count("css=" + CSS[5])
        
        if count_links != 10:
            print "Missing links in Editorial/Masthead", str(count_links) + " links found"
        if count_entries != 10:
            print "Missing entries in Editorial/Masthead", str(count_entries) + " entries found"
        if count_links != count_entries:
            print "Mismatched Data in Editorial/Masthead"
            
        ########################################################################    	    

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(MastHead)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
