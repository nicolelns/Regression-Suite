#! /usr/bin/python

import unittest
import time, datetime
import re
import pickle
import subprocess
#import Logger			
import cutSoup		
from selenium import selenium   

BASEURL = raw_input('Enter a BaseURL: ')
BROWSERS = ('firefox3 /Applications/Firefox 2.app/Contents/MacOS/firefox-bin', )
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
            	self.verificationErrors.append(str(e))
                #L.log(BROWSERS[x], TEST, "FAIL, ELEMENT NOT FOUND", str(e) + c)
            
            else:
                #L.log(BROWSERS[x], TEST, "PASS, ELEMENT FOUND", c)
                pass
                
            n += 1
            
        self.b_responsive() 
            
        ########################################################################
   
    def b_responsive(self):
    	
    	m = 0
	sel = self.selenium
	test = "Test B - Responsive Design"
	print test
	
	for each in keys:

            d = keys[m]
            data_list = values[m]
            
            # For n % 1, article headline, text, etc should be to the right of n % 0
            # IMPLEMENT LATER
	  
	    for w in range(0,3):  # w is for window
		
		img_list = data_list[1]
		image = img_list[w]
		if image is not None:    
		    	    
		    if w == 0:
			sel.window_maximize()
			desktop_height = sel.get_element_height("//img[@src='" + image + "']")
			desktop_width = sel.get_element_width("//img[@src='" + image + "']")
			desktop_paragraph_loc = sel.get_element_position_left("//p[@class='articleText']")
			desktop_title_loc = sel.get_element_position_left("//a[@href='" + d + "']")
			  
		    elif w == 1:
			sel.get_eval("window.resizeTo(728, 1000);")
			tablet_height = sel.get_element_height("//img[@src='" + image + "']")
			tablet_width = width = sel.get_element_width("//img[@src='" + image + "']")
			tablet_paragraph_loc = sel.get_element_position_left("//p[@class='articleText']")
			tablet_title_loc = sel.get_element_position_left("//a[@href='" + d + "']")
			
		    elif w == 2:
			sel.get_eval("window.resizeTo(420, 600);")
			mobile_height = sel.get_element_height("//img[@src='" + image + "']")
			mobile_width = sel.get_element_width("//img[@src='" + image + "']")
			mobile_paragraph_loc = sel.get_element_position_left("//p[@class='articleText']")
			mobile_title_loc = sel.get_element_position_left("//a[@href='" + d + "']")
			    
		    w += 1
	        
	    if ((desktop_height >= tablet_height) and (desktop_height >= mobile_height) and (tablet_height >= mobile_height)):
		#L.log(BROWSERS[x], test, "PASS, IMAGE RESPONDS TO WINDOW RESIZE", image)
		print "PASS RESIZE", image
		
	    else:
		print "Resize image fails!", image
		#L.log(BROWSERS[x], test, "FAIL, IMAGE DOES NOT RESPOND TO WINDOW RESIZE", image)
		 
	    if ((desktop_paragraph_loc >= mobile_paragraph_loc) and (tablet_paragraph_loc >= mobile_paragraph_loc)):
		#L.log(BROWSERS[x], test, "PASS, EXCERPT RESPONDS TO WINDOW RESIZE", "Excerpt for " + d)
		print "PASS RESIZE", d
		
	    else:
		print "Resize exceprt fails!", d
		#L.log(BROWSERS[x], test, "FAIL, EXCERPT DOES NOT RESPOND TO WINDOW RESIZE", "Excerpt for " + d)
		
	    if ((desktop_title_loc >= mobile_title_loc) and (tablet_title_loc >= mobile_title_loc)):
		#L.log(BROWSERS[x], test, "PASS, ARTICLE TITLE RESPONDS TO WINDOW RESIZE", "Title for " + d)
		print "PASS RESIZE", d
		
	    else:
	    	print "Resize article fails!", d
		#L.log(BROWSERS[x], test, "FAIL, ARTICLE TITLE DOES NOT RESPOND TO WINDOW RESIZE", "Title for " + d)
	    
	    m += 1
            
        sel.get_eval("window.resizeTo(1200, 1000);")
	        
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
