#! /usr/bin/python
# -*- coding: latin-1 -*-

import unittest
import time, datetime
import re
#import Logger			
import cutSoup
from selenium import selenium   

BASEURL = raw_input("Enter a BaseURL: ")
BROWSERS = ('firefox3 /Applications/Firefox 2.app/Contents/MacOS/firefox-bin', 'safari')
TEST = "The Cut Homepage - QA - Interview Module"

S = cutSoup.Parser(BASEURL)

CSS = open('../data/text/interview.css.txt', 'r').readlines()
DATA = S.interview()

keys = DATA.keys()
values = DATA.values()

#L = Logger.MainLogger(BASEURL, TEST)
x = 0

class Interview(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################

    def test_interview(self):
	
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
             
            n += 1
            
        self.responsive_test()
               
        ########################################################################
	    
    def click_test(self):
    	    
	sel = self.selenium
	test = "Test B - Click and Wait for Page"
	print test
        
        link = keys[0]
        
        try:
            sel.click("//a[@href='" + link + "']")
            sel.wait_for_page_to_load("50000")
            
        except AssertionError, e:
            print "link not clickable", str(e), keys[0]
            self.verificationErrors.append(str(e) + link)
            #L.log(BROWSERS[x], test, "FAIL, CANNOT CLICK LINK", css[n], exception=str(e))
        
            self.title()
	    self.text()	
	    self.back()
        
        ########################################################################
        
    def responsive_test(self):
    	    
        sel = self.selenium
        test = "Test D - Responsive Design"
        print test
        m = 0
        
        for each in keys:
        	
            data = values[m]
            image = data[0]
            
            if image is not None:
            	
		for w in range(0,3):
		    	    
		    if w == 0:
			sel.window_maximize()
			time.sleep(1)
			self.failIf(sel.is_visible("//p[@class='contentReadMore']"))
			  
		    elif w == 1:
		    	sel.get_eval("window.resizeTo(728, 1000);")
		    	time.sleep(1)
			self.failIf(sel.is_visible("//p[@class='contentReadMore']"))
			
		    else:
		    	sel.get_eval("window.resizeTo(300, 600);")
		    	time.sleep(1)
			self.failUnless(sel.is_visible("//p[@class='contentReadMore']"))
			
		    self.click_test()
		    w += 1
                
	    else:
            	print "NO IMAGE for URL " + feed_keys[m]
	        
	    m += 1
            
        sel.get_eval("window.resizeTo(1200, 1000);")  
        
        ########################################################################
        
    def text(self):
    	    
    	sel = self.selenium
    	test = "Test C - Correct Title for Article"
    	print test
    	
    	t = values[0]
        text = t[1] + " -- The Cut"
        
        try:
            self.assertEqual(text, self.title())
            
	except AssertionError, e:
	    #L.log(BROWSERS[x], test, "FAIL, INCORRECT TITLE", CSS[n], exception=str(e))
	    print str(e), "FAILURE, TEXT/TITLE DON'T MATCH"
	    
        ########################################################################  
        
    def imagefile(self):
    	    
    	data = values[0]
    	img_src = data[0]
    	silo = data[2]
    	
    	if silo is None:
    		
       	    try:
       	    	re.search(img_src, '.jpg', re.I)
       	    	
       	    except Exception, e:
       	    	print "NO JPG IN NON-SILO IMAGE", img_src, str(e)
       	    	self.verificationErrors.append(img_src + str(e))
       	    	
       	else:
            try:
       	    	re.search(img_src, '.png', re.I)
       	    	
       	    except Exception, e:
       	    	print "NO PNG IN SILO IMAGE", img_src, str(e)
       	    	self.verificationErrors.append(img_src + str(e))
       	    	
       	########################################################################
       	
    def headers(self):
    	    
    	sel = self.selenium
    	test = "Test E - Interview Header and Read More"
    	print test
    	n = 0
    	
    	p = (CSS, CSS)
    	t = title
    	
    	for each in p:
    		
    	    try:
    	    	sel.click("css="p[n])
    	    	
    	    except Exception, e:
    	    	print "CANNOT FIND/CLICK LINK", p[n], str(e)
    	    	
    	    else:
    	    	try:
    	            t2 = self.title
    	    	    self.assertEqual(t, t2)
    	    	    
    	    	except Exception, e:
    	    	print "TITLES DON'T MATCH, VISUALLY VERIFY", t, t2, str(e)
    	    	
    	    n += 1
    	    	    
    	########################################################################
       	
    def image(self):
    	    
    	sel = self.selenium
    	test = "Test E - Image Links to Article"
    	print test
    	
    	data = values[0]
    	img = data[0]
    	permalink = data[3]
    	
    	if img is not None:
    	
            try:
                sel.click("//img[@src='" + img + "']")
                r = sel.get_location
        	
            except Exception, e:
                print "FAIL, CAN'T CLICK IMAGE" + str(e) + img
                print "Visually verify"
                #self.verificationErrors.append(img + str(e))
            
            try:
		self.assertEqual(r, permalink) 
        	
            except Exception, e:
    	        print "FAIL, IMAGE DOES NOT LINK TO ARTICLE", str(e)
    	        print "Visually verify"
                #self.verificationErrors.append(img + str(e))
    	        
    	    self.back()
    	    self.imagefile()
    	    
    	########################################################################
        
    def back(self):
    	    
    	sel = self.selenium
    	sel.go_back()
    	sel.wait_for_page_to_load("50000")
    	
    	########################################################################
    	
    def title(self):
    	    
    	sel = self.selenium
    	t = sel.get_title()
    	return t
    	
    	########################################################################
    
    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(Interview)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
#L.save()
