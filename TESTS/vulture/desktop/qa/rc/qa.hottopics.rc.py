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
TEST = "Hot Topics Module - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.hottopics()			# Call the relevant BeautifulSoup function (usually same name as test)

CSS = open('../data/text/hottopics.css.txt', 'r').readlines()		# a = presence; Is it there?
DATA = pickle.load(open('../data/pickle/hottopics.data.p', 'rb')) 	# c = function; Does the module work?

keys = DATA.keys()
values = DATA.values()

x = 0

"""
This is a regression test for the "Hot Topics" section of the Global Navigation bar on vulture's home page.

"""

#########################################################################
#########################################################################
	

class HotTopics(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
    
    def test_hottopics(self):

	n = 0
	sel = self.selenium
        sel.open(BASEURL)
        sel.wait_for_page_to_load("50000")
        test = "Test A - Presence of Elements via CSS"
        print test
        
        # Loops through the data in the CSS file asserting each element is on the page
        
	for each in CSS:

	    c = CSS[n].strip('\n') 
        
            try:
                self.failUnless(sel.is_element_present("css=" + c))
                
            except AssertionError, e:
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], test, "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            
            else:
                L.log(BROWSERS[x], test, "PASS, ELEMENT FOUND", c)
                
            n += 1
       
        self.b_content_test()
        self.c_click_test()
        
        ########################################################################
	    
    def b_content_test(self):
    	    
    # Makes sure exactly 5 links are in the Hot Topics section 
    	 
    	m = 0
	sel = self.selenium
	test = "Test B - Number of Links in Module"
	print test
           
        if len(keys) != 5:
            self.verificationErrors.append(len(keys) + " links")
            L.log(BROWSERS[x], test, "FAIL, WRONG NUMBER OF LINKS", str(len(keys)) + " links found")
            
        if sel.is_text_present('Hot Topics'):
            L.log(BROWSERS[x], test, "PASS, TEXT PRESENT", "Hot Topics")

        else:
            L.log(BROWSERS[x], test, "FAIL, TEXT NOT PRESENT", "Hot Topics")
        
        
        
        ########################################################################

    def c_click_test(self):
    	    
    # Can the link be clicked on and does the page load?  Is there an image silo for the first Hot Topics entry?
    
    	m = 0 
        sel = self.selenium
        test = "Test C - Click and Wait for Page to Load"
        print test
        
        # First, make sure each link can be clicked on and that the page loads
        
        for each in keys:
		
	    d = keys[m]
	    c = values[m]
	    
	    try:
                sel.click("//a[@href='" + d + "']")
                sel.wait_for_page_to_load("50000")
                
	    except Exception, e:
		print "FAILURE " + d, " does not load"
		L.log(BROWSERS[x], test, "FAIL, PAGE DOES NOT LOAD", d, exception=str(e))
		
	    else:
	    	L.log(BROWSERS[x], test, "PASS, PAGE LOADS", d)
		sel.go_back()
	        sel.wait_for_page_to_load("50000")
	        
	# Second, make sure each image can be clicked on and that the page loads
	
	    if c is not None:
	        try:
                    sel.click("//img[@src='" + c + "']")
                    sel.wait_for_page_to_load("50000")
                
	        except Exception, e:
		    print "FAILURE " + c, " does not load"
		    L.log(BROWSERS[x], test, "FAIL, IMAGE DOES NOT LOAD", c, exception=str(e))
		
	        else:
	            L.log(BROWSERS[x], test, "PASS, IMAGE LOADS", c)
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

    suite = unittest.TestLoader().loadTestsFromTestCase(HotTopics)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
