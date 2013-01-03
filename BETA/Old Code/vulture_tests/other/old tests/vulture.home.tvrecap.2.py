#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "TV Recap Module"

text_list  = []

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.tvrecap()

CSS = open('../data/vulture.home.tvrecap.css.txt', 'r').readlines()             
CONTENT = open('../data/vulture.home.tvrecap.content.txt', 'r').readlines()
DATA = open('../data/vulture.home.tvrecap.data.txt', 'r').readlines()           

x = 0

"""This is a regression test for the TV Recap module on Vulture's home page"""
""" Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements (via XPATH locators in the CONTENT file) contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  The DATA file contains this data"""
"""IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!"""	

#########################################################################
#########################################################################


class TVRecap(unittest.TestCase):
    
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
    
        comments = "html.js body#nymag.vulture div#wrap-wrap.skin-takeover div#wrap div#content div#content-primary div#features-wrap div#top-features.features-group div.col-b div.parsys div.parbase section#feature-recaps.feature-recaps div#tab-latestrecaps.content article.entry p span.comment-tout span a.extra strong.article_comment_count"
    	    
    	n = m = i = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        # Loops through the data in the CONTENT file (XPATH locators) to aggregate data for test c and to make sure each article in TMMATB has a link and corresponding text
        
	for each in CONTENT:

	    c = CONTENT[n].strip('\n') 
        
            try:
                sel.is_element_present("xpath=//img[@src='" + c + "']")
            	
            except Exception, e:
                print "FAILURE, can't find image " + c
                self.verificationErrors.append(str(e))
                
            else:
            	pass
        
            n += 1
        
        # Get link text
        
        for each in DATA:
        	
            d = DATA[m].strip('\n')
            
            if re.search('recap', d, re.I):
            	    
            	spam = "xpath=//a[@class='permalink'][@href='" + d + "']"
        
            else:
            	    
            	spam = "xpath=//a[@href='" + d + "']"
            
                try:
            	    text = sel.get_text(spam)
            	
                except Exception, e:
                    print "FAILURE, can't get link text " + d
                    print str(e)
                    self.verificationErrors.append(str(e))
                
                else:
                    text_list.append(text)
                
            m += 1
            
        # Count number of headings, articles, etc. by CSS selector and make sure all values are equal    
                   
        counts = (CSS[6], CSS[7], CSS[8], CSS[9], CSS[10])
        
        for each in counts:
            	    
            count = sel.get_css_count("css=" + counts[i])
            
            if (count != 4):
                print "MISSING ELEMENTS!"
                print counts[i], " count"
                	
            i += 1
                
            if S.tvrecap() != (count,count):                                #S.tvrecap(x,y), where x = number of links to individual articles and y = number of links to articles WITH an image, these values (integers) should be equal
                print "MISMATCHED ARTICLES"
	  
        ########################################################################

    def test_c(self):
    	    
    # Tests for the module's functionality
    # Clicks on each link based on its text (text between <a> tags)
    # Tries to open each page based on its address (href attribute)
    	
    	n = i = 0 
        sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        # First, make sure each link can be clicked on
        
        for each in text_list:
        	
            try:
            	sel.click("link=" + text_list[i])
                sel.wait_for_page_to_load("50000")
                
	    except Exception, e:
		print "FAILURE " + text_list[i]
		print str(e)
		
	    else:
		print "PASS " + text_list[i]
		sel.go_back()
	        sel.wait_for_page_to_load("50000")
	    
            i += 1
            
        # Second, make sure each URL opens
        # After each page opens, get the title
        # Make sure the link text (acquired from test 'b') matches the title of each opened page
			
	for each in DATA:

	    d = DATA[n].strip('\n') 
        
            try:
            	sel.open("xpath=//a[@href='" + d + " and @class='permalink']")
                sel.wait_for_page_to_load("50000")
                
            except Exception, e:
            	print "FAILURE " + d, str(e)
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + d)
                
            else:
                L.log(BROWSERS[x], TEST, "PASS, PAGE LOADS", d)
                print "PASS " + d
                
                try:
                    title = sel.get_title()
                    
                except AssertionError, e:
                    print "FAIL, cannot get title" + d
                    
                else:
                    if re.search(text_list[i], title, re.I):
                        print "PASS, correct title", d
                        
                    elif re.search("not found", title, re.I):
                    	print "FAIL, 404 error", d
                    	
                    else:
                    	print "Test has a bug", d
                    	
                    i += 1
                    
                    	
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

    suite = unittest.TestLoader().loadTestsFromTestCase(TVRecap)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
