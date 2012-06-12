#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement
import unittest, time, re
import subprocess
import pickle
import Logger

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

BASEURL = 'http://dev.nymag.biz/'
BROWSERS = ('chrome', 'firefox') 	# Add browsers
TEST = "NY Mag Utility Navigation Update - DEV - NY Mag"

L = Logger.MainLogger(BASEURL, TEST)

CSS = open('../data/text/qa.utilitynav.css.txt', 'r').readlines()
DATA = pickle.load(open('../data/pickle/qa.utilitynavUrls.p', 'rb'))

keys = DATA.keys()
print keys
values = DATA.values()

x = 0

"""
This is a test for the NY Mag Utility Navigation Update - Removing the Facebook button and adding share tool buttons:
The DATA file is a pickle file generated by vultureSoup.Parser(), customized for this module.
IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT, .P and .JSON FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!

"""	

#########################################################################
#########################################################################

class UtilityNav(unittest.TestCase):

    def setUp(self):
    	    
        if x == 0:
            self.driver = webdriver.Chrome(chromedriver)
            
        elif x == 1:    
            self.driver = webdriver.Firefox() 
            
        elif x == 2:
    	    self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.INTERNETEXPLORER)
        
        #elif x == 3:
	    #self.driver = webdriver.Remote(desired_capabilities = {}, command_executor = "http://localhost:8080/wd/hub")
	    #self.driver = webdriver.Remote("http://localhost:8080/wd/hub", webdriver.DesiredCapabilities.ANDROID)
        
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        print "TESTING " + BASEURL + " in " + BROWSERS[x]
        print x
	
	########################################################################
	
    def test_new_navigation(self):
        
        """
        Preliminary test for the presence of various elements in the updated NY Mag navigation bar.
        CSS selectors are in a .txt file, and this test makes sure each element exists on the page before proceeding.
        Failures will fail the whole test.  (No point in continuing if images and links aren't present, right?).
        The other tests are called from this function to avoid repetitive and unnecessary SetUp and TearDown of the browser.
        In addition, the other tests can be commented out and not run - easy to select which tests run.  None are dependent on 
        results from other tests.  Only test_splash_feed needs to be run for the sub-tests to run.
        
        PASSING CONDITIONS:  All elements are present on the page.
        FAILING CONDITIONS:  Any ONE element is not present on the page.
        """
	
        n = 0
        driver = self.driver
        
        for n in range(0,1):
        
            url = keys[n]
            test = "Test A - Open Pages"
            print test
            
	    try:
                driver.get(BASEURL)
                
            except AssertionError, e:
            	print "FAILURE " + url
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], test, "FAIL, CANNOT OPEN PAGE", url, exception=str(e))
            
            else:
                L.log(BROWSERS[x], test, "PASS, OPENED PAGE", url)
              
            self.b_css()   
	    self.d_click_test()
	    
	    n += 1
	
	########################################################################
	
    def b_css(self):	
    	    
    	"""
    	The pass test is a straightforward test - if the element is there, it passes.
    	
    	PASSING CONDITIONS:  None of the elements are found on the page.
    	FAILING CONDITIONS:  Any of the elements are found on the page.
    	
    	"""
	n = 0
        driver = self.driver
        test = "Test C - Test for Correct CSS"
        print test
        
        # Loops through the data in the CSS file asserting each element is on the page
        
        for each in CSS:

	    c = CSS[n].strip('\n')
            
            try:
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, c))
                
            except AssertionError, e:
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], test, "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            
            else:
                L.log(BROWSERS[x], test, "PASS, ELEMENT FOUND", c)
                
            n += 1
            
        ########################################################################
            
    def d_click_test(self):
    
        """
        This test clicks and waits for the page to load
        The title is acquired and compared to the title in the URLS dictionary
        
        PASSING CONDITIONS:	Selenium can click "Home", get the page title and the home page loads correctly
        FAILING CONDITIONS:	Selenium cannot click home, cannot acquire the title of the page, or
        			the page does not loadk OK
        			
        """  
    
    	n = 0
        driver = self.driver
        test = "Test D - Click and Wait for Page Load"
        print test
	
	for each in keys:
	    
	    url = keys[n]
	    
	    try:
	        driver.find_element_by_xpath("//a[@href='" + url + "']").click()
	        title = driver.title
	
	    except Exception, e:
	    	print "FAILURE ", str(e)
	    	L.log(BROWSERS[x], test, "FAIL, CANNOT GET TITLE", url, exception=str(e))
	
	    else:
	        if re.search("not found", title, re.I):
		    print "FAILURE " + title
		    L.log(BROWSERS[x], test, "FAIL, 404 ERROR", title)
		
	        try:
		    self.assertEqual(title, values[n])
			
	        except AssertionError, e:
		    print "ERROR" + str(e) + url
		    self.verificationErrors.append(values[n] + str(e))
		    L.log(BROWSERS[x], test, "FAIL, TITLES DO NOT MATCH", values[n], exception=str(e))
	
	        else:	
		    L.log(BROWSERS[x], test, "PASS, PAGE LOAD OK", title)
			
	    n += 1
	    	   
	########################################################################
	
    def c_pass_css(self):	
    	    
    	"""
    	The pass test is a straightforward test - if the element is there, it passes.
    	
    	PASSING CONDITIONS:  None of the elements are found on the page.
    	FAILING CONDITIONS:  Any of the elements are found on the page.
    	
    	"""
	n = 0
        driver = self.driver
        test = "Test C - Test for Correct CSS"
        print test
        
        # Loops through the data in the CSS file asserting each element is on the page
        
        for each in PASS_CSS:

	    c = PASS_CSS[n].strip('\n')
            
            try:
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, c))
                
            except AssertionError, e:
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], test, "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            
            else:
                L.log(BROWSERS[x], test, "PASS, ELEMENT FOUND", c)
                
            n += 1
	
	########################################################################
	
    def login(self):
    	    
    	driver = self.driver
    	test = "Login for New Navigation"
    	#New Feature - Make sure test works when user is also logged in.
    	
	"""
    	try:
    	    driver.click on button
    	    driver.select window
    	    driver.is_element_present(By.CSS_SELECTOR, BLAH).click()	#Username
    	    driver.send_keys(BLAH)				
    	    driver.is_element_present(By.CSS_SELECTOR, BLAH).click()	#Password
    	    driver.send_keys(BLAH)    
    	    driver.is_element_present(By.CSS_SELECTOR, BLAH).click()
    	    
        except Exception, e:
    	    print "FAIL, CANNOT LOG IN"
    	    
        else:
    	    print "YAY"
    	"""
    	    
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

    suite = unittest.TestLoader().loadTestsFromTestCase(UtilityNav)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1

L.save()