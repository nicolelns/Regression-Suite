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
        
        """
    	The elements in CSS should all be found, and there should be one of each found for each article in the feed.
    	
    	PASSING CONDITIONS:  Each article has a link, timestamp, excerpt, header and comment placeholder.
    	FAILING CONDITIONS:  Any of the elements are not on the page or the wrong number of elements is present.
    	
    	"""	
    
	n = 0
        driver = self.driver
        driver.get(BASEURL)
        test = "Test A - Presence of Elements via CSS"
        print test
         
        try:
            comment = driver.find_elements_by_class_name(CSS[0])
            header = driver.find_elements_by_class_name(CSS[1])
            text = driver.find_elements_by_class_name(CSS[2])
            time = driver.find_elements_by_class_name(CSS[3])
            link = driver.find_elements_by_class_name(CSS[4])
            
        except AssertionError, e:
            self.verificationErrors.append(str(e))
            #L.log(BROWSERS[x], test, "FAIL, CANNOT GET ELEMENTS", "", str(e), exception=str(e))
            print "FAIL", str(e), " Cannot get elements!"
             
        else:
            if (len(comment) != len(header) != len(text) != len(time) != len(link)):
            	# Removed L.log(), replaced with print
            	#L.log(BROWSERS[x], test, "FAIL, INCORRECT NUMBER OF HEADERS, TIMESTAMPS, ETC", "", exception=str(e))
            	print "FAIL, Incorrect number of headers, timestamps, etc."
            	    
            else: 	    
                #L.log(BROWSERS[x], test, "PASS, CORRECT NUMBER OF HEADERS, TIMESTAMPS, ETC", "")
                print "PASS"
                
        print "COMMENTS: ", len(comment)
        print "HEADERS: ", len(header)
        print "TEXT: ", len(text)
        print "TIME: ",  len(time)
        print "LINK: ",  len(link)        
        
        self.b_click_test()
           
	########################################################################
	
    def b_click_test(self):
    
        """
        This test clicks and waits for the page to load
        
        			
        """  
    
    	n = 0
        driver = self.driver
        test = "Test B - Click Links and Wait for Page Load"
        print test
	
	for each in keys:
	    
	    url = keys[n]
	    
	    try:
	    	driver.find_element_by_xpath("//a[@class='permalink'][@href='" + url + "']").click()
	
	    except Exception, e:
	    	#L.log(BROWSERS[x], test, "FAIL, CANNOT GET TITLE", url, exception=str(e))
	    	print "FAILURE!, Cannot click element!", str(e)
	    	print "URL: " + url
	
	    else:
	        #L.log(BROWSERS[x], test, "PASS, PAGE LOAD OK", url)
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
	    
	    """
	    
	    try:
	    	driver.find_element_by_xpath("//a[@class='permalink'][@href='" + url + "']").click()
	
	    except Exception, e:
	    	print BROWSERS[x], test, "FAIL, CANNOT GET TITLE", url, exception=str(e)
	
	    else:
	        print BROWSERS[x], test, "PASS, PAGE LOAD OK", url
	        driver.back()
	        
	    """
			
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
