#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import wait
import unittest, time, re
import HTMLTestRunner

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


BROWSERS = ('chrome', 'firefox', 'ie')
TEST = "The Cut Runway Show Opener"
	

#########################################################################
#########################################################################

class RunwayShowOpener(unittest.TestCase):

    def setUp(self):
    	    
        if y == 0:
            self.driver = webdriver.Chrome(chromedriver)
            
        elif y == 1:    
            self.driver = webdriver.Firefox() 
            
        elif y == 2:
    	    self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.INTERNETEXPLORER)
        
        #elif y == 3:
	    #self.driver = webdriver.Remote(desired_capabilities = {}, command_executor = "http://localhost:8080/wd/hub")
        
        self.driver.get(show)
        
        self.driver.implicitly_wait(10)
        self.wait = wait.WebDriverWait(self.driver, 10)
        self.verificationErrors = []
        
        print "TESTING " + show + " in " + browser
        print TEST
        
	########################################################################
    
    def test_open_close_show(self):
    	    
    	driver = self.driver
    	driver.find_element_by_xpath("//a[contains(text(),'View the Collection')]").click()
    	
	for i in range(60):
		
            try:
                driver.find_element_by_xpath("/html/body/section[2]/header/a").click() 
                break
            except: 
            	pass
            
            time.sleep(1)
            
        else: self.fail("time out")
    	
        ########################################################################
    	
    def test_runway(self):
    
        driver = self.driver
        driver.find_element_by_xpath("(//a[contains(@href, '/thecut/runway/')])[2]").click()
        time.sleep(2)
        url = str(driver.current_url)
        
        self.assertEqual(url, BASE + 'runway/')
    
        ########################################################################
    	 
    def test_fashion(self):
    	  
        driver = self.driver
        driver.find_element_by_xpath("(//a[contains(@href, '/thecut/fashion/')])[2]").click()
        time.sleep(2)
        url = str(driver.current_url)
        
        self.assertEqual(url, BASE + 'fashion/')	  
    	  
    	########################################################################  
      
    def test_show_opener(self):
    	
    	driver = self.driver
    	
    	driver.find_element_by_css_selector("span.breadCrumbs a.breadCrumbsLink").click()
    	time.sleep(1)
        driver.find_element_by_css_selector("li.showFinderListItem.selected").click()
        driver.find_element_by_css_selector("#showfinder_cities > li.showFinderListItem.selected").click()
        driver.find_element_by_css_selector("span.x").click()
        
        driver.find_element_by_css_selector("span.openerShowChooserLink.topOfPage").click()
        time.sleep(1)
        driver.find_element_by_css_selector("li.showFinderListItem.selected").click()
        driver.find_element_by_css_selector("#showfinder_cities > li.showFinderListItem.selected").click()
        driver.find_element_by_css_selector("span.x").click()
    	    
    	########################################################################
    	
    def test_pop_shows(self):
        	
        driver = self.driver
        
        driver.find_element_by_css_selector("nav.nextCarousel").click()
        driver.find_element_by_css_selector("nav.prevCarousel").click()
        silos = driver.find_elements_by_css_selector("img.silo")
        
        pop_shows = driver.find_elements_by_css_selector('ul.mostPopularShowsList li.mostPopularShowsListitem')
        
        self.assertEqual(len(pop_shows), len(silos))

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
	
    if x == 0:
    	ENV = 'stg'
    	BASE = 'http://stg.nymetro.com/thecut/'
	SHOWS = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/stg.runway_shows.txt', 'r').readlines()	
    
    elif x == 1:
    	ENV = 'ec2'
    	BASE = 'http://ec2.qa.nymetro.com/thecut/'
        SHOWS = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/ec2.runway_shows.txt', 'r').readlines()
        
    else:
    	ENV = 'prod'
    	BASE = 'http://nymag.com/thecut/'
    	SHOWS = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/prod.runway_shows.txt', 'r').readlines()
    
    for y in range(0,2):
    	    
    	browser = BROWSERS[y]
    	    
    	for s in range(len(SHOWS)):
    	    show = SHOWS[s].strip('\n')
            filename = show.split('/')
            
            results = open('../../DATA/HTML/RUNWAY/OPENER/' + browser + '.' + filename[-1] + '.runwayshowopener.sel.html', 'wb')
            print "TESTING " + show
            suite = unittest.TestLoader().loadTestsFromTestCase(RunwayShowOpener)
            unittest.TextTestRunner(verbosity=2).run(suite)
            runner = HTMLTestRunner.HTMLTestRunner(stream=results, title=show, description='Results for Runway Show Opener on ' + ENV)
            runner.run(suite)
        
            s += 1
            
        y += 1
        
    x += 1
    
