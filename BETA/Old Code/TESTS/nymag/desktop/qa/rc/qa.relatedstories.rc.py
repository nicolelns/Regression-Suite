#! /usr/bin/python

import unittest
import time, datetime
import re
import pickle
import Logger			# Logging module (for test results, outputs results to a .txt file)
import nymagSoup     		# BeautifulSoup page scraper collects relevant data from qa.nymetro
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://qa.nymetro.com/daily/intel/2012/04/test-for-eve-vl-191.html'
BROWSERS = 'safari' 
TEST = "Related Stories Module - QA - NYMag (SAFARI)"

L = Logger.MainLogger(BASEURL, TEST)

S = nymagSoup.Parser("http://qa.nymetro.com/daily/intel/2012/04/test-for-eve-vl-191.html")
S.relatedstories()

CSS = open('../data/text/qa.relatedstories.css.txt', 'r').readlines()
DATA = pickle.load(open('../data/pickle/qa.relatedstories.data.p', 'rb'))

keys = DATA.keys()
values = DATA.values()

x = 0

"""
This is a test for the Cut Celebrity Splash Pages:

Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  

The DATA file is a pickle file generated by vultureSoup.Parser(), customized for this module.

IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!
"""	

#########################################################################
#########################################################################
	

class RelatedStories(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS, BASEURL)
        self.selenium.start()
	print "TESTING qa.nymetro in " + BROWSERS
	
	########################################################################
    
    def test_a(self):

    # Tests for the presence of elements in the module using CSS locators
    # This test is an 'assert' test: if any element is not present, the test fails
	
	n = m = 0
	sel = self.selenium
        sel.open("http://qa.nymetro.com/daily/intel/2012/04/test-for-eve-vl-191.html")
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
            
        for each in keys:
    		
    	    url = keys[m]
    	    data = values[m]
    	    title = data[1]
    	    print url, title
    	    
    	    if not re.search('http://', url, re.I):
    	    	    
                if title is None:
    	    	
    	    	    print "no title with relative url, FAIL"
    	    	    
    	        else:
    	        	
    	            print "relative url with title, PASS"
    	    	
    	    else:
    	    	    
    	    	if title is None:
    	    		
    	    	    print "no title with full url, FAIL"
    	    	    
    	    	else:
    	        	
    	            print "full url with title, PASS"
    	            
    	    m += 1
       
        ########################################################################

    def test_c(self):
    	    
    # Tests for the module's functionality
    # Clicks on each link based on its address (href attribute)
    # Makes sure the page loads
    	
    	m = n = 0 
        sel = self.selenium
        sel.open("http://qa.nymetro.com/daily/intel/2012/04/test-for-eve-vl-191.html")
        sel.wait_for_page_to_load("50000")
        
        
        # First, make sure each link can be clicked on and that the page loads
        
        for each in keys:
		
	    d = keys[m]
	    data = values[m]
	    c = data[1]
	    
	    try:
                sel.click("//a[@href='" + d + "']")
                sel.wait_for_page_to_load("50000")
                
	    except Exception, e:
		print "FAILURE " + d, " does not load"
		L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + " " + d)
		
	    else:
	    	L.log(BROWSERS[x], TEST, "PASS, Page loads", d)
		sel.go_back()
	        sel.wait_for_page_to_load("50000")
	        
	# Second, make sure each image can be clicked on and that the page loads           
	    if c is not None:
	        try:
                    sel.click("//img[@src='" + c + "']")
                    sel.wait_for_page_to_load("50000")
                
	        except Exception, e:
		    print "FAILURE " + c, " does not load"
		    L.log(BROWSERS[x], TEST, "FAIL, IMAGE DOES NOT LOAD", str(e) + c)
		
	        else:
	            L.log(BROWSERS[x], TEST, "PASS, Page loads", c)
		    sel.go_back()
	            sel.wait_for_page_to_load("50000")
	            
	    m += 1

        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(RelatedStories)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
