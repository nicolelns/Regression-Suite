#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
#import cutSoup

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


BASEURL = raw_input("Enter a BaseUrl: ")
BROWSERS = ('chrome', 'firefox', 'ie')
TEST = "The Cut - Article Migration"

#S = cutSoup.Parser(BASEURL)

#CSS = open('../data/text/interview.css.txt', 'r').readlines()
#DATA = S.interview()

#keys = DATA.keys()
#values = DATA.values()

x = 0				# Browser counter
#v = 0				# Window size counter (desktop = 0, tablet = 1, mobile = 2)


#########################################################################
#########################################################################

class Article(unittest.TestCase):

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
	
    def test_desktop(self):
        
	n = 0
        driver = self.driver
        driver.get(BASEURL)
        
        driver.set_window_size(1200,1200)
        
        self.partners(0)
        self.ads(0)
        self.click_next_arrows()
        #self.float_arrows(0)
        
    	########################################################################
    	
    def test_tablet(self):
    	    
    	n = 0
        driver = self.driver
        driver.get(BASEURL)
        
        driver.set_window_size(720,720)
        
        self.partners(1)
        self.ads(1)
        self.click_next_arrows()
        #self.float_arrows(1)
    	    
    	########################################################################
    	
    def test_mobile(self):
    	    
    	n = 0
        driver = self.driver
        driver.get(BASEURL)
        
        driver.set_window_size(320,320)
        
        self.partners(2)		# Is the partners module supposed to be on mobile?
        self.ads(2)
        self.click_next_arrows()
        #self.float_arrows(2)
    	    
    	########################################################################	
    	
    def partners(self, num):
    	    
    	driver = self.driver
    	v = num
    	test = "Test A - Partners Module"
    	print test
    	
    	if v == 0:	# Desktop
    	
    	    try:
    	        self.failUnless(driver.find_element_by_xpath("//div[@id='nym-partners']"))
    	        
    	    except NoSuchElementException, e:
    	    	driver.get_screenshot_as_file('../screenshots/d.' + test + '.' + BASEURL + '.png')
    	    	print str(e)
    	    	
    	elif v == 1:	# Tablet
    		
    	    try:
    	    	self.failUnless(driver.find_element_by_xpath("//div[@id='nym-partners']"))
    	        
    	    except NoSuchElementException, e:
    	    	driver.get_screenshot_as_file('../screenshots/t.' + test + '.' + BASEURL + '.png')
    	    	print str(e)
    	    	
    	else:		# Mobile
    		
    	    try:
    	    	self.failIf(driver.find_element_by_xpath("//div[@id='nym-partners']"))
    	        
    	    except NoSuchElementException, e:
    	    	driver.get_screenshot_as_file('../screenshots/m.' + test + '.' + BASEURL + '.png')
    	    	print str(e)
    	    	
    	
    	########################################################################
    	
    def ads(self, num):
    	    
    	driver = self.driver
    	v = num
    	test = "Test B - Ads"
    	print test
    	
    	a = b = c = True
    	
    	if v == 0:
    		
    	    try:
    	    	a = self.failUnless(driver.find_element_by_xpath("//div[@id='leaderboard-desktop']"))
    	    	b = self.failUnless(driver.find_element_by_xpath("//div[@id='secondary-flex']"))	
    	    	c = self.failUnless(driver.find_element_by_xpath("//div[@id='footer-tablet-desktop']"))
    	    		
    	    except NoSuchElementException, e:
    	    	print "DESKTOP FAIL", str(e), str(a) + " Leaderboard", str(b) + " Flex", str(c) + " Footer"
    	    	driver.get_screenshot_as_file('/Users/nsmith/Regression-Suite/TESTS/cut/desktop/qa/screenshots/d.' + test + '.' + BASEURL + '.png')

	elif v == 1:
    	
    	    try:
    	    	a = self.failUnless(driver.find_element_by_xpath("//div[@id='leaderboard-tablet']"))
    	    	b = self.failUnless(driver.find_element_by_xpath("//div[@id='secondary-flex']"))	
    	    	c = self.failUnless(driver.find_element_by_xpath("//div[@id='footer-tablet-desktop']"))
    	    		
    	    except NoSuchElementException, e:
    	    	print "TABLET FAIL", str(e), str(a) + " Leaderboard", str(b) + " Flex", str(c) + " Footer" 
    	    	
    	else:
    	
    	    try:
    	    	a = self.failUnless(driver.find_element_by_xpath("//div[@id='leaderboard-mobile']"))
    	    	b = self.failUnless(driver.find_element_by_xpath("//div[@id='secondary-flex']"))	
    	    	c = self.failUnless(driver.find_element_by_xpath("//div[@id='footer-mobile']"))
    	    		
    	    except NoSuchElementException, e:
    	    	print "MOBILE FAIL", str(e), str(a) + " Leaderboard", str(b) + " Flex", str(c) + " Footer" 
    	    	
    	########################################################################
    	
    def float_arrows(self, num):
    	    
        driver = self.driver
        v = num
        test = "Test C - Floating Nav Arrows"
        print test
        
        if v != 2:
    		
    	    try:
    	    	self.failUnless(driver.find_element_by_xpath("//nav[@class='entryNext rightArticleArrow']"))
    	    	self.failUnless(driver.find_element_by_xpath("//nav[@class='entryPrev leftArticleArrow']"))	
    	    		
    	    except AssertionError, e:
    	    	print "FAIL"
    	   
    	########################################################################
    	
    def click_next_arrows(self):
    	    
    	driver = self.driver
    	test = "Test K - Click Arrows to Go to Next/Prev Article"
    	print test

    	try:
    	    #self.hover("html.js body#nymag.fashion div#wrap-wrap-wrap div#wrap-wrap div#wrap div#content div.contentPrimary article#entry-116096.entry header.primaryHeader nav.entryNext")
    	    driver.find_element_by_xpath("//article[@id='entry-116096']/header/nav[3]/a").click()	# Top Next Arrow
    	    	
    	except NoSuchElementException, e:
    	    print "FAIL", str(e)
    	    
        else:
            f = driver.current_url
            #driver.back()	# Un comment when back button works
            driver.get(BASEURL)
            
            try:
            	driver.find_element_by_xpath("//div[@id='content']/div/div/nav[3]/a/span/i").click()	# Bottom Next Arrow
            	
            except NoSuchElementException, e:
    	        print "FAIL", str(e)
    	    
            else:
                g = driver.current_url
                #driver.back()	# Un comment when back button works
                driver.get(BASEURL)
                
                try:
    	            self.assertEqual(f, g)   
    	           
    	        except AssertionError, e:
    	       	   print "URLS NOT EQUAL", f, g
    	       	   
    	   	else:
    	   	    print "URLS MATCH!  YAY!", f, g
    	   
    	########################################################################
    	
    def static_arrows(self):
    	    
    	driver = self.driver
    	test = "Test D - Static Arrows Under Article"
    	print test
    	
    	if v == 0:
    		
    	    try:
    	    	self.failUnless(driver.find_element_by_xpath("//nav[@class='entryNext rightArticleArrow']"))
    	    	self.failUnless(driver.find_element_by_xpath("//nav[@class='entryPrev leftArticleArrow']"))	
    	    		
    	    except AssertionError, e:
    	    	print "FAIL"
    	    	
    	    	# Get URL
    	
    	########################################################################
    	
    def all_news(self):
    	    
    	driver = self.driver
    	test = "Test E - All News Button"
    	print test
    	
    	if v != 2:
    		
    	    try:
    	    	self.failUnless(driver.find_element_by_xpath("//a[@class='newsLink']")).click()
    	    	t = driver.title
    	    	
    	    except AssertionError, e:
    	    	print "FAIL"
    	    	
    	    else:
    	    	self.assertEqual(t, "Articles News Feed")
    	    	
    	else:
    	    
    	    try:
    	    	self.failIf(driver.find_element_by_xpath("//a[@class='newsLink']")).click()
    	    	
    	    except AssertionError, e:
    	    	print "FAIL"
    		
    	########################################################################
    	
    def tags(self):
    	    
    	driver = self.driver
    	test = "Test F - Tags"
    	print test
    	
    	re = re.compile('read all posts tagged ' + '.*?')
    	
    	try:
    	    driver.find_elements_by_css_selector('css=a[title="' + re + "']")
    	    
        except Exception, e:
            print "FAIL"
            
        ######################################################################## 
        
    def byline(self):
    	    
    	driver = self.driver
    	test = "Test G - Byline"
    	print test
    	
    	try:
    	    self.failUnless(driver.find_elements_by_xpath("//cite/a")).click()
    	    
        except AssertionError, e:
            print "FAIL"
            
        ########################################################################
        
    def headline(self):
    	    
    	driver = self.driver
    	test = "Test H - Headline"
    	print test
    	
    	try:
    	    driver.find_element_by_xpath("//title")
    	    
        except Exception, e:
            print "FAIL"
            
        # if len(title) <> some condition:
            # print "not using long headline
            
        ########################################################################
        
    def pubdate(self):
    	    
    	driver = self.driver
    	test = "Test I - Publish Date"
    	print test
    	
    	try:
    	    driver.find_element_by_xpath("li[@class='first']")
    	    
        except Exception, e:
            print "FAIL"
    	
    	########################################################################
    	
    def comments(self):
    	    
    	driver = self.driver
    	test = "Test J - Comments"
    	print test
    	
    	########################################################################
    	
    def hover(self, element):
    	    
    	driver = self.driver
    	self.element = element		# Pass this function css
    	
    	mouse = webdriver.ActionChains(driver)
    	element = driver.find_element_by_css_selector(element)
        mouse.move_to_element(element).click_and_hold(element).perform()
        mouse.release(element)   
    	    
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

for x in range(1,2):
	
    suite = unittest.TestLoader().loadTestsFromTestCase(Article)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1

