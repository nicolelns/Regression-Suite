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
import nymagSoup
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

BASEURL = 'http://dev.vulture.com/'
BROWSERS = ('chrome', 'firefox', 'ie') 	# Add browsers
TEST = "NY Mag Lazy Load - QA - NY Mag"

L = Logger.MainLogger(BASEURL, TEST)

CSS = open('../data/text/qa.lazyload.css.txt', 'r').readlines()
DATA = open('../data/text/qa.lazyload.data.txt', 'r').readlines()

S = nymagSoup.Parser(DATA[0].strip('\n'))

x = 0

"""
This is a test for the NY Mag Lazy Load ad feature:

"""	

#########################################################################
#########################################################################

class LazyLoad(unittest.TestCase):

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
	
	########################################################################
	
    def test_lazy_load(self):
        
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
        
        for each in DATA:
        
            url = DATA[n].strip('\n')
            	    
            test = "Test A - Open Pages"
            print test
            
	    try:
                driver.get(url)
                
            except AssertionError, e:
            	print "FAILURE " + url
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], test, "FAIL, CANNOT OPEN PAGE", url, exception=str(e))
            
            else:
                L.log(BROWSERS[x], test, "PASS, OPENED PAGE", url)
            
	    self.scroll()    # Scroll down and try to find the element
	    self.b_css()
	    self.c_query_implement()	# Known issue with trying to find correct iframe
	    #self.d_click_test()
	    
	    n += 1
	
	########################################################################
	
    def b_css(self):	
    	    
    	"""
    	The pass test is a straightforward test - if the element is there, it passes.
    	
    	PASSING CONDITIONS:  Any of the elements are found on the page.
    	FAILING CONDITIONS:  None of the elements are found on the page.
    	
    	"""
	n = 0
        driver = self.driver
        test = "Test B - Test for Correct CSS"
        print test
        
        # Loops through the data in the CSS file asserting each element is on the page
        
        for each in CSS:

	    c = CSS[n].strip('\n')
            
            try:
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, c))
                
            except AssertionError, e:
            	print "FAILURE " + c + str(e)
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], test, "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            
            else:
                L.log(BROWSERS[x], test, "PASS, ELEMENT FOUND", c)
                
            n += 1
            
        ########################################################################
        
    def c_query_implement(self):
    	    
    	"""
    	This function verifies the presence of the correct ord value and test=true in the script source.
    	
    	"""
    	
    	driver = self.driver
    	test = "Test C - Correct Parameters"
    	print test
    	
    	try:
    	    driver.find_element_by_xpath("//div[@id='ad-flex-2']")
    	    
    	except Exception, e:
	    print "FAILURE ", str(e)
	    L.log(BROWSERS[x], test, "FAIL, CANNOT FIND AD", "AD", exception=str(e))
	
	else:
	    L.log(BROWSERS[x], test, "PASS, AD FOUND", "AD")
	    S.lazy_load()
	    
	########################################################################
            
    def d_click_test(self):
    
        driver = self.driver
        test = "Test D - Click and Wait for Page Load"
        print test
	
	try:
	    driver.find_element_by_xpath("//div[@id='ad-flex-2']").click()
	
	except Exception, e:
	    print "FAILURE ", str(e)
	    L.log(BROWSERS[x], test, "FAIL, CANNOT CLICK", BASEURL, exception=str(e))
	
	else:
	    L.log(BROWSERS[x], test, "PASS, PAGE LOAD OK", CSS[0].strip('\n'))
	    driver.back()
	
        ########################################################################	
	
    def scroll(self):
    	    
    	driver = self.driver    
    	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"); 
    	time.sleep(3)
    	return
	
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

    suite = unittest.TestLoader().loadTestsFromTestCase(LazyLoad)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1

L.save()
