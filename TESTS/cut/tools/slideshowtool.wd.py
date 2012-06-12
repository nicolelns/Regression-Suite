#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.action_chains import ActionChains
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


BASEURL = 'http://author01.qa.nymetro.com/'
BROWSERS = ('chrome', 'firefox') 	# Add browsers
TEST = "Slideshow Tool - Author - The Cut"

#L = Logger.MainLogger(BASEURL, TEST)

#PASS_CSS = open('../data/text/newnavigation.pass.css.txt', 'r').readlines()
#FAIL_CSS = open('../data/text/newnavigation.fail.css.txt', 'r').readlines()
#URLS = pickle.load(open('../data/pickle/newnavUrls.p', 'r'))

#keys = URLS.keys()
#values = URLS.values()

x = 0

"""
This is a test for the Cut Runway Builder.

"""	

#########################################################################
#########################################################################

class NewNavigation(unittest.TestCase):

    def setUp(self):
    	    
        if x == 0:
            self.driver = webdriver.Chrome(chromedriver)
            
        else:    
            self.driver = webdriver.Firefox()
            
        #elif x == 2:
    	    #self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.INTERNETEXPLORER)
        
        #elif x == 3:
	    #self.driver = webdriver.Remote(desired_capabilities = {}, command_executor = "http://localhost:8080/wd/hub")
	    #self.driver = webdriver.Remote("http://localhost:8080/wd/hub", webdriver.DesiredCapabilities.ANDROID)
        
        self.driver.implicitly_wait(10)
        self.mouse = webdriver.ActionChains(self.driver)
        self.verificationErrors = []
        print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
	
    def test_login(self):
	
        driver = self.driver
        test = "Test A - Login"
        print test
        
        driver.get(BASEURL + "apps/dashboard.html")
            
	try:
            driver.find_element_by_id("input-username").clear()
            driver.find_element_by_id("input-username").send_keys("admin")
            driver.find_element_by_id("input-password").clear()
            driver.find_element_by_id("input-password").send_keys("admin")
            driver.find_element_by_id("input-submit").click()
                
        except AssertionError, e:
            print "FAILURE TO LOGIN", str(e)
            self.verificationErrors.append(str(e))
            #L.log(BROWSERS[x], test, "FAIL, CANNOT LOG IN", "", exception=str(e))
             
        else:
            #L.log(BROWSERS[x], test, "PASS, LOGIN OK", "")
            print "OK"
            
        self.runway_builder()
        self.form_fill()
              
	########################################################################
	
    def runway_builder(self):
    	    
    	driver = self.driver
    	
    	try:
    	    driver.find_element_by_link_text("TheCut.com").click()
    	    driver.find_element_by_link_text("Create New Show").click()
    
	except Exception, e:
	    print "FAILURE" + str(e)
	    
    	else:
            print "PASS"
		
        ########################################################################
        
    def form_fill(self):
    	    
    	driver = self.driver
    	mouse = self.mouse
    	
    	
    	try:
	    menu1 = driver.find_element_by_id("label_name")
	    menu1.click()
	    mouse.move_to_element(menu1).perform()
	    driver.find_element_by_id("ui-active-menuitem").click()
	    driver.find_element_by_id("season_name").click()
	    driver.find_element_by_id("ui-active-menuitem").click()
	    driver.find_element_by_id("year_name").click()
	    driver.find_element_by_id("ui-active-menuitem").click()
	    driver.find_element_by_id("type_name").click()
	    driver.find_element_by_id("ui-active-menuitem").click()
	    driver.find_element_by_id("city_name").click()
	    driver.find_element_by_id("ui-active-menuitem").click()
	    driver.find_element_by_id("date").click()
	    driver.find_element_by_link_text("24").click()
	    driver.find_element_by_id("create_show").click()
	    
        except Exception, e:
            print "FAILURE", str(e)
            
        else:
            print "OK"
        	
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

    suite = unittest.TestLoader().loadTestsFromTestCase(NewNavigation)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1

#L.save()

