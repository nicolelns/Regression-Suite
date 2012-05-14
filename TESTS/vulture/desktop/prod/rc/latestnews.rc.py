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
TEST = "Latest News Module - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.latestnews()			

CSS = open('../data/text/latestnews.css.txt', 'r').readlines()		
DATA = pickle.load(open('../data/pickle/latestnews.data.p', 'rb')) 	        
      
x = 0

"""
This is a regression test for the Latest News module on Vulture's home page

"""

#########################################################################
#########################################################################
	
	
class LatestNews(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
    
    def test_latestnews(self):

    # Tests for the presence of elements in the module using CSS locators
    # This test is an 'assert' test: if any element is not present, the test fails
	
	n = 0
	sel = self.selenium
        sel.open(BASEURL)
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
            
        self.b_content_test()
        self.c_click_test()
            
        ######################################################################## 
            	
    def b_content_test(self):
    	
    	n = 0
	sel = self.selenium
	test = "Test B - Number of Links in Latest News"
	print test
        
        count = sel.get_css_count("css=" + CSS[2])
        
        if count != 6:
            self.verificationErrors.append("Incorrect number of articles! " + str(coount))
            print count, " articles, should be 6."
            L.log(BROWSERS[x], test, "FAIL, INCORRECT NUMBER OF ARTICLES: ", str(count) + " articles")
            	
        ########################################################################
            
    def c_click_test(self):
    	    
    # Tests for the module's functionality
    # Clicks on each link based on its address (href attribute)
    # Makes sure the page loads
    	
    	n = 0 
        sel = self.selenium
        test = "Test C - Click and Wait for Page to Load"
        print test
        
        # First, make sure each link can be clicked on and that the page loads
        
        for each in DATA:

	    d = DATA[n] 
        
            try:
            	text = sel.get_text("//a[@href='" + d + "']")
            	
            except AssertionError, e:
            	L.log(BROWSERS[x], test, "FAIL, CANNOT GET LINK TEXT", d, exception=str(e))
                print "FAILURE, can't get link text " + d
                self.verificationErrors.append(str(e) + d + " can't get link text")
                
            # Second, get the title and search the title for the link text
            	
            try:
            	sel.click("//a[@href='" + d + "']")
            	sel.wait_for_page_to_load("50000")
                title = sel.get_title()
                
            except AssertionError, e:
            	L.log(BROWSERS[x], test, "FAIL, CANNOT OPEN PAGE/GET TITLE", d, exception=str(e))
                print "FAILURE, can't open page and get title " + d
                self.verificationErrors.append(str(e) + d + " can't get title")
                
            else:
            	L.log(BROWSERS[x], test, "PASS, GOT TITLE, PAGE OPENS", d)
            	
                if re.search(text, title, re.I):
                    L.log(BROWSERS[x], test, "PASS, Correct page loads", d)
                        
                elif re.search("not found", title, re.I):
                    L.log(BROWSERS[x], test, "FAIL, PAGE DOES NOT LOAD", d)
                    print "Failure, page does not load " + title + ": Title for page " + d
                    	
                else:
                    print "Test has a bug / exception - visually verify"
                    print "Title: " + title, " Text: " + text, "Page: " + d
                    
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

    suite = unittest.TestLoader().loadTestsFromTestCase(LatestNews)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()