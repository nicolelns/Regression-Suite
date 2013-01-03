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
TEST = "Clickables Module - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.clickables()			# Call the relevant BeautifulSoup function (usually same name as test)

CSS = open('../data/text/clickables.css.txt', 'r').readlines()		# a = presence; Is it there?
DATA = pickle.load(open('../data/pickle/clickables.data.p', 'rb')) 	# c = function; Does the module work?
      
keys = DATA.keys()
values = DATA.values()
      
x = 0

"""This is a regression test for the Clickables module on Vulture's home page"""
""" Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  The DATA file contains this data"""
"""IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!"""	

#########################################################################
#########################################################################
	

class Clickables(unittest.TestCase):

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
    	    
        """
        Tests for the correct content within the module using data from the pickled data file, DATA
        This is a 'verify' test, it will not fail the whole test if one item fails
        """
    	    
        n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        """
        1. Gets the link text for each link
        2. Opens each page directly in the browser (as opposed to clicking on a link)
        3. Gets the page's title and checks that the link text is in the title (correct page loads)
        4. 
        """
        
	for each in keys:
	# Links is a list containing data for each entry in the clickables module
        	
            article = articles[n]	# Re-name variable
            
            m = 0
            a_list = []                 # Re-name, list isn't a good choice, either
            permalinks = []
            
            for each in article:
            # Contains data for the clickables entries
            	    
                datapoint = article[m]
                url = datapoint[0]
                data = datapoint[1]
                
                if len(article) > 1:
               
                    link1 = article[0]
                    link2 = article[1]
                	
                    a_list.append(link1)
                    permalinks.append(link2)
        
                try:
            	    if len(article) > 1:    
            	        text = sel.get_text("//a[@href='" + url + "']")
            	
                except AssertionError, e:
            	    L.log(BROWSERS[x], TEST, "FAIL, Cannot get link Text", url)
                    print "FAILURE, can't get link text " + url
                    self.verificationErrors.append(str(e))
                
            # Second, get the title and search the title for the link text
            	
                try:
            	    sel.open(url)
            	    sel.wait_for_page_to_load("50000")
            	    if len(article) > 1:
                        title = sel.get_title()
                
                except AssertionError, e:
            	    L.log(BROWSERS[x], TEST, "FAIL, Cannot open page and get title", url)
                    print "FAILURE, can't open page and get title " + url
                    self.verificationErrors.append(str(e))
                
                else:
            	    L.log(BROWSERS[x], TEST, "PASS, page opens and title has been acquired", url)
            	
            	    if len(article) > 1:
                        if re.search(text, title, re.I):
                            L.log(BROWSERS[x], TEST, "PASS, Correct page loads", url)
                        
                        elif re.search("not found", title, re.I):
                            L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", url)
                    	
                        else:
                    	    print "Test has a bug / exception", url, title, text
               
                    
                    sel.go_back()
                    sel.wait_for_page_to_load("50000")
            
                    m += 1
            
                n += 1
                   
            if len(a_list) != len(permalinks):
            	L.log(BROWSERS[x], TEST, "FAIL, MISMATCHED LINKS", url)
            else:
                L.log(BROWSERS[x], TEST, "PASS, Clickables article has permalink and regular link", url)
                if (len(a_list) > 23 or len(a_list) < 7):
                    L.log(BROWSERS[x], TEST, "FAIL, TOO MANY/TOO FEW ARTICLES IN CLICKABLES", str(len(a_list)) + " articles")
        

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
        
        for n in range(0,8):
        	
            article = articles[n]
            datapoint = article[m]
            d = datapoint[0]
            c = datapoint[1]
            print d
            print c
        	
            try:
                sel.click("//a[@href='" + d + "']")
                sel.wait_for_page_to_load("50000")
                
	    except Exception, e:
		print "FAILURE " + d, " does not load"
		L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + d)
		
	    else:
	    	L.log(BROWSERS[x], TEST, "PASS, Page loads", d)
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

    suite = unittest.TestLoader().loadTestsFromTestCase(Clickables)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
