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

class RunwayShow(unittest.TestCase):

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
        
        print "TESTING " + show + " in " + BROWSERS[y]
        print TEST
        
	########################################################################
    @unittest.skip("Needs debugging")
    def test_num_imgs(self):
    	    
    	driver = self.driver
    	driver.find_element_by_xpath("//a[contains(text(),'View the Collection')]").click()
    	
    	num1 = driver.find_element_by_xpath('/html/body/section[2]/footer[2]/div/span/span[3]').text
    	num = driver.find_element_by_css_selector('div.ssPhotoMeta span.ssCount span.ssTotal').text
    	
    	self.driver.find_element_by_xpath("/html/body/section[2]/footer[2]/nav/a[2]").click()
    	count = driver.find_elements_by_xpath('/html/body/section[2]/div/ul/li')
    	
    	self.assertEqual(str(num), str(len(count)))
    	
    	########################################################################
    
    def test_close_show(self):
    	    
    	driver = self.driver
    	driver.find_element_by_xpath("//a[contains(text(),'View the Collection')]").click()
    	
	for i in range(60):
            try:
                driver.find_element_by_xpath("/html/body/section[2]/header/a").click() 
                break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
    	
        ########################################################################
    	    
    def test_view_slides(self):
    	    
    	driver = self.driver
    	driver.find_element_by_xpath("//a[contains(text(),'View the Collection')]").click()
    	
    	for r in range(0,7):
    	
    	    self.assertTrue(self.is_element_present(By.CSS_SELECTOR, 'div.ssPhotoMainviewWrap div img.ssPhoto'))
            driver.find_element_by_css_selector("footer.ssFooter nav.ssNav a.ssNext").click()
            r += 1
            
        for l in range(0,7):
    	
    	    self.assertTrue(self.is_element_present(By.CSS_SELECTOR, 'div.ssPhotoMainviewWrap div img.ssPhoto'))
            driver.find_element_by_css_selector("footer.ssFooter nav.ssNav a.ssPrev").click()
            l += 1
    
        ########################################################################
        
    def test_hit_miss(self):
    	
    	driver = self.driver
    	driver.find_element_by_xpath("//a[contains(text(),'View the Collection')]").click()
    	    
    	driver.find_element_by_css_selector("div.ssHitMiss > a.hit").click() 
    	self.assertTrue(self.is_element_present(By.CSS_SELECTOR, " div.ssHitMiss div.ssHitMissInfo span.ssHitMissCount"))
        driver.find_element_by_css_selector("footer.ssFooter > nav.ssNav > a.ssPrev").click()
        driver.find_element_by_css_selector("div.ssHitMiss > a.miss").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, " div.ssHitMiss div.ssHitMissInfo span.ssHitMissCount"))
        
        ########################################################################
        
    def test_ads(self):
    	
    	driver = self.driver
    	driver.find_element_by_xpath("//a[contains(text(),'View the Collection')]").click()
    	     
    	self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "section#ss-ad.ssAd"))
        
        ########################################################################
       
    def test_zoom(self):
    	    
    	IMG = "'http://pixel.nymag.com/imgs/" + show[:-5] + "/collection-full-length/1.o.jpg/a_5x.jpg'"
    	
    	driver = self.driver
    	
    	driver.find_element_by_xpath("//a[contains(text(),'View the Collection')]").click()
    	old_size = driver.find_element_by_xpath('/html/body/section[2]/div[2]/div/ul/li/div/div[2]/img').size
    	
    	for i in range(60):
            try:
                driver.find_element_by_xpath("/html/body/section[2]/div[2]/div/ul/li/div/div[2]/span").click()
                break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        
	for p in range(0,4):
    	    driver.find_element_by_xpath("//div[@id='lightbox']/div/div/a[2]").click()
    	    p += 1
    	
    	for p in range(0,4):
    	    driver.find_element_by_xpath("//div[@id='lightbox']/div/div/a[3]/div[2]").click()
    	    p += 1
    	    
    	new_size = driver.find_element_by_xpath('//img[contains(@src,' + IMG + ")]").size
        
        self.assertTrue(old_size['width'] < new_size['width'])
        self.assertTrue(old_size['height'] < new_size['height'])
        
        driver.find_element_by_xpath("//div[@id='lightbox']/div/div/a[2]/div[2]").click()
        
        ########################################################################
    
    def test_show_name(self):
    	
    	driver = self.driver
    	
    	driver.find_element_by_xpath("//a[contains(text(),'View the Collection')]").click()
    	
    	self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.ssTabletMetaWrap > h1.ssSlideshowTitle"))
    	
    	########################################################################
   	
    def test_photo_credit(self):
    	
    	driver = self.driver
    	driver.find_element_by_xpath("//a[contains(text(),'View the Collection')]").click()
    	
    	self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "dl.ssDictionary dt"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "dl.ssDictionary dd"))
        
        ########################################################################
    
    def test_collection_finder(self):
    	
    	driver = self.driver
    	driver.find_element_by_xpath("//a[contains(text(),'View the Collection')]").click()
    	
    	for i in range(60):
    	    try:
    	        driver.is_element_present(By.XPATH, "/html/body/section[2]/footer[2]/div[2]/h3[2]/a")
    	        break
            except:
                pass
            time.sleep(1)
            
        else:
    	    self.fail("time out")
    	    	
    	driver.find_element_by_xpath("/html/body/section[2]/footer[2]/div[2]/h3[2]/a").click()
    	self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "ol#showfinder_seasons.showFinderList li.showFinderListItem"))  
    	self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "ol#showfinder_cities.showFinderList li.showFinderListItem"))
    	self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "ol#showfinder_labels.showFinderList li.showFinderListItem"))
    	driver.find_elements_by_xpath("//div[@id='lightbox']/section/div/div/span")
    	
        ########################################################################
    
    def clickable(self, element):
    	    
        if element.is_clickable():
            return element
        return null

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
	SHOWS = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/stg.runway_shows.txt', 'r').readlines()	
    
    elif x == 1:
    	ENV = 'ec2'
        SHOWS = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/ec2.runway_shows.txt', 'r').readlines()
        
    else:
    	ENV = 'prod'
    	SHOWS = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/prod.runway_shows.txt', 'r').readlines()
    
    for y in range(0,2):
    	    
    	browser = BROWSERS[y]
    	    
    	for s in range(len(SHOWS)):
    	    show = SHOWS[s].strip('\n')
    	    filename = show.split('/')
    	    
            results = open('../../DATA/HTML/RUNWAY/SHOWS/' + browser + '.' + filename[-1] + '.runwayshow.sel.html', 'wb')
            print "TESTING " + show
            suite = unittest.TestLoader().loadTestsFromTestCase(RunwayShow)
            unittest.TextTestRunner(verbosity=2).run(suite)
            runner = HTMLTestRunner.HTMLTestRunner(stream=results, title=show, description='Results for Runway Show on ' + ENV)
            runner.run(suite)
        
            s += 1
            
        y += 1
        
    x += 1
    
