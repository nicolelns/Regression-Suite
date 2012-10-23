#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re
import string
import urllib
import urllib2
import unittest
import time
import json
import pickle
import socket
#from bs4 import BeautifulSoup


reload(sys)
sys.setdefaultencoding("utf-8")


#URL = 'http://author.nymetro.com/'
QUERY = pickle.load(open('/Users/nsmith/Desktop/BETA/CUT/DATA/PICKLE/query.p', 'rb'))


class MyOpener(urllib.FancyURLopener):
	
    # Used with the old login version, ignore for now
    
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'
    
    #########################################################################
    #########################################################################
    

class JSONParserPublish(unittest.TestCase):
	
    def setUp(self):
        
        timeout = 10
        socket.setdefaulttimeout(timeout)
        
        # Set up authorization in header and open page
        # request.add_header()'s second arg is the usr/pwd in base64
        
        request = urllib2.Request(QUERY)
        request.add_header("Authorization", "Basic bnNtaXRoOkd1YW53dWs1")   
        self.result = urllib2.urlopen(request)
        
    #########################################################################
    
    def test_login(self):
    	
    	# Open a file and write the JSON data (result) to the file
    	
        d = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/s.txt', 'w')
        d.write(self.result.read())
        d.close()
        
    #########################################################################    
    @unittest.skip("Old Login via Selenium Webdriver - DEPRECATED")
    def test_old_login(self):
           
    	# Log in to CQ:
    	# Change the empty strings in send_keys() to a username/password 
    	# to configure login credentials until a config file is set up
    
        driver = self.driver
        
        driver.get(URL)
               
        try:
            driver.find_element_by_id("input-username").clear()
            driver.find_element_by_id("input-username").send_keys("")
            driver.find_element_by_id("input-password").clear()
            driver.find_element_by_id("input-password").send_keys("")
            driver.find_element_by_id("input-submit").click()
            
        except AssertionError, e:
            print "FAILURE TO LOGIN", str(e)
            
        else:
            driver.get(QUERY)	
            self.data = self.scrape(self.get_src())
            d = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/s.txt', 'w')
            d.write(self.data)
            d.close()
         
        ########################################################################
        
    def get_src(self):
    	    
    	# Old functionality, used in the Webdriver login version
    	    
    	return self.driver.page_source
        
        ########################################################################
        
    def scrape(self, page):
    	 
    	# Old functionality, used in the Webdriver login version 
    	 
    	self.page = page
        self.soup = BeautifulSoup(self.page)
        return self.soup('pre')[0].string
    
        ########################################################################
    
    def tearDown(self):
    	    
    	# Uncomment below to use this code with the old Webdriver backed login
    	
    	#self.driver.quit()
    	pass
    	
    #########################################################################
    #########################################################################
    
if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(JSONParserPublish)
    unittest.TextTestRunner(verbosity=2).run(suite)
