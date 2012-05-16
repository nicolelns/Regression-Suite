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
TEST = "Main Navigation (NY Mag, Grub St, Daily Intel, etc) - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.mainnav()

CSS = open('../data/text/mainnav.css.txt', 'r').readlines()	
DATA = pickle.load(open ('../data/pickle/mainnav.data.p', 'rb'))
x = 0

"""
This is a regression test for the Navigation at the top of Vulture's home page

"""	

#########################################################################
#########################################################################
	

class MainNav(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
    
    def test_mainnav(self):

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
            
        self.b_click()
        self.c_link_count()
            
        ########################################################################
	    
    def b_click(self):
    	    
        n = 0
	sel = self.selenium
	test = "Test B - Click and Wait for Page to Load"
	print test
        
	for each in DATA:

	    d = DATA[n] 
        
            try:
            	text = sel.get_text("//a[@href='" + d + "']")
                sel.click("link=" + text)
                sel.wait_for_page_to_load("50000")
                title = sel.get_title()
                
	    except Exception, e:
		print "FAILURE " + d, " does not load"
		L.log(BROWSERS[x], test, "FAIL, PAGE DOES NOT LOAD", d, exception=str(e))
		
	    else:
	    	L.log(BROWSERS[x], test, "PASS, PAGE LOADS", d)
            	
            self.back()
                 
            n += 1   
        
        ########################################################################

    def c_link_count(self):
    
    	n = 0 
        sel = self.selenium
        count = sel.get_css_count("css=" + CSS[1])
        test = "Test C - Correct Number of Links"
        print test
        
        if count != 4:
            L.log(BROWSERS[x], test, "FAIL, MISSING LINKS", str(count) + " links found")

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

    suite = unittest.TestLoader().loadTestsFromTestCase(MainNav)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
    

