#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "Latest Talk Module"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.latesttalk()

CSS = open('../data/vulture.home.latesttalk.css.txt', 'r').readlines()        
DATA = open('../data/vulture.home.latesttalk.data.txt', 'r').readlines()           

x = 0

"""This is a regression test for the Latest Talk module on Vulture's home page"""
""" Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  The DATA file contains this data"""
"""IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!"""	

#########################################################################
#########################################################################
	

class LatestTalk(unittest.TestCase):

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
    	    
        comments = "html.js body#nymag.vulture div#wrap-wrap div#wrap div#content div#content-secondary div.parsys div.parbase section.vulture-talk article.entry footer a.comments span.comment-tout span a.extra strong.article_comment_count"    

    	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        # Tests the Latest Talk Module for content
        
	for each in DATA:

	    d = DATA[n].strip('\n') 
        
            try:
            	text = sel.get_text("//a[@href='" + d + "']")
            	
            except AssertionError, e:
            	L.log(BROWSERS[x], TEST, "FAIL, Cannot get link Text", d)
                print "FAILURE, can't get link text " + d
                self.verificationErrors.append(str(e))
                
            # Second, get the title and search the title for the link text
            	
            try:
            	sel.open(d)
            	sel.wait_for_page_to_load("50000")
                title = sel.get_title()
                
            except AssertionError, e:
            	L.log(BROWSERS[x], TEST, "FAIL, Cannot open page and get title", d)
                print "FAILURE, can't open page and get title " + d
                self.verificationErrors.append(str(e))
                
            else:
            	L.log(BROWSERS[x], TEST, "PASS, page opens and title has been acquired", d)
            	
                if re.search(text, title, re.I):
                    L.log(BROWSERS[x], TEST, "PASS, Correct page loads", d)
                        
                elif re.search("not found", title, re.I):
                    L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", d)
                    	
                else:
                    print "Test has a bug / exception", d
                    
                sel.go_back()
                sel.wait_for_page_to_load("50000")
                 
            n += 1 
                
        counts = (CSS[2], CSS[3], CSS[4], CSS[5])
        i = 0
        
        for each in counts:
        	
            count = sel.get_css_count("css=" + counts[i]) 	
        	
            if count != 2:
            	print count, " elements found, missing links, headers, etc"
            	L.log(BROWSERS[x], TEST, "FAIL, Missing Links", str(count) + " links found")
                self.verificationErrors.append("Failure, incorrect number of articles in Latest Talk")
            
            i += 1
            	    
            
        ########################################################################

    def test_function(self):
    	    
    # Tests for the module's functionality
    	    
    	pass

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(LatestTalk)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()