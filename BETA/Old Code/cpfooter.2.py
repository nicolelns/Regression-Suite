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
TEST = "Copyright Footer Section Test (General Promo) - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.cpfooter()

CSS = open('../data/text/cpfooter.css.txt', 'r').readlines()		
DATA = pickle.load(open('../data/pickle/cpfooter.data.p', 'rb')) 
CONTENT = "2010 2011, New York Media LLC. All Rights Reserved."

x = 0

"""This is a regression test for the Copyright Footer section on Vulture's home page"""
""" Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements (via XPATH locators in the CONTENT file) contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  The DATA file contains this data"""
"""IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!"""	

#########################################################################
#########################################################################
	

class CpFooter(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
	
	########################################################################
    
    def test_cp_footer(self):

    # Tests for the presence of elements in the module using CSS locators
    # This test is an 'assert' test: if any element is not present, the test fails
	
	n = 0
	sel = self.selenium
        sel.open(BASEURL)
        sel.wait_for_page_to_load("50000")
        test = "Test A - Presence of Elements"
        print test
        
        # Loops through the data in the CSS file asserting each element is on the page
        
	for each in CSS:

	    c = CSS[n].strip('\n') 
        
            try:
                self.failUnless(sel.is_element_present("css=" + c))
                
            except AssertionError, e:
            	print "FAILURE, ELEMENT NOT FOUND" + c
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], test, "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            
            else:
                L.log(BROWSERS[x], test, "PASS, ELEMENT FOUND", c)
                
            n += 1
            
        self.b_title_test()    
        self.c_link_count()
        self.d_clicky_test()
        
        ########################################################################
	    
    def b_title_test(self):
    	    
    # Tests for the correct content within the module
    # This is a 'verify' test, it will not fail the whole test if one item fails
    	
        n = 0
	sel = self.selenium
	test = "Test B - Do the Links Open the Right Pages?"
	print test
        
        # Gets the link text for each link in DATA
        # Opens each page directly in the browser
        # Gets the page's title and checks that the link text is in the title (correct page loads)
        # Verifies that the copyright text is on the page
        
	for each in DATA:

	    d = DATA[n] 
        
            try:
            	text = sel.get_text("//a[@href='" + d + "']")
            	
            except AssertionError, e:
            	L.log(BROWSERS[x], test, "FAIL, CANNOT GET LINK TEXT", d, exception=str(e))
                print "FAILURE, CAN'T GET LINK TEXT " + d
                self.verificationErrors.append(str(e))
                
            # Second, get the title and search the title for the link text
            	
            try:
            	sel.open(d)
            	sel.wait_for_page_to_load("50000")
                title = sel.get_title()
                
            except AssertionError, e:
            	L.log(BROWSERS[x], test, "FAIL, CANNOT OPEN PAGE AND GET TITLE", d, exception=str(e))
                print "FAILURE, CAN'T OPEN PAGE AND GET TITLE " + d
                self.verificationErrors.append(str(e))
                
            else:
            	L.log(BROWSERS[x], test, "PASS, PAGE OPENS, TITLE ACQUIRED", d)
            	
                if re.search(text, title, re.I):
                    L.log(BROWSERS[x], test, "PASS, CORRECT PAGE LOADS", d)
                        
                elif re.search("not found", title, re.I):
                    L.log(BROWSERS[x], test, "FAIL, 404 ERROR", d)
                    	
                else:
                    print "Test has a bug / exception", d
                    
                sel.go_back()
                sel.wait_for_page_to_load("50000")
                 
            n += 1   
            
        ########################################################################    
            
    def c_link_count(self):
    	    
    	sel = self.selenium
    	test = "Test C - Counting Links in Footer, Verifying Copyright Statement"
    	print test
            
        count = sel.get_css_count("css=" + CSS[2])
        
        if count != 11:
            L.log(BROWSERS[x], test, "FAIL, MISSING LINKS IN COPYRIGHT FOOTER", str(count) + " links found")
            print "LINKS MISSING FROM FOOTER"
            
        # Make sure the copyright statement is on the page
            	
        if sel.is_text_present(CONTENT):
            L.log(BROWSERS[x], test, "PASS, COPYRIGHT STATEMENT IS PRESENT", CONTENT)
           
        else:
            L.log(BROWSERS[x], test, "FAIL, TEXT NOT PRESENT", CONTENT)
            print "COPYRIGHT STATEMENT NOT PRESENT" 	
            
        ########################################################################

    def d_clicky_test(self):
    	    
    # Tests for the module's functionality
    # Clicks on each link based on its address (href attribute)
    # Makes sure the page loads
    	
    	n = 0 
        sel = self.selenium
        test = "Test D - Functionality, Can Links Be Clicked On?"
        
        # First, make sure each link can be clicked on and that the page loads
        
        for each in DATA:
        	
            d = DATA[n]
        	
            try:
                sel.click("//a[@href='" + d + "']")
                sel.wait_for_page_to_load("50000")
                
	    except Exception, e:
		print "FAILURE " + d, " DOES NOT LOAD"
		L.log(BROWSERS[x], test, "FAIL, PAGE DOES NOT LOAD", d, exception=str(e))
		
	    else:
	    	L.log(BROWSERS[x], test, "PASS, PAGE LOADS", d)
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

    suite = unittest.TestLoader().loadTestsFromTestCase(CpFooter)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
    
