#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import time, datetime
import re
import pickle
import subprocess
#import Logger			
import cutSoup		
from selenium import selenium   

BASEURL = raw_input('Enter a BaseURL: ')
BROWSERS = ('firefox3 /Applications/Firefox 2.app/Contents/MacOS/firefox-bin', 'safari')
TEST = "The Feed Module - Desktop - The Cut Home Page"

#L = Logger.MainLogger(BASEURL, TEST)
S = cutSoup.Parser(BASEURL)

CSS = open('../data/text/feed.css.txt', 'r').readlines()
DATA = S.feed()

keys = DATA.keys()
values = DATA.values()
      
x = 0

"""
This is a regression test for The Cut's home page.  This test is for the automated feed.

"""	

#########################################################################
#########################################################################

	
class TheFeed(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
    
    def test_feed(self):

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
            	print "FAILURE " + c, str(e)
            	self.verificationErrors.append(str(e) + c)
                #L.log(BROWSERS[x], TEST, "FAIL, ELEMENT NOT FOUND", str(e) + c)
              
            n += 1
            
        self.b_responsive() 
            
        ########################################################################
        
    def content(self):
    	    
        sel = self.selenium
        test = "Test B - Correct Number of Timestamps, etc."
        print test
    	    
    	try:
            comment = sel.get_css_count(CSS[0])
            header = sel.get_css_count(CSS[1])
            text = sel.get_css_count(CSS[2])
            time = sel.get_css_count(CSS[3])
            link = sel.get_css_count(CSS[4])
            
        except AssertionError, e:
            self.verificationErrors.append(str(e))
            print "FAIL", str(e), " Cannot get elements!"
             
        else:
            if (len(comment) != len(header) != len(text) != len(time) != len(link)):
            	print "FAIL, Incorrect number of headers, timestamps, etc."
            	    
            else: 	    
                print "PASS"
                
        print "COMMENTS: ", len(comment)
        print "HEADERS: ", len(header)
        print "TEXT: ", len(text)
        print "TIME: ",  len(time)
        print "LINK: ",  len(link)
        
        ########################################################################
   
    def responsive(self):
    	
    	m = 0
	sel = self.selenium
	test = "Test C - Responsive Design"
	print test
	
	for each in keys:

            d = keys[m]
            data_list = values[m]
            
            # For n % 1, article headline, text, etc should be to the right of n % 0
            # IMPLEMENT LATER
	  
	    for w in range(0,3):  # w is for window
		
		img_list = data_list[1]
		image = img_list[w]
		digit = data_list[5]
		
		if image is not None:    
		    	    
		    if w == 0:
			sel.window_maximize()
			desktop_paragraph_loc = sel.get_element_position_left("//p[@class='articleText']")
			desktop_title_loc = sel.get_element_position_left("//a[@href='" + d + "']")
			  
		    elif w == 1:
			sel.get_eval("window.resizeTo(728, 1000);")
			tablet_paragraph_loc = sel.get_element_position_left("//p[@class='articleText']")
			tablet_title_loc = sel.get_element_position_left("//a[@href='" + d + "']")
			
		    elif w == 2:
			sel.get_eval("window.resizeTo(420, 600);")
			mobile_paragraph_loc = sel.get_element_position_left("//p[@class='articleText']")
			mobile_title_loc = sel.get_element_position_left("//a[@href='" + d + "']")
			    
		    w += 1
	        
	    
	    
	    m += 1
            
        sel.get_eval("window.resizeTo(1200, 1000);")
	        
    ########################################################################  
    
    def headers(self):
    	    
    	sel = self.selenium
    	test = "Test D - Links to News Page"
    	print test
    	n = 0
    	    
    	h = ("section.module header h3.feedTitle a", "div.readMoreDesktopWrap a p.readMore")
    	title = 'Articles News Feed'
    	
    	for each in h:

	    try:
	    	sel.click('css=' + h[n])
    	        sel.wait_for_page_to_load("50000")
    	        
    	    except Exception, e:
    	    	print "FAIL, CANNOT CLICK ON LINK", str(e)
    	    	self.verificationErrors.append(str(e) + h[n])
    	    	
    	    try:
    	    	t = sel.get_title()
    	        self.assertEqual(title, t)
    	        
    	    except Exception, e:
    	    	print "FAIL, CANNOT GET TITLE/TITLES DO NOT MATCH", str(e)
    	    	self.verificationErrors.append(str(e) + title + t)
    		
    	    self.back()
    	    n += 1
    		
    ########################################################################
    
    def click(self):
    	    
    	sel = self.selenium
    	test = "Test SLDKFJ - Click and Wait for Page to Load"
    	print test
    	n = 0
    	
    	for each in keys:
    	
    	d = keys[n]
    	
    	    try:
    		sel.click("//a[@href='" + d + "']")
    		
    	    except Exception, e:
    	    	print "FAILURE, CANNOT CLICK LINK" + str(e) + d
    	    	
    	    self.back()
    	    
    ########################################################################
    
    def title(self):
    	    
    	sel = self.selenium
    	t = sel.get_title
    	return t
    	    
    ########################################################################
    	
    def text(self, title):
    	    
    	test = "Test F - Correct Title for Article"
    	print test
    	self.title = title
    	
    	t = values[0]
        text = t[1] + " -- The Cut"
        
        try:
            self.assertEqual(text, title)
            
	except AssertionError, e:
	    print str(e), "FAILURE, TEXT/TITLE DON'T MATCH, MANUALLY VERIFY"
    	    
    ########################################################################
    
    def slideshow(self):
    	    
    	driver = self.driver
    	test = "Test E - Slideshows Have Images Always"
    	print test
    	    
	asdf = values[0]
    	asdfasdf = asdf[2]
    	asdfasdfasdf = asdfasdf[1]
    	
    	for each in keys:
    		
    	    if slideshow is not None:
    	    	    
    	    	blah
		    
    ########################################################################
	
    def headline(self):
    	  
    	test = "Test F - Short Headline is Used"
    	print test
    	    
	asdf = values[0]
    	asdfasdf = asdf[2]
    	asdfasdfasdf = asdfasdf[1]
    	
    	if len(str(asdfasdfadsf)) >= 40:
    		
    	    print "FAIL"
    	    
    ########################################################################
    	    
    def linkmatch(self):
    	    
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

    suite = unittest.TestLoader().loadTestsFromTestCase(TheFeed)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
#L.save()
