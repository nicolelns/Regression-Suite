#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import re
import cutSoup
import pickle
#import Logger

reload(sys)
sys.setdefaultencoding("utf-8")

BASEURL = raw_input('Enter a BaseURL: ')
BROWSERS = ('chrome', 'firefox', 'ie')
TEST = "The Cut Homepage - Desktop - The Feed"

chromedriver = '/Library/Python/2.7/site-packages/chromedriver'

"""
The below code is for the Internet Explorer remote driver; These tests were developed on a Mac
Webdriver can run tests in chrome (using the above path for chromedriver), Firefox, IE, Android, iOS

"""

PROXY = "localhost:8080"

webdriver.DesiredCapabilities.INTERNETEXPLORER['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}

#L = Logger.MainLogger(BASEURL, TEST)
S = cutSoup.Parser(BASEURL)

CSS = ('articleCommentCount', 'permalinkWrap', 'articleText', 'timestamp', 'permalink')
DATA = S.feed()

keys = DATA.keys()
values = DATA.values()

x = 0

"""
This is a test for the feed module on the Cut home page:
The CSS file is a text file with some CSS class names in it.
DATA is a dictionary containing urls and other data.

"""	

#########################################################################
#########################################################################

class TheFeed(unittest.TestCase):

    def setUp(self):
    	    
        if x == 0:
            self.driver = webdriver.Chrome(chromedriver)
            
        elif x == 1:    
            self.driver = webdriver.Firefox() 
            
        elif x == 2:
    	    self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.INTERNETEXPLORER)
        
        #elif x == 3:
	    #self.driver = webdriver.Remote(desired_capabilities = {}, command_executor = "http://localhost:8080/wd/hub")
        
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
	
    def test_feed(self):
        
        n = 0
        driver = self.driver
        driver.get(BASEURL)
        test = "Test A - Presence of Elements via CSS"
        print test
        
        # Loops through the data in the CSS file asserting each element is on the page
        
        for each in CSS:

	    c = CSS[n].strip('\n')
            
            try:
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, c))
                
            except AssertionError, e:
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e))
            	
            n += 1
        
        self.content()
           
	########################################################################
	
    def content(self):
    	    
        driver = self.driver
        test = "Test B - Correct Number of Timestamps, etc."
        print test
    	    
    	try:
            comment = driver.find_elements_by_class_name(CSS[0])
            header = driver.find_elements_by_class_name(CSS[1])
            text = driver.find_elements_by_class_name(CSS[2])
            time = driver.find_elements_by_class_name(CSS[3])
            link = driver.find_elements_by_class_name(CSS[4])
            
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
	
    def click(self):
    
    	n = 0
        driver = self.driver
        test = "Test C - Click Links and Wait for Page Load"
        print test
	
	for each in keys:
	    
	    url = keys[n]
	    
	    try:
	    	driver.find_element_by_xpath("//a[@class='permalink'][@href='" + url + "']").click()
	
	    except Exception, e:
	    	print "FAILURE!, Cannot click element!", str(e)
	    	print "URL: " + url
	
	    else:
	        print "PASS"
	        driver.back()
			
	    n += 1
	    
	########################################################################
	
    def c_image_test(self):
    
        """
        TODO:  TEST IMAGES ONCE THEY APPEAR IN THE FEED
        
        			
        """  
    
    	n = m = 0
        driver = self.driver
        test = "Test C - Images"
        print test
	
	for each in keys:
	    
	    datum = values[n]
	    img_list = datum[1]
	    img = img_list[m]
	    
	    num = datum[6]
	    
	    if num <=2:
	    	  
	    	self.failIf(img is not None)
	    	
	    n += 1
	    
    	########################################################################
    	
    def slideshow(self):
    	    
    	driver = self.driver
    	test = "Test D - Slideshows Display Image"
    	print test
    	
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
    	
    def title(self):
    	    
    	driver = self.driver
    	t = driver.title
    	return t
    	    
    	########################################################################
    	
    def headers(self):
    	    
    	driver = self.driver
    	test = "Test C - Links to News Page"
    	print test
    	n = 0
    	    
    	h = ("section.module header h3.feedTitle a", "div.readMoreDesktopWrap a p.readMore")
    	title = 'Articles News Feed'
    	
    	for each in h:

	    try:
	    	driver.find_element_by_css(h[n]).click()
    	        
    	    except Exception, e:
    	    	print "FAIL, CANNOT CLICK ON LINK", str(e)
    	    	self.verificationErrors.append(str(e) + h[n])
    	    	
    	    try:
    	    	t = driver.title
    	        self.assertEqual(title, t)
    	        
    	    except Exception, e:
    	    	print "FAIL, CANNOT GET TITLE/TITLES DO NOT MATCH", str(e)
    	    	self.verificationErrors.append(str(e) + title + t)
    		
    	    self.back()
    	    n += 1
    	    
    	########################################################################
    	
    def is_element_present(self, how, what):
    	    
        try: 
            self.driver.find_element(by=how, value=what)
        
        except NoSuchElementException, e: 
            return False
        
        return True
    
        ########################################################################
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for x in range(0,3):

    suite = unittest.TestLoader().loadTestsFromTestCase(TheFeed)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
#L.save()
