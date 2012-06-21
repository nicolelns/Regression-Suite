import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
#import Logger
import vultureSoup

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

BASEURL = raw_input('Enter a BaseURL: ')
BROWSERS = ('chrome', 'firefox', 'ie')
TEST = "Vulture Search - Desktop - Prod"

#L = Logger.MainLogger(BASEURL, TEST)

SEARCH = ('romney', 'sunshine', '', '$#$#$', '2345', '30 Rock', '<tag>This is some mock HTML</tag>')

x = 0

"""
This is a test for the Search function on Vulture.  This test primarily checks output on the search results page, 
rather than how 'optimized' search is.

"""	

#########################################################################
#########################################################################

class Search(unittest.TestCase):

    def setUp(self):
    	    
        if x == 0:
            self.driver = webdriver.Chrome(chromedriver)
            
        elif x == 1:    
            self.driver = webdriver.Firefox() 
            
        elif x == 2:
    	    self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.INTERNETEXPLORER)
        
        #elif x == 3:
	    #self.driver = webdriver.Remote(desired_capabilities = {}, command_executor = "http://localhost:8080/wd/hub")
        
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
	print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
	
    def test_search(self):
    	    
    	driver = self.driver
    	driver.get(BASEURL)
    	test = "Test A - Search"
    	print test
    	
    	n = 0
    	
    	for each in SEARCH:
    		
    	    try:
    	    	driver.find_element_by_id('txt-ny-search').send_keys(SEARCH[n])
    	    	driver.find_element_by_id('sc-vulture').click()
    	    	
    	    except Exception, e:
            	print "FAIL, can't select search bar/vulture button", SEARCH[n], str(e)
            	#L.log(BROWSERS[x], test, "FAIL, CANNOT FILL IN SEARCH BAR", searchterms[n], exception=str(e))    
            		
            else:
            	#L.log(BROWSERS[x], test, "PASS, FILLING IN SEARCH BAR WORKS", searchterms[n])
    	    	driver.find_element_by_id('btn-ny-search').click()
    	    	time.sleep(10)
    	    	self.sort_search(SEARCH[n])
    	    	driver.get(BASEURL)
		
	    n += 1
    	    	    
        ########################################################################
   
    def sort_search(self, searchterm):
    	    
    	driver = self.driver
    	test = "Test B - Do the 'Sort By' Buttons Work?"
    	print test
    	
    	self.SEARCH = searchterm
    	
    	click = ('issuedate%7C1', 'issuedate2%7C0', 'nyml_type_srt%7C0', "Relevance%7C0")
    	n = 0
    	
    	v = self.verify_content()
    	
    	if v is not None:
    	
    	    for each in click:
    		
    	        url = "http://nymag.com/srch?t=sw&tx=" + self.SEARCH + "&N=272&No=0&fd=All&Ns=" + click[n]
    	
    	        try:
    	    	    driver.find_element_by_xpath("//a[@href='" + url + "']").click()
    	    
                except Exception as e:
    	            print "FAILURE", str(e), url
    	            #L.log(BROWSERS[x], test, "FAIL, CANNOT FILL IN SEARCH BAR", click[n], exception=str(e))
    	        
    	        else:
    	    	    time.sleep(3)
    	    	    # Add in something to close all pop-ups and replace time.sleep()
    	    	    self.verify_content()
    	    	    print "SORT SEARCH OK"
    	    
    	        n += 1
    	    
    	########################################################################
    	    
    def prev_next(self):
    	    
    	driver = self.driver
    	test = "Test C - Previous Next Buttons"
    	print test
    	
    	n = 0
    	
    	prevnext = ('nextActive', 'prevActive')
    	
    	for each in prevnext:
    		
    	    try:
    	    	driver.find_element_by_class_name(prevnext[n]).click()
    	    	self.verify_content()
    	    	
    	    except Exception as e:
    	        print "FAILURE", str(e), prevnext[n]
    	        
    	    else:
    	        print "OK"
    	        
    	    n += 1  
    
        ########################################################################
        
    def verify_content(self):
    	
    	driver = self.driver
    	search_page = driver.current_url
    	S = vultureSoup.Parser(search_page)
        DATA = S.search()
        
        if DATA is None:
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

for x in range(0,1):

    suite = unittest.TestLoader().loadTestsFromTestCase(Search)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
#L.save()
    		
    		
