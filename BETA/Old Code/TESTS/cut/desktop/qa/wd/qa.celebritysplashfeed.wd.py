#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import pickle
import Logger
import cutSoup

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

BASEURL = 'http://ec2.qa.nymetro.com/thecut/celebrity/'
BROWSERS = ('chrome', 'firefox', 'ie')
TEST = "Celebrity Splash Page - QA - The Cut"

L = Logger.MainLogger(BASEURL, TEST)

S = cutSoup.Parser(BASEURL)
S.qa_celebrity_splash_feed()

CSS = open('../data/text/qa.celebritysplash.css.txt', 'r').readlines()
FEED_DATA = pickle.load(open('../data/pickle/qa.celebritysplashfeed.data.p', 'rb'))

feed_keys = FEED_DATA.keys()
feed_values = FEED_DATA.values()
x = 0

"""
This is a test for the Cut Celebrity Splash Pages:

Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  

The DATA file is a pickle file generated by vultureSoup.Parser(), customized for this module.

IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!
"""	

#########################################################################
#########################################################################

class CelebritySplash(unittest.TestCase):
	
    def setUp(self):
    	    
        if x == 0:
            self.driver = webdriver.Chrome(chromedriver)
            
        elif x == 1:    
            self.driver = webdriver.Firefox()
            
        elif x == 2:
    	    self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.INTERNETEXPLORER)
            
        self.driver.implicitly_wait(60)
        self.base_url = BASEURL
        self.verificationErrors = []
        print "TESTING ec2.qa.nymetro.com/thecut/ in " + BROWSERS[x]
    
    def test_a(self):
    	    
        """ 
        Tests for the presence of elements in the module using CSS locators.  The CSS file contains the locators.
        This test is an 'assert' test: if any element is not present, the test fails
        """
        
        n = 0
        driver = self.driver
        driver.get(BASEURL)
        
        for each in CSS:
        	
            c = CSS[n].strip('\n')
        	
            try: 
            	self.assertTrue(self.is_element_present(By.CSS_SELECTOR, c))
        
            except AssertionError as e: 
            	self.verificationErrors.append(str(e))
            	print "FAILURE"
            	L.log(str(BROWSERS[x]), "Test A - Presence", "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            	
            else:
                L.log(str(BROWSERS[x]), "Test A - Presence", "PASS, ELEMENT FOUND", c)
                
            n += 1
            
        self.b()
        self.c()
        self.d()
        #self.e()
        
        ########################################################################
        
    def b(self):
    	    
        # Tests for the correct content within the module
        # This is a 'verify' test, it will not fail the whole test if one item fails
    	 
	driver = self.driver
        
        images = len(driver.find_elements_by_css_selector(CSS[3]))
        timestamp = len(driver.find_elements_by_css_selector(CSS[4]))
	comments = len(driver.find_elements_by_css_selector(CSS[5]))
        headers = len(driver.find_elements_by_css_selector(CSS[6]))
	paragraphs = len(driver.find_elements_by_css_selector(CSS[7]))
        
	driver.find_element_by_css_selector(CSS[7]).click()
	time.sleep(2)
	
	images2 = len(driver.find_elements_by_css_selector(CSS[3])) - images
	timestamp2 = len(driver.find_elements_by_css_selector(CSS[4])) - timestamp
	comments2 = len(driver.find_elements_by_css_selector(CSS[5])) - comments
        headers2 = len(driver.find_elements_by_css_selector(CSS[6])) - headers
        paragraphs2 = len(driver.find_elements_by_css_selector(CSS[7])) - paragraphs
        
        if ((images2 < 5) or (timestamp2 < 5) or (comments2 < 5) or (headers2 < 5) or (paragraphs2 < 5)):
            print "Missing articles!"
            L.log(BROWSERS[x], "Test B - Presence", "FAIL, MISSING CONTENT AFTER CLICKING LOAD MORE", "Images: " + str(images2) + " Timestamp: " + str(timestamp2) + " Comments: " + str(comments2) + " Headers: " + str(headers2) + " Paragraphs: " + str(paragraphs2)) 
        
	########################################################################
	
    def c(self):
     	     
        m = n = r = 0    
        driver = self.driver
        time_list = []
        webdriver_time_list = []
        
	for each in feed_keys:
        
            blah = feed_values[m]
            json_time = blah[1]
            if json_time not in time_list:
                time_list.append(json_time)
           
	    m += 1
	    
	try:
            foo = driver.find_elements_by_class_name("metaTime")
            	
    	except Exception, e:
    	    print "TIMESTAMP FAIL", str(e)
    	    L.log(BROWSERS[x], "Test B - Presence", "FAIL, CANNOT FIND TIMESTAMPS FOR ARTICLES", str(len(time_list)), exception=str(e))
        
	else:
	    L.log(BROWSERS[x], "Test B - Presence", "PASS, TIMESTAMPS FOUND", str(len(time_list)))
	    
	for each in foo:
		
	    foo2 = foo[r].text
	    webdriver_time_list.append(foo2)
	    r += 1
	    	    
	for each in time_list:
	
	    if time_list[n] in webdriver_time_list:
	    	    
	    	time_list.pop(n)
	    	
	    n += 1
    	
	try:
	    self.assertEqual([], time_list)
		
        except AssertionError, e:
            print "FAIL", len(time_list)
            
        else:
	    print "PASS"
	    
        ########################################################################
        
    def d(self):
    	   
        driver = self.driver
        m = 0
        
        for each in feed_keys:
        	
            data = feed_values[m]
            image = data[0]
            
            if image is not None:
            	
		    for w in range(0,3):
		    	    
			if w == 0:
		            driver.manage.window.set_position(0,0)
		            driver.manage.window.set_size(1920,1080)
			    test = driver.find_element_by_xpath("//img[@src='" + image + "']").size
			    print test
				
			    """	
			    sel.window_maximize()
			    desktop_height = sel.get_element_height("//img[@src='" + image + "']")
			    desktop_width = sel.get_element_width("//img[@src='" + image + "']")
			    desktop_paragraph_loc = sel.get_element_position_left("//p[@class='excerpt']")
			    desktop_title_loc = sel.get_element_position_left("//a[@href='" + feed_keys[m].strip("^^") + "']")
			  
			elif w == 1:
			    sel.get_eval("window.resizeTo(728, 1000);")
			    tablet_height = sel.get_element_height("//img[@src='" + image + "']")
			    tablet_width = width = sel.get_element_width("//img[@src='" + image + "']")
			    tablet_paragraph_loc = sel.get_element_position_left("//p[@class='excerpt']")
			    tablet_title_loc = sel.get_element_position_left("//a[@href='" + feed_keys[m].strip("^^") + "']")
			
			elif w == 2:
			    sel.get_eval("window.resizeTo(420, 600);")
			    mobile_height = sel.get_element_height("//img[@src='" + image + "']")
			    mobile_width = sel.get_element_width("//img[@src='" + image + "']")
			    mobile_paragraph_loc = sel.get_element_position_left("//p[@class='excerpt']")
			    mobile_title_loc = sel.get_element_position_left("//a[@href='" + feed_keys[m].strip("^^") + "']")
			   """    
			w += 1
                
            if ((desktop_height >= tablet_height) and (desktop_height >= mobile_height) and (tablet_height >= mobile_height)):
                print "Resize images okay"
                
            else:
            	print "Resize images fails!", feed_keys[m]
                    
            if ((desktop_paragraph_loc >= tablet_paragraph_loc) and (desktop_paragraph_loc >= mobile_paragraph_loc) and (tablet_paragraph_loc >= mobile_paragraph_loc)):
                print "Resize paragraphs/excerpts okay", mobile_paragraph_loc, tablet_paragraph_loc, desktop_paragraph_loc
                
            else:
            	print "Resize paragraphs/excerpts fails!", feed_keys[m], mobile_paragraph_loc, tablet_paragraph_loc, desktop_paragraph_loc
                
            if ((desktop_title_loc >= tablet_title_loc) and (desktop_title_loc >= mobile_title_loc) and (tablet_title_loc >= mobile_title_loc)):
                print "Resize article titles okay"
                
            else:
            	print "Resize articles fails!", feed_keys[m]
            m += 1
            
    	########################################################################
        
    def e(self):
    	    
    	m = n = 0    
        driver = self.driver
        driver.get(self.base_url)
        wait = driver.implicitly_wait(20)
        
        for each in feed_keys:
        	
            href = feed_keys[m]
            href = href.strip('^^')
            print href, "feed link"
            
            try:
    	        driver.find_element_by_xpath("//a[@href='" + href + "']").click()
    	        wait
        
            except Exception as e:
                self.verificationErrors.append(str(e))
                print href + " not found"
            	L.log(str(BROWSERS[x]), "Test C - Function - Feed", "FAIL, LINK DOES NOT WORK", href)  
        
            else:
                driver.back()
                wait
                L.log(str(BROWSERS[x]), "Test C - Function - Feed", "PASS, LINK WORKS", href)
                
            if feed_values[m] is not None:
            	  
            	data = feed_values[m]  
            	img = data
            	print img, 'feed img'
            	  
                try:
    	            driver.find_element_by_xpath("//img[@src='" + img + "']").click()
    	            wait
        
                except Exception as e:
                    self.verificationErrors.append(str(e))
                    print img + " not found"
            	    L.log(str(BROWSERS[x]), "Test C - Function - Feed", "FAIL, IMAGE DOES NOT LOAD", img)  
        
                else:
                    driver.back()
                    wait
                    L.log(str(BROWSERS[x]), "Test C - Function - Feed", "PASS, IMAGE LOADS", img)
                
            m += 1
            
        for each in lede_keys:
        	
            href = lede_keys[n]
            href = href.strip('^^')
            print href, 'lede link'
            
            try:
    	        driver.find_element_by_xpath("//a[@href='" + href + "']").click()
    	        wait
        
            except Exception as e:
                self.verificationErrors.append(str(e))
                print href + " not found"
            	L.log(str(BROWSERS[x]), "Test C - Function - Feed", "FAIL, LINK DOES NOT WORK", href)  
        
            else:
                driver.back()
                wait
                L.log(str(BROWSERS[x]), "Test C - Function - Feed", "PASS, LINK WORKS", href)
                
            if lede_values[m] is not None:
            	    
            	data = lede_values[m]  
            	img = data  
            	print data, 'lede img'
            	    
                try:
    	            driver.find_element_by_xpath("//img[@src='" + img + "']").click()
    	            wait
        
                except Exception as e:
                    self.verificationErrors.append(str(e))
                    print img + " not found"
            	    L.log(str(BROWSERS[x]), "Test C - Function - Feed", "FAIL, IMAGE DOES NOT LOAD", img)  
        
                else:
                    driver.back()
                    wait
                    L.log(str(BROWSERS[x]), "Test C - Function - Feed", "PASS, IMAGE LOADS", img)
                
            n += 1
            
        driver.find_element_by_xpath("/html/body/div/div/div[4]/div/section/nav/a").click()
        wait
        articles = driver.get_css_count('css=' + CSS[3])
        images = driver.get_css_count('css=' + CSS[6])
        paragraphs = driver.get_css_count('css=' + CSS[7])
        
        print articles
        print images
        print paragraphs
    
            
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

for x in range(1,2):

    suite = unittest.TestLoader().loadTestsFromTestCase(CelebritySplash)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()

