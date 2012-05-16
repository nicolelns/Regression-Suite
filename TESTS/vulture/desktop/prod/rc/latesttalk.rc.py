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
TEST = "Latest Talk Module - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.latesttalk()

CSS = open('../data/text/latesttalk.css.txt', 'r').readlines()		
DATA = pickle.load(open ('../data/pickle/latesttalk.data.p', 'rb')) 	       

x = 0

"""
This is a regression test for the Latest Talk module on Vulture's home page

"""	

#########################################################################
#########################################################################
	

class LatestTalk(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
    
    def test_latesttalk(self):

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
            
        self.b_talk_links()
        self.c_content()
        self.d_click_test()
            
        ########################################################################
	    
    def b_talk_links(self):
    	    
    	n = 0
	sel = self.selenium
	test = "Test B - Links to Talk Page"
        print test
        
        links = ('Latest Talk', 'See All Conversations')
        talk_title = 'Talk News - Vulture'
        
	for each in links:
		
 	    d = links[n]		
		
	    try:
	    	sel.click("link=" + d)
	    	sel.wait_for_page_to_load("50000")
	    	title = sel.get_title()
            	
            except AssertionError, e:
            	L.log(BROWSERS[x], test, "FAIL, CANNOT CLICK LINK", d, exception=str(e))
                print "FAILURE, can't get link text " + d
                self.verificationErrors.append(d + str(e))
                
            else: 
                if talk_title != title:
                    L.log(BROWSERS[x], test, "FAIL, MISMATCHED TITLES", title)
                    print "FAILURE, " + title + " does not match " + talk_title
                    self.verificationErrors.append(title)  
                    
            self.back()
            	    	   
            n += 1 
            
        ########################################################################    
            
    def c_content(self):
    	    
    	n = 0
	sel = self.selenium
	test = "Test C - Content"
        print test    
                
        counts = (CSS[2], CSS[3], CSS[4], CSS[5])
        i = 0
        
        for each in counts:
        	
            count = sel.get_css_count("css=" + counts[i]) 	
        	
            if count != 2:
            	print count, " elements found, missing links, headers, etc"
            	L.log(BROWSERS[x], test, "FAIL, MISSING CONTENT", str(count))
                self.verificationErrors.append("Failure, incorrect number of articles in Latest Talk")
            
            i += 1
            	    
        ########################################################################

    def d_click_test(self):
   
   	n = 0 
        sel = self.selenium
        test = "Test D - Click and Wait"
        print test
        
        for each in DATA:
        	
            d = DATA[n]
        	
            try:
                sel.click("//a[@href='" + d + "']")
                sel.wait_for_page_to_load("50000")
                title = sel.get_title()
                
	    except Exception, e:
		print "FAILURE " + d, " does not load"
		L.log(BROWSERS[x], test, "FAIL, PAGE DOES NOT LOAD", d, exception=str(e))
		
	    else:
	    	L.log(BROWSERS[x], test, "PASS, PAGE LOADS", d)
	
            self.back()
	        
	    try:
	        sel.click("css=" + CSS[5].strip('\n'))
            	sel.wait_for_page_to_load("50000")
                
            except AssertionError, e:
            	L.log(BROWSERS[x], test, "FAIL, CANNOT CLICK ON JOIN IN", d, exception=str(e))
                print "FAILURE, can't click join in " + d
                self.verificationErrors.append(d + str(e))
                
            else:
            	L.log(BROWSERS[x], test, "PASS, CLICKED JOIN IN", d)
            	
            self.back()


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

    suite = unittest.TestLoader().loadTestsFromTestCase(LatestTalk)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()