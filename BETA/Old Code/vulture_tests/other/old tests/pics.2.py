#! /usr/bin/python

import unittest
import time, datetime
import re
import pickle
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "Pics Module"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.pics()

CSS = open('../data/vulture.home.pics.css.txt', 'r').readlines()
DATA = pickle.load(open('../data/vulture.home.pics.data.p', 'rb'))

x = 0

"""This is a regression test for the Pics module on Vulture's home page"""
""" Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  The DATA file contains this data"""
"""IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!"""	

#########################################################################
#########################################################################
	

class Pics(unittest.TestCase):

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
	    
    def test_content(self):
    	    
    # Tests for the correct content within the module
    	    
    	pass

    ########################################################################    	    
            
    def test_c(self):
    	    
    # Tests for the module's functionality
    # Clicks on each link based on its address (href attribute)
    # Makes sure the page loads
    	
    	n = 0 
        sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        links = DATA.values()
        abc = links[0]
        print abc
        
        # First, make sure each link can be clicked on and that the page loads
        
        for each in abc:
        
            article = abc[n]
            
            m = 0
            
            for each in article:
            	    
            	datapoint = article[m]
                url = datapoint[0]
                data = datapoint[1]
        	
                try:
                    sel.click("//a[@href='" + url + "']")
                    sel.wait_for_page_to_load("50000")
                
	        except Exception, e:
		    print "FAILURE " + url, " link does not load " + str(e)
		    L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + url)
		
	        else:
	    	    print "PASS"
	    	    L.log(BROWSERS[x], TEST, "PASS, Page loads", url)
		    sel.go_back()
	            sel.wait_for_page_to_load("50000")
	        
	        if (data is not None) and (data != "*") and (data != "See All"):
	    	
	    	    try:
                        sel.click("//img[@src='" + data + "']")
                        sel.wait_for_page_to_load("50000")
                
	            except Exception, e:
		        print "FAILURE " + data, " image does not load"
		        L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + data)
		 
                    else:
                        print "PASS IMAGE"
	    	        L.log(BROWSERS[x], TEST, "PASS, Page loads", data)
		        sel.go_back()
	                sel.wait_for_page_to_load("50000")
	    
	        m += 0
	    
            n += 1
            print n

        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(Pics)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()