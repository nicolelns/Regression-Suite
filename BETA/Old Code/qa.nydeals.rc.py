#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import time, datetime
import re
import pickle
import Logger			# Logging module (for test results, outputs results to a .txt file)
from selenium import selenium 

reload(sys)
sys.setdefaultencoding("utf-8")

BASEURL = 'http://newyork.grubstreet.dev.nymag.biz/2011/06/as_food_trucks_irk_the_upper_w.html?dfsdgdsgh=sdfsdgdshdshsdgdsghdshdsh'
BROWSERS = ('safari', 'safari')
TEST = "NY Mag Navigation Update - Desktop - NY Mag"

L = Logger.MainLogger(BASEURL, TEST)

CSS = open('../data/text/grubnews.css.txt', 'r').readlines()
URLS = {'http://newyork.grubstreet.dev.nymag.biz/2011/06/as_food_trucks_irk_the_upper_w.html?dfsdgdsgh=sdfsdgdshdshsdgdsghdshdsh': 'As Food Trucks Irk the Upper West Side, Is Their Era On the Wane? -- Grub Street New York'}
# Eventually, URLS will be URLS = pickle.load(open ('../pickle/FILENAME.p', 'wb'))

keys = URLS.keys()
values = URLS.values()

x = 0

"""
    This is a test for the NY Mag Deals Newsletter - Adding the Newsletter to Grub Street article pages:
    The DATA file is a pickle file generated by vultureSoup.Parser(), customized for this module.
    IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT, .P and .JSON FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!
    """	

#########################################################################
#########################################################################


class GrubNews(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL)
        self.selenium.start()
        print "TESTING www.nymag.com in " + BROWSERS[x]
	
	########################################################################
	
    def test_a(self):
        
        # Tests for the presence of elements in the module using CSS locators
        # This test is an 'assert' test: if any element is not present, the test fails
	
        n = 0
        sel = self.selenium
        sel.open(BASEURL)
        sel.wait_for_page_to_load("50000")
        test = "Test A - Presence of Elements on Page"
        print test
        
        # Loops through the data in the CSS file asserting each element is on the page
        
        for each in CSS:

	    c = CSS[n].strip('\n')
            
            try:
                self.failUnless(sel.is_element_present("css=" + c))
                
            except AssertionError, e:
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], test, "FAIL, ELEMENT NOT FOUND", str(e) + c)
            
            else:
                L.log(BROWSERS[x], test, "PASS, ELEMENT FOUND", c)
                
            n += 1
            
        self.email_test()
	
	########################################################################
	
    def email_test(self):
    	  
    	sel = self.selenium
    	n = 0
    	test = "Test B - Deals Newsletter Email"
    	print test
    	
    	emails = ('abcd', '', 'nowhere@foo.com')
    	
    	for each in emails:
    		
    	    email = emails[n]
    	
    	    try:
    	        sel.click("id=txt-newsletter-subscribe-deals")
                sel.type("id=txt-newsletter-subscribe-deals", email)
                
            except Exception, e:
        	L.log(BROWSERS[x], test, "FAIL, CANNOT TYPE IN THE BOX", email, exception=str(e))
        	
            else:
            	sel.click("id=btn-newsletters-deals")
        	L.log(BROWSERS[x], test, "PASS", email)
        	
            n += 1

	########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(GrubNews)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
