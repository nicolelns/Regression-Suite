#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
#import Logger
import cutSoup

reload(sys)
sys.setdefaultencoding("utf-8")

chromedriver = '/Library/Python/2.7/site-packages/chromedriver'

"""
The below code is for the Internet Explorer remote driver; These tests were developed on a Mac :)

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


BASEURL = raw_input("Enter a BaseUrl: ")
BROWSERS = ('chrome', 'firefox', 'ie')
TEST = "The Cut Homepage - QA - Interview Module"

S = cutSoup.Parser(BASEURL)

CSS = open('../data/text/interview.css.txt', 'r').readlines()
DATA = S.interview()

keys = DATA.keys()
values = DATA.values()
x = 0


#########################################################################
#########################################################################

class Interview(unittest.TestCase):

    def setUp(self):
    	    
        if x == 0:
            self.driver = webdriver.Chrome(chromedriver)
            
        #elif x == 1:    
            #self.driver = webdriver.Firefox() 
            
        elif x == 1:
    	    self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.INTERNETEXPLORER)
        
        #elif x == 3:
	    #self.driver = webdriver.Remote(desired_capabilities = {}, command_executor = "http://localhost:8080/wd/hub")
        
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
	
    def test_image(self):
        
        """
    	The fail test is meant to "fail", in the sense that the CSS elements should NOT be on the page after nav update.
    	The element not being found is considered a pass.
    	
    	PASSING CONDITIONS:  None of the elements are found on the page.
    	FAILING CONDITIONS:  Any of the elements are found on the page.
    	"""	
    
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
                #L.log(BROWSERS[x], test, "FAIL, ELEMENT FOUND", c, exception=str(e))
            
            #else:
                #L.log(BROWSERS[x], test, "PASS, ELEMENT NOT FOUND", c)
                
            n += 1
            
        self.click()
	
	########################################################################
	
    def click(self):
    	    
    	driver = self.driver
    	test = "Test B - Click and Wait for Page"
    	print test
    	
    	link = keys[0]
    	
    	try:
    	    driver.find_element_by_xpath("//a[@class='contentTextWrap'][@href='" + link + "']").click()
	
        except AssertionError, e:
    	    print "link not clickable", str(e), link
    	    self.verificationErrors.append(str(e) + link)
    	    
    	self.text(self.title())
	driver.back() 
	self.image()
    	    
    	########################################################################
    	
    def text(self, title):
    	    
    	test = "Test C - Correct Title for Article"
    	print test
    	self.title = title
    	
    	t = values[0]
        text = t[1] + " -- The Cut"
        
        try:
            self.assertEqual(text, title)
            
	except AssertionError, e:
	    print str(e), "FAILURE, TEXT/TITLE DON'T MATCH, MANUALLY VERIFY"
	    
    	 
        ########################################################################
        
    def image(self):
    	    
    	driver = self.driver
    	test = "Test D - Image Exists and Links to Article"
    	print test	
    	
    	data = values[0]
    	img = data[0]
    	permalink = data[3]
    	
    	if img is not None:
    	
            try:
                driver.find_element_by_xpath("//img[@src='" + img + "']").click()
                r = driver.current_url
        	
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
    	        
    	    driver.back()
    	    self.imagefile()
    	
    	########################################################################
    	
    def headers(self):
    	    
    	driver = self.driver
    	test = "Test E - Interview Header and Read More"
    	print test
    	n = 0
    	
    	p = (CSS, CSS)
    	t = title
    	
    	for each in p:
    		
    	    try:
    	    	driver.find_element_by_css(p[n]).click()
    	    	
    	    except Exception, e:
    	    	print "CANNOT FIND/CLICK LINK", p[n], str(e)
    	    	
    	    else:
    	    	try:
    	            t2 = self.title()
    	    	    self.assertEqual(t, t2)
    	    	    
    	    	except Exception, e:
    	    	print "TITLES DON'T MATCH, VISUALLY VERIFY", t, t2, str(e)
    	    	
    	    n += 1
    	    	    
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
        
    def title(self):
    	    
    	driver = self.driver
    	t = driver.title
    	return t
    	
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

for x in range(0,2):

    suite = unittest.TestLoader().loadTestsFromTestCase(Interview)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
#L.save()
