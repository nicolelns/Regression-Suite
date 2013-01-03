#! /usr/bin/python

import unittest
import time, datetime
import re
import pickle
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

#Huffpost 75%, Moviefone 25%

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox', 'safari')
TEST = "Partners Module - Desktop - Vulture Home Page"
      
L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.partners()

CSS = open('../data/text/partners.css.txt', 'r').readlines()		# a = presence; Is it there?
DATA = pickle.load(open('../data/pickle/partners.data.p', 'rb')) 	# c = function; Does the module work?

keys = DATA.keys()
links = DATA.values()

x = 0

"""This is a regression test for the Partners module on Vulture's home page"""
""" Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  The DATA file contains this data"""
"""IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!"""	

#########################################################################
#########################################################################


class Partners(unittest.TestCase):

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
    	    
    # Tests for the correct content within the module
    # This is a 'verify' test, it will not fail the whole test if one item fails
    
    	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        wonder = sel.get_css_count("css=" + CSS[4])
        holly = sel.get_css_count("css=" + CSS[7])
        buzz = sel.get_css_count("css=" + CSS[13])
        
        try:
            huff = sel.get_css_count("css=" + CSS[10]) #Huffington Post
        except:
            huff = None
            fone = sel.get_css_count("css=" + CSS[16]) #Moviefone
        else:
            fone = None
            
        if (wonder != 5) or (holly != 5) or (buzz != 5) or ((huff != 5)  or (fone != 5)):
            #self.verificationErrors.append("Incorrect number of articles!")	
            L.log(BASEURL[x], TEST, "Incorrect number of articles", "")	
	    print "Incorrect number of articles"
	    print str(wonder), "wonder"
	    print str(holly), "holly"
	    print str(huff), "huff"
	    print str(buzz), "buzz"
	    print str(fone), "fone"
	    
        ########################################################################

    def test_c(self):
    	    
    # Tests for the module's functionality
    # Clicks on each link based on its address (href attribute)
    # Makes sure the page loads
    	
    	n = 0 
        sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        # First, make sure each link can be clicked on and that the page loads
        
        for each in links:
        	
            partners = links[n]
            m = 0
            
            for each in partners:
            	    
            	data = partners[m]
                d = data[0]
                c = data[1]
        	
                try:
                    sel.click("//a[@href='" + d + "']")
                    sel.wait_for_page_to_load("50000")
                
	        except AssertionError, e:
		    print "FAILURE " + d, " does not load"
		    L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + d)
		
	        else:
	    	    L.log(BROWSERS[x], TEST, "PASS, Page loads", d)
		    sel.go_back()
	            sel.wait_for_page_to_load("50000")
	            
	        if c is not None:
	    
                    try:
                        sel.click("//img[@src='" + c + "']")
                        sel.wait_for_page_to_load("50000")
                
	            except AssertionError, e:
		        print "FAILURE " + c, " does not load", str(e)
		        L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + c)
		
	            else:
	    	        L.log(BROWSERS[x], TEST, "PASS, Page loads", c)
		        sel.go_back()
	                sel.wait_for_page_to_load("50000")
	    
                m += 1
            n += 1

        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(Partners)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
