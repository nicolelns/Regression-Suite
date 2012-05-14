#! /usr/bin/python
# -*- coding: latin-1 -*-

import unittest
import time, datetime
import re
import pickle
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox', 'safari')
TEST = "Global Navigation (Music, Movies, TV, etc) - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.globalnav()

CSS = open('../data/text/globalnav.css.txt', 'r').readlines()		# a = presence; Is it there?
DATA = pickle.load(open('../data/pickle/globalnav.data.p', 'rb')) 	# c = function; Does the module work?

x = 0

"""
This is a regression test for the global Nav bar on Vulture's home page
This test should NOT be confused with the site-wide global navigation bar - this tests the Global Vulture
navigation - i.e. the music, tv, movies, etc, menus

IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!	

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
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], test, "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            
            else:
                L.log(BROWSERS[x], test, "PASS, ELEMENT FOUND", c)
                
            n += 1
            
        self.b_title_test()
            
        ########################################################################
	    
    def b_title_test(self):
    	    
    	"""
    	This test grabs the link text (text between <a></a> tags) for each link.  
    	Each page is clicked on to ensure that the link works.
    	The title of the opened page is acquired.
    	The title is searched for "not found", "404", etc to verify page load
    	
    	PASSING CONDITIONS:  Each link has text associated with it
    			     Each link can be clicked on
    			     Each page loads and has a title
    			     
    	FAILING CONDITIONS:  Links have no text for the user to see/click on aka headline does not show
    			     Links cannot be clicked on
    			     Pages do not load or have "not found" in the title
    			     
    	
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
            	title = sel.get_title()
                
            except AssertionError, e:
            	L.log(BROWSERS[x], test, "FAIL, CANNOT OPEN PAGE AND GET TITLE", d, exception=str(e))
                print "FAILURE, CAN'T OPEN PAGE AND GET TITLE " + d, "Error: " + str(e)
                self.verificationErrors.append(str(e))
                
            else:
            	L.log(BROWSERS[x], test, "PASS, PAGE OPENS", d)
            	
                if (re.search("not found", title, re.I) or re.search("internal server error", title)):
                    L.log(BROWSERS[x], test, "FAIL, 404/500 ERROR", d)
                    self.verificationErrors.append("404 Error" + d)
                    
                else:
                    L.log(BROWSERS[x], test, "PASS, NO 404/500 ERROR", d)
                    
                sel.go_back()
                sel.wait_for_page_to_load("50000")
                 
            n += 1    
            
        ########################################################################
        
    def c_hover_test(self):
    	    
    	"""
    	This test will test the "etc" section of the vulture "global nav"
    	
    	"""
    	
    	pass

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(GlobalNav)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
    

