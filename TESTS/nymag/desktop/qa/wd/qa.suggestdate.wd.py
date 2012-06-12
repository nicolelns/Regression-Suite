import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import subprocess
import pickle
import os
import Logger
import nymagSoup

BASEURL = 'http://dev.nymag.biz/'
BROWSERS = ('firefox', 'chrome', 'ie')     # Safari as subprocess
TEST = "Related Stories Module - QA - NYMag"

L = Logger.MainLogger(BASEURL, TEST)

S = nymagSoup.Parser(BASEURL)
S.suggest_date_pickler()

CSS = open('../data/text/qa.suggestdate.css.txt', 'r').readlines()
DATA = pickle.load(open('../data/pickle/qa.dateUrlList.data.p', 'rb'))

x = 0

"""
This is a test for the suggest a date module on all listings for nymag except restaurants

"""

#########################################################################
#########################################################################
	

class SuggestDate(unittest.TestCase):

    def setUp(self):
    	
    	self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        self.base_url = BASEURL
        self.verificationErrors = []
	print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
    
    def test_suggestdate(self):

    # Tests for the presence of elements in the module using CSS locators
    # This test is an 'assert' test: if any element is not present, the test fails
	
	n = m = 0
	driver = self.driver
        driver.get(self.base_url + DATA[m])
        
        # Loops through the data in the CSS file asserting each element is on the page
        
	for each in CSS:

	    c = CSS[n].strip('\n') 
        
            try:
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, c))
                
            except AssertionError, e:
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e) + c)
                L.log(BROWSERS[x], TEST, "FAIL, ELEMENT NOT FOUND", str(e) + c)
            
            else:
                L.log(BROWSERS[x], TEST, "PASS, ELEMENT FOUND", c)
                
            n += 1
            m += 1
            
        self.b_click_test()
            
    ############################################################################
        
    def b_click_test(self):
    	    
    	n = 0
	driver = self.driver
	test = "Test B - Click and Wait for Page"
	print test
        
        for each in DATA:
        	
            href = DATA[n]
            driver.get(BASEURL + href)
            
            try:
                driver.find_element_by_xpath("//a[@href='http://nymag.howaboutwe.com/?f=dating-listing']").click()
    	        time.sleep(2)
                
            except Exception as e:
                self.verificationErrors.append(str(e) + href)	
            	L.log(BROWSERS[x], test, "FAIL, LINK DOES NOT WORK", href, exception=str(e))  
        
            else:
            	L.log(BROWSERS[x], test, "PASS, LINK WORKS", href)
               
            n += 1
            
        ########################################################################
    
    def is_element_present(self, how, what):
    	    
        try: 
            self.driver.find_element(by=how, value=what)
        
        except NoSuchElementException, e: 
            return False
        
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for x in range(0,1):

    suite = unittest.TestLoader().loadTestsFromTestCase(SuggestDate)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
