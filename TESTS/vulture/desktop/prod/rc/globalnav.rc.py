#! /usr/bin/python
# -*- coding: latin-1 -*-

import unittest
import time, datetime
import re
import pickle
#import Logger			
import vultureSoup		
from selenium import selenium    

BASEURL = raw_input("Please enter a BaseURL: ")
BROWSERS = ('chrome', 'firefox', 'safari')
TEST = "Global Navigation (Music, Movies, TV, etc) - Desktop - Vulture Home Page"

#L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser(BASEURL)

CSS = open('../data/text/globalnav.css.txt', 'r').readlines()		
DATA = S.globalnav()	#List

x = 0

"""
This is a regression test for the global Nav bar on Vulture's home page
This test should NOT be confused with the site-wide global navigation bar - this tests the Global Vulture
navigation - i.e. the music, tv, movies, etc, menus

"""
#########################################################################
#########################################################################
	

class GlobalNav(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
    
    def test_global_nav(self):

	"""
        Preliminary test for the presence of various elements in the Vulture Global Navigation bar.
        CSS selectors are in a .txt file, and this test makes sure each element exists on the page before proceeding.
        Failures will fail the whole test.  (No point in continuing if links aren't present, right?).
        The other tests are called from this function to avoid repetitive and unnecessary SetUp and TearDown of the browser.
        In addition, the other tests can be commented out and not run - easy to select which tests run.  None are dependent on 
        results from other tests.  Only test_biginterview needs to be run for the sub-tests to run (unless you comment them out)
        
        PASSING CONDITIONS:  All elements are present on the page.
        FAILING CONDITIONS:  Any ONE element is not present on the page.
        
        """
	
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
            	print "FAILURE to find CSS" + c, str(e)
            	self.verificationErrors.append("CSS ERROR TEST A")
                #L.log(BROWSERS[x], test, "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            
            #else:
                #L.log(BROWSERS[x], test, "PASS, ELEMENT FOUND", c)
                
            n += 1
            
        self.b_link_test()
            
        ########################################################################
	    
    def b_link_test(self):
    	    
    	"""  
    	Each page is clicked on to ensure that the link works.
    	The title of the opened page is acquired and passed to the title test function
    	
    	PASSING CONDITIONS:  Each link can be clicked on
    			     Each page loads and has a title
    			     
    	FAILING CONDITIONS:  Links cannot be clicked on
    			     Pages do not load or have no title
    			     
    	
    	"""
    	
        n = 0	
	sel = self.selenium
	test = "Test B - Do the Links Open the Right Pages?"
	print test
        
	for each in DATA:
	
            d = DATA[n]
            
            try:
            	sel.click("//a[@href='" + d + "']")
            	sel.wait_for_page_to_load("50000")
                
            except Exception, e:
                print "FAILURE, CAN'T OPEN PAGE " + d, "Error: " + str(e)
                self.verificationErrors.append("LINK ERROR TEST B")
            
            try:
            	title = sel.get_title()
            	
            except Exception, e:
            	print "FAILURE, CAN'T GET TITLE" + d, "Error: " + str(e)
            	self.verificationErrors.append("TITLE ERROR TEST B")
            	
            self.c_title_test(title)
            self.back()	
            n += 1    
            
        ########################################################################
        
    def c_title_test(self, title):
    	    
    	self.title = title
    	sel = self.selenium
    	test = "Test C - No Errors (404, 500, etc.) in Titles"
    	print test
    	
    	try:
    	    self.assertNotEqual(len(title), 0)
    	    self.assertFalse(re.search("404", title))
    	    self.assertFalse(re.search("500", title))
    	    self.assertFalse(re.search("not found", title, re.I))
    	    self.assertFalse(re.search("internal server error", title, re.I))
    	    
        except AssertionError, e:
            self.verificationErrors.append("TITLE ERROR TEST C")
            print "FAILURE, INCORRECT TITLE" + title, "Error: " + str(e)
            
        return
    	
    	########################################################################
    
    def d_hover_test(self):
    	    
    	"""
    	This test will test the "etc" section of the vulture "global nav"
    	
    	"""
    	
    	pass

	########################################################################
	
    def back(self):
    	    
    	sel = self.selenium
    	sel.go_back()
    	sel.wait_for_page_to_load("50000")

        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(GlobalNav)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
    

