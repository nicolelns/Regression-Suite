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
TEST = "Big Interview Module - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.biginterview()		# Call the relevant BeautifulSoup function (usually same name as test)

CSS = open('../data/text/biginterview.css.txt', 'r').readlines()		
DATA = pickle.load(open('../data/pickle/biginterview.data.p', 'rb')) 	        

links = DATA[0]
images = DATA[1]

x = 0

"""This is a regression test for the Big Interview module on Vulture's home page"""
""" Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  The DATA file contains this data"""
"""IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!"""	

#########################################################################
#########################################################################
	

class BigInterview(unittest.TestCase):

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
	    
    def test_b(self):
   
    	m = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        """
        Gets the link text for each link in DATA
        Opens each page directly in the browser
        Gets the page's title and checks that the link text is in the title (correct page loads)
        Verifies that the copyright text is on the page
        """
        
	for each in links:
	    
            href = links[m]
            
            try:
            	text = sel.get_text("//a[@href='" + href + "']")
            	
            except AssertionError, e:
            	L.log(BROWSERS[x], TEST, "FAIL, Cannot get link Text", href)
                print "FAILURE, can't get link text " + href
                self.verificationErrors.append(str(e))
                
            try:
            	sel.open(href)
            	sel.wait_for_page_to_load("50000")
                title = sel.get_title()
                
            except AssertionError, e:
            	L.log(BROWSERS[x], TEST, "FAIL, Cannot open page and get title", href)
                print "FAILURE, can't open page and get title " + href
                self.verificationErrors.append(str(e))
                
            else:
            	L.log(BROWSERS[x], TEST, "PASS, page opens and title has been acquired", href)
            	
                if re.search("not found", title, re.I):
                    L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", href)
                    	
                else:
                    L.log(BROWSERS[x], TEST, "PASS, Page loads ok", href)
                    
                sel.go_back()
                sel.wait_for_page_to_load("50000")
            
            m += 1      
            
        ########################################################################

    def test_c(self):
    	    
    # Tests for the module's functionality
    # Clicks on each link based on its address (href attribute)
    # Makes sure the page loads
    	
    	m = n = 0 
        sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        # First, make sure each link can be clicked on and that the page loads
        
        for each in links:
	    
            href = links[m]
        	
            try:
                sel.click("//a[@href='" + href + "']")
                sel.wait_for_page_to_load("50000")
                
	    except Exception, e:
		print "FAILURE " + href, " does not load"
		L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + href)
		
	    else:
	    	L.log(BROWSERS[x], TEST, "PASS, Page loads", href)
		sel.go_back()
	        sel.wait_for_page_to_load("50000")
	        
	    m += 1
	    
        for each in images:
        	
            img = images[n]
        	
            try:
                sel.click("//img[@src='" + img + "']")
                sel.wait_for_page_to_load("50000")
                
	    except Exception, e:
	        print "FAILURE " + img, " does not load"
		L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + img)
		
	    else:
	    	L.log(BROWSERS[x], TEST, "PASS, Page loads", img)
		sel.go_back()
	        sel.wait_for_page_to_load("50000")
	    
            n += 1

        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(BigInterview)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()