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
from selenium.webdriver import ActionChains
import unittest, time, re
import nymagSoup

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

BASEURL = raw_input("Please enter a BaseURL: ")
BROWSERS = ('chrome', 'ie') 	# Add browsers
TEST = "NY Mag Utility Navigation Update - STG - NYM"

S = nymagSoup.Parser(BASEURL)

CSS = open('../data/text/utilitynav.css.txt', 'r').readlines()
DATA = S.utilitynav()

keys = DATA.keys()
values = DATA.values()

x = 0

"""
This is a test for the NY Mag Utility Navigation Update - Removing the Facebook button and adding share tool buttons:
The DATA file is generated by nymagSoup.Parser(), customized for this module.

"""	

#########################################################################
#########################################################################

class UtilityNav(unittest.TestCase):

    def setUp(self):
    	    
        if x == 0:
            self.driver = webdriver.Chrome(chromedriver)
            
        #elif x == 1:    
            #self.driver = webdriver.Firefox() 
            
        elif x == 1:
    	    self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.INTERNETEXPLORER)
        
        #elif x == 3:
	    #self.driver = webdriver.Remote(desired_capabilities = {}, command_executor = "http://localhost:8080/wd/hub")
	    #self.driver = webdriver.Remote("http://localhost:8080/wd/hub", webdriver.DesiredCapabilities.ANDROID)
        
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        print "TESTING " + BASEURL + " in " + BROWSERS[x]
        
	
	########################################################################
	
    def test_new_navigation(self):
    	    
    	driver = self.driver
    	driver.get(BASEURL)
    	
	self.css()
	self.click()
    	self.count()
    	self.img()
    	#self.fb() 	ERROR:  {"sessionId":"052e80dedee2730578e8c293ae9e726b","status":400,"value":{"message":"Invalid \'id\' parameter"}}
    	self.tw()
    	self.login()
    	self.reg()
    	
        ########################################################################
	
    def css(self):
       
        """
    	The pass test is a straightforward test - if the element is there, it passes.
    	
    	PASSING CONDITIONS:  None of the elements are found on the page.
    	FAILING CONDITIONS:  Any of the elements are found on the page.
    	
    	"""
    	
	n = 0
        driver = self.driver
        test = "Test A - Test for Correct CSS"
        print test
        
        # Loops through the data in the CSS file asserting each element is on the page
        
        for each in CSS:

	    c = CSS[n].strip('\n')
            
            try:
            	self.hover()
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, c))
                
            except AssertionError, e:
            	print "FAILURE " + c + str(e)
            	self.verificationErrors.append(str(e))
               
            n += 1
	
	########################################################################
	
    def click(self):
    
        """
        This test clicks and waits for the page to load
        The title is acquired and compared to the title in the URLS dictionary
        
        PASSING CONDITIONS:	Selenium can click "Home", get the page title and the home page loads correctly
        FAILING CONDITIONS:	Selenium cannot click home, cannot acquire the title of the page, or
        			the page does not loadk OK
        			
        """  
    
    	n = 0
        driver = self.driver
        test = "Test B - Click and Wait for Page Load"
        print test
	
	for each in values:
	    
	    url = keys[n]
	    data = values[n]	# Nth tuple	
	    xpath = data[0]
	    #u = data[1]
	    text = data[2]
	    self.hover()
	    
	    try:
	    	print text
		driver.find_element_by_link_text(text).click()
		time.sleep(1)
	    	
	    except Exception, e:
	    	print str(e)
	    	
	    	#"""
	    	print "Trying xpath..."
	    	
                try:
	    	    driver.find_element_by_xpath(xpath).click()
	    	    time.sleep(1)
	    	    
	        except Exception, e:
	            print "FAIL CLICK, ", str(e) + xpath
	            
	        else:
	            print "xpath click ok"
	            driver.back()
	            
	        #"""
	            
	    else:
	    	driver.back()
	        	
	    #self.url_loc(url) 		
	    n += 1
	    	   
	########################################################################
	
    def url_loc(self, url):
    	    
    	driver = self.driver
    	self.url = url
    	
    	loc = driver.current_url
    	
    	try:
    	    self.assertEqual(loc, self.url)
    	    
        except AssertionError, e:
            print "FAIL, WRONG URL", self.url, loc
            
        ########################################################################    
        
    def login(self):
    	    
    	driver = self.driver
    	test = "Test G - Login"
    	print test
    	
    	try:
    	    driver.find_element_by_xpath("//a[@class='login-lightbox']").click()
    	    time.sleep(2)
    	    
        except Exception, e:
            print "FAIL, CANNOT CLICK LOGIN ", str(e)
            self.verificationErrors.append("LOGIN FAIL")
            
        else:
            self.lightbox()
        
    ########################################################################
    	    
    def reg(self):
    
    	driver = self.driver
    	test = "Test H - Registration"
    	print test
    	
    	try:
    	    driver.find_element_by_link_text("Register").click()
    	    #driver.find_element_by_xpath("//a[@href='https://secure.qa.nymag.com/registration/']").click()
    	    
        except Exception, e:
            print "FAIL, CANNOT CLICK REGISTER ", str(e)
            self.verificationErrors.append("REGISTER FAIL")
            
        else:
            self.lightbox()
    	    
    ########################################################################	    
	
    def img(self):
    	    
    	driver = self.driver
    	test = "Test D - Magazine Image"
    	print test
    	
    	try:
    	    self.hover()
    	    driver.find_element_by_xpath("//img[@src='http://nymag.com/current_issue.jpg']").click()
        
	except Exception, e:
	    print "FAIL, CURRENT ISSUE IMG NOT FOUND", str(e)
	    self.verificationErrors.append(str(e) + "IMG NOT FOUND")
	    
	driver.back()
	
    	########################################################################
    	
    def fb(self):
    	    
    	"""
    	Facebook Share Tool Test
    	
    	PASSING CONDITIONS:  User can click on the Facebook buttons
    			     User can "Like" NYMag
    			     
    	FAILING CONDITIONS:  User cannot click on the Facebook buttons
    			     User cannot "Like" NYMag
    			     
    	"""
    	
    	driver = self.driver
    	test = "Test E - Facebook Like"
    	
    	try:
    	    driver.switch_to_frame(driver.find_elements_by_tag_name("iframe"[1]))
    	    driver.find_element_by_xpath("//*[@class='liketext']").click()
    	
        except Exception, e:
            print "CANNOT CLICK FB LIKE", str(e)
            
        else:
    	    driver.switch_to_window('f1-4')
    	    driver.close()
	
	########################################################################
	
    def tw(self):
    	    
    	"""
    	Twitter Share Tool Test
    	
    	PASSING CONDITIONS:  User can click on the Twitter buttons
    			     Lightbox appears
    			     Lightbox closes when user closes window
    			     
    	FAILING CONDITIONS:  User cannot click on the Twitter buttons
    			     Lightbox does not appear
    			     
    	"""
    	
    	driver = self.driver
    	test = "Test F - Twitter"
    	print test
    	
    	try:
    	    driver.find_element_by_xpath("//*[@class='twitter-follow-button']").click()
    	    driver.switch_to_window('f1-4')
    	    
        except Exception, e:
            print "CANNOT CLICK TWITTER", str(e)
            
        else:
    	    driver.close()
    	    driver.switch_to_window('f1-2')
    	    
    	    
	########################################################################
	
    def hover(self):
    	
    	driver = self.driver
    	
    	mouse = webdriver.ActionChains(driver)
    	element = driver.find_element_by_xpath("//*[@id='nav-mag']")
        mouse.move_to_element(element).click_and_hold(element).perform()
        mouse.release(element)
           
    	########################################################################
    	
    def count(self):
    	    
    	driver = self.driver
    	test = "Test C - Correct Number of Links in Nav"
    	print test
    	
    	self.hover()
    	links = len(driver.find_elements_by_css_selector("li.top div#sub_nav_mag ul li a"))
    	
	if links != 7:
    	    print "FAILURE, MISSING ITEMS IN NAV"
    	    self.verificationErrors.append("MISSING ITEMS IN NAV - " + str(links) + " LINKS")
        
	########################################################################
	
    def lightbox(self):
    	    
    	driver = self.driver
    	
    	try:
    	    driver.find_element_by_css_selector("div.head h5.closelightbox").click()
    	    
        except Exception, e:
            print str(e) + " lightbox fail"
            
        driver.refresh()
            
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

for x in range(0,1):

    suite = unittest.TestLoader().loadTestsFromTestCase(UtilityNav)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
