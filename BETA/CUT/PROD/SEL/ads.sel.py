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


class Ads(unittest.TestCase):
    
    def setUp(self):
    
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        
        ########################################################################
        
    def test_(self):    
        
        self.driver = driver
        pass

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

if __name__ == '__main__':
	
    url = sys.argv[1]
    x = int(sys.argv[2])
    
    if x == 0:
    	ENV = 'stg'
    	BASEURL = 'http://stg.nymetro.com/'
    	
    elif x == 1:
    	ENV = 'ec2'
    	BASEURL = 'http://author.ec2.qa.nymetro.com/'
    	
    else:
    	ENV = 'prod'
    	BASEURL = 'http://nymag.com/'
    	
    suite = unittest.TestLoader().loadTestsFromTestCase(ArticleJson)
    unittest.TextTestRunner(verbosity=2).run(suite)
