#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import urllib
import urlparse
import sys
import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")


class ArticleJson(unittest.TestCase):
    
    def setUp(self):
    
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        
        ########################################################################
    	
    def test_login(self):
        
        # Log in to CQ:
    	
        driver = self.driver
        driver.get(AUTHOR)
         
        try:
            driver.find_element_by_id("input-username").clear()
            driver.find_element_by_id("input-username").send_keys(USR)
            driver.find_element_by_id("input-password").clear()
            driver.find_element_by_id("input-password").send_keys(PWD)
            driver.find_element_by_id("input-submit").click()
            
        except AssertionError, e:
            print "FAILURE TO LOGIN", str(e)
            
        else:
            driver.get(self.query_url_maker())	
            self.scrape(self.get_src())
            
        ########################################################################
        
    def get_src(self):
    	    
    	driver = self.driver
    	src = driver.page_source
        return src
        
        ########################################################################
        
    def scrape(self, page):
    	 
    	self.page = page 
        self.soup = BeautifulSoup(self.page)
        self.spam = self.soup.find_all
        
        try:
            json_data = self.soup('pre')[0]
        except IndexError:
            D[str(URL)] = None
        else:
            D[str(URL)] = str(json_data)[5:-6]
        
	########################################################################
	
    def query_url_maker(self):
    	
    	l = URL.split('/')
    	ll = l[-1]
    	# Re-do this string concatenation.  Don't yo-yo
    	new_url = AUTHOR + CONTENT + l[-3] + '/' + l[-2] + '/' + ll[:-5] + '/jcr:content.json'
    	return str(new_url)
    	
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


class Configure():
	
    def __init__(self, author, usr, pwd):    
    	 
    	self.author = author 
    	self.usr = usr
    	self.pwd = pwd
    	
    	# I hate globals, better way to do this?
        global USR 
        USR = self.usr
    	global PWD
    	PWD = self.pwd
    	global AUTHOR
    	AUTHOR = self.author
    	
#########################################################################
#########################################################################
    
    
class Run():
	
    def __init__(self, _list):
    	
        for url in _list:
            # Re-do, globals are bad.
            global CONTENT	
            CONTENT = self.blog_converter(url)
            global URL
            URL = url
            
    	    suite = unittest.TestLoader().loadTestsFromTestCase(ArticleJson)
    	    unittest.TextTestRunner(verbosity=2).run(suite)
  
    #########################################################################  
    
    def blog_converter(self, url):
    	
    	self.url = url
    	
    	if re.search('vulture', self.url, re.I):
    	    return 'content/nymag/daily/entertainment/'
    	    
        elif re.search('intel', self.url, re.I):
            return 'content/nymag/daily/intel/'
            
        elif re.search('thecut', self.url, re.I):
            return 'content/nymag/daily/fashion/'
    	 
#########################################################################
#########################################################################

D = {}

if __name__ == '__main__':
	
    D = {}

