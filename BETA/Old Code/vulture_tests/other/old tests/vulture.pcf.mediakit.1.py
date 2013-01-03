#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "Media Kit Module"

DATA = ('html.js body#nymag.vulture div#wrap-wrap.skin-takeover div#wrap div#content div#content-secondary div.parsys div.parbase section.vulture-network a img')

L = Logger.MainLogger(BASEURL, TEST)
x = 0

# This test opens www.vulture.com and does the following:
#	ENTER INFORMATION
	

class MediaKit(unittest.TestCase):

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
	    
    def test_bc(self):
    	    
    # Tests for the correct content within the module
    # This is a 'verify' test, it will not fail the whole test if one item fails
    	    
        comments = "html.js body#nymag.vulture div#wrap-wrap.skin-takeover div#wrap div#content div#content-primary div#features-wrap div.parsys div.parbase section.features-group div.col section.first ul li.entry span.comment-tout span a.extra strong.article_comment_count"    

    	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        self.failUnless(sel.is_element_present("//img[@src='http://images.nymag.com/images/2/promos/10/09/vulture_network_banner.gif'"))
        
        try:
            sel.click("//a[@href=''")
   
        except AssertionError, e:
            print "link not clickable"
            self.verificationErrors.append(str(e))
          
        else:
            print "PASS"
            self.assertEqual(sel.get_title(), "New York Media")
            print "OK"

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