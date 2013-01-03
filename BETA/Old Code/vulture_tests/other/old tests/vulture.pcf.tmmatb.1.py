#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module for test results
import vultureSoup		# Crawler to scrape vulture.com for data and content
from selenium import selenium

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "TV, Music, Movies, Art, Theater, Books Module"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.tmmatb()			# Call the relevant BeautifulSoup module for scraping data

CSS = open('../data/vulture.home.tmmatb.css.txt', 'r').readlines()		# a = presence; Is it there?
CONTENT = open('../data/vulture.home.tmmatb.content.txt.', 'r').readlines() 	# b = content;	Does it have the right stuff?
DATA = open('../data/vulture.home.tmmatb.data.txt', 'r').readlines() 		# c = function; Does it work?

x = 0

# This test opens www.vulture.com and does the following:
#	ENTER INFORMATION
	

class TMMATB(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
	
	########################################################################

    def test_a(self):

    # Tests for the presence of elements in the module
	
	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        comments = "html.js body#nymag.vulture div#wrap-wrap.skin-takeover div#wrap div#content div#content-primary div#features-wrap div.parsys div.parbase section.features-group div.col section.vertical-books ul li.entry span.comment-tout span a.extra strong.article_comment_count"
	
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
    	    
    	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
	
	for each in CONTENT:

	    c = CONTENT[n].strip('\n') 
        
            try:
            	self.assertEqual("****", c)
            except AssertionError, e:
                print "FAILURE " + c
                self.verificationErrors.append(str(e))
                L.log(BROWSSERS[x], TEST, "FAIL, INCORRECT CONTENT", str(e) + c)
            else:
            	L.log(BROWSERS[x], TEST, "PASS, CORRECT CONTENT", c)
            n += 1

    def test_c(self):
    	    
    # Tests for the module's functionality
    	    
    	n = 0  
        sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
	
	for each in DATA:

	    d = DATA[n].strip('\n') 
        
            try:
            	sel.click("//a[@href='" + d + "']")
                sel.wait_for_page_to_load("50000")
            except Exception, e:
            	print "FAILURE " + d
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + d)
            else:
                L.log(BROWSERS[x], TEST, "PASS, PAGE LOADS", d)
                print "PASS " + d
                sel.go_back()
                sel.wait_for_page_to_load("50000")
                
    	    n += 1

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(TMMATB)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
