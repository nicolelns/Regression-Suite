#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "Viral Video Module on Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.viralvideo()			# Call the relevant BeautifulSoup function (usually same name as test)

CSS = open('../data/vulture.home.viralvideo.css.txt', 'r').readlines()		# a = presence; Is it there?
CONTENT = open('../data/vulture.home.viralvideo.content.txt', 'r').readlines()  # b = content; Does the module have the right stuff?
DATA = open('../data/vulture.home.viralvideo.data.txt', 'r').readlines()  	# c = function; Does the module work?
      
x = 0

"""This is a regression test for the Viral Video module on Vulture's home page"""
""" Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  The DATA file contains this data"""
"""IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!"""	

#########################################################################
#########################################################################	

class ViralVideos(unittest.TestCase):
    
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
    
        comments = "html.js body#nymag.vulture div#wrap-wrap div#wrap div#content div#content-primary div#features-wrap div.parsys div.vulturevideos section#feature-video.feature-video div.carousel ul li article.entry header h3 span.comment-tout span a.extra strong.article_comment_count"
    	    
    	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        # Gets the link text for each link in DATA
        # Opens each page directly in the browser
        # Gets the page's title and checks that the link text is in the title (correct page loads)
        # Verifies that the copyright text is on the page
        
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
            
        # Count number of headings, articles, etc. by CSS selector and make sure all values are equal    
                   
        counts = (CSS[5], CSS[6], CSS[7])
        i = 0
        
        for each in counts:
            	    
            count = sel.get_css_count("css=" + counts[i])
            
            if i == 0: 
            	count = count/2                  # Should be 6
            elif i == 1: 
            	count = count/4                # Should be 6
            elif i == 2: 
            	count = count/2                # Should be 6
            
            if (count != 6):
                print "MISSING ELEMENTS!"
                print count, " count", i
                L.log(BROWSERS[x], TEST, "FAIL, Missing Viral Video Links", str(count) + " links found")
                	
            i += 1
                
            if S.viralvideo() != (count,count):                                #S.tvrecap(x,y), where x = number of links to individual articles and y = number of links to articles WITH an image, these values (integers) should be equal
                print "MISMATCHED ARTICLES", S.viralvideo()
	  
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
        
        for each in DATA:
        	
            d = DATA[n].strip('\n')
            
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
            
        m = 0
            
        for each in CONTENT:
        	
            c = CONTENT[m].strip('\n')
            
            try:
            	sel.click("//img[@src='" + c + "']")
                sel.wait_for_page_to_load("50000")
                
            except Exception, e:
		print "FAILURE " + c, " does not load"
		L.log(BROWSERS[x], TEST, "FAIL, IMAGE DOES NOT LOAD", str(e) + c)
		
	    else:
	    	L.log(BROWSERS[x], TEST, "PASS, Image loads", c)
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

    suite = unittest.TestLoader().loadTestsFromTestCase(ViralVideos)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.Save()
