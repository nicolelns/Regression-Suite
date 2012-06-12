#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox', 'safari')
TEST = "Media Kit Module - Desktop - Vulture Home"

CSS = open('../data/text/mediakit.css.txt', 'r').readlines()

L = Logger.MainLogger(BASEURL, TEST)
x = 0

class MediaKit(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################

    def test_mediakit(self):
	
	n = 0
	sel = self.selenium
        sel.open(BASEURL)
        sel.wait_for_page_to_load("50000")
        test = "Test A - Presence of Elements via CSS"
        print test
        
        
	for each in CSS:

	    c = CSS[n].strip('\n') 
        
            try:
                self.failUnless(sel.is_element_present("css=" + c))
                
            except AssertionError, e:
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], TEST, "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            
            else:
                L.log(BROWSERS[x], TEST, "PASS, ELEMENT FOUND", c)
                
            self.click_test(n)
                
            n += 1
               
        ########################################################################
	    
    def click_test(self, n):
    	    
    # Tests for the correct content within the module
    # This is a 'verify' test, it will not fail the whole test if one item fails
    	
	sel = self.selenium
	test = "Test B - Click and Wait for Page"
	print test
        
        self.n = n
        
        self.failUnless(sel.is_element_present("//img[@src='http://images.nymag.com/images/2/promos/10/09/vulture_network_banner.gif']"))
        self.failUnless(sel.is_element_present("//img[@src='http://nymag.com/images/2/sweepstakes/2012/Entertainment/Vulture_301x60.jpg']"))
        
        
        try:
            sel.click("css=" + CSS[self.n].strip('\n'))
            sel.wait_for_page_to_load("50000")
            
        except AssertionError, e:
            print "link not clickable"
            self.verificationErrors.append(str(e) + CSS[n])
            L.log(BROWSERS[x], test, "FAIL, CANNOT CLICK LINK", css[n], exception=str(e))
          
        else:
            try:
                self.assertEqual(sel.get_title(), "New York Media")
            
	    except AssertionError, e:
	    	L.log(BROWSERS[x], test, "FAIL, INCORRECT TITLE", CSS[n], exception=str(e))
	    	self.verificationErrors.append(str(e) + CSS[n])
            
	    else:
            	L.log(BROWSERS[x], test, "PASS, PAGE LOADS OK", "New York Media")

        ########################################################################  
    
    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(MediaKit)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()