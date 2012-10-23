#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re
import pickle
import string
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import wait
#import HTMLTestRunner
import urllib2


reload(sys)
sys.setdefaultencoding("utf-8")

RESULTS = open('/Users/nsmith/Desktop/RUNWAYMIGRATION/results.txt', 'a')
TAGGED = open('/Users/nsmith/Desktop/RUNWAYMIGRATION/untaggedshows.txt', 'a')
PUBLISHED = open('/Users/nsmith/Desktop/RUNWAYMIGRATION/dupedunpublishedshows.txt', 'a')

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


DATA = pickle.load(open('/Users/nsmith/Desktop/BETA/CUT/DATA/PICKLE/showdict.p', 'rb'))
URL = pickle.load(open('/Users/nsmith/Desktop/BETA/CUT/DATA/PICKLE/url.p', 'rb'))


class ShowMigration(unittest.TestCase):
	
    def setUp(self):
    	
        self.verificationErrors = []
            
    	self.data = DATA.values()[0]
    	self.basic_info = self.data[0].values()
    	self.tag_status = self.data[1].values()
    	self.image_srcs = self.data[2].values()
    	self.applied_srcs = self.data[3].values()
    	self.gallery = self.data[4].values()
    	self.title = self.data[5].values()
    	self.videos = self.data[6].values()
    	self.page_activation = self.data[7].values()
    	self.slideshow_activation = self.data[8].values()
    	self.offset_coords = self.data[10].values()
    	self.beauty_notes = self.data[11].values()
    	self.crit_reaction = self.data[12].values()
    	self.standout_accessories = self.data[13].values()
    	self.trends = self.data[14].values()
    	self.after_party = self.data[15].values()
    	self.show_name = self.data[16].values()
    	
    	self.t = self.tag_status[0]
    	self.t1 = self.t[0]
    	
    	self.tagged = self.t1['tagged']
    	self.untagged = self.t1['untagged']
    	self.total = self.t1['total'] 
    	
    	if self.published() is not False:
    		
    	    if y == 0:
                self.driver = webdriver.Chrome(chromedriver)
            
            elif y == 1:    
                self.driver = webdriver.Firefox() 
            
            elif y == 2:
    	        self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.INTERNETEXPLORER)
        
            #elif y == 3:
	        #self.driver = webdriver.Remote(desired_capabilities = {}, command_executor = "http://localhost:8080/wd/hub")
        
            self.driver.implicitly_wait(10)
            self.wait = wait.WebDriverWait(self.driver, 7)
            
        else:
            self.driver = None
        
        #print "TESTING " + URL + " in " + "FIREFOX"
        
        ########################################################################
       
    def test_tags(self):
    	
    	self.assertEqual(self.tagged + self.untagged, self.total)
    	
        try:  
            self.assertNotEqual(self.tagged, 0)
            
        except AssertionError:
            TAGGED.write(URL + " has no image tags")
            TAGGED.write('\n')
            self.verificationErrors.append(URL + " has no image tags")
    	    
        ########################################################################
    @unittest.skip("Develop later")
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
    @unittest.skip("Develop later")	
    def test_runway(self):
    
        driver = self.driver
        
        driver.find_element_by_xpath("(//a[contains(@href, '/thecut/runway/')])[2]").click()
        time.sleep(2)
        url = str(driver.current_url)
        
        self.assertEqual(url, 'http://nymag.com/thecut/runway/')
    
        ########################################################################
        
    @unittest.skipIf('self.videos == [[]]', 'No Video/Not developed')
    def test_videos(self):
    	pass    
    	#driver = self.driver
    	
    	#driver.find_element_by_css_selector('ul li a.contentOpenerSlideshowLink').click()
    	#self.failUnless(driver.find_element_by_css_selector('div#mvp_overlay_mvp_media_player_insertion_854839645'))
    @unittest.skip("Develop later")	 
    def test_fashion(self):
    	  
        driver = self.driver
        
        driver.find_element_by_xpath("(//a[contains(@href, '/thecut/fashion/')])[2]").click()
        time.sleep(2)
        url = str(driver.current_url)
        
        self.assertEqual(url, 'http://nymag.com/thecut/fashion/')	  
    	  
    	########################################################################  
    @unittest.skip("Broken - needs debugging")  
    def test_list_finder(self):
    	
    	driver = self.driver
    	
    	driver.find_element_by_css_selector("span.breadCrumbs a.breadCrumbsLink").click()
    	time.sleep(1)
        driver.find_element_by_css_selector("li.showFinderListItem").click()
        driver.find_element_by_css_selector("#showfinder_cities > li.showFinderListItem").click()
        driver.find_element_by_css_selector("span.x").click()
        
        driver.find_element_by_css_selector("span.openerShowChooserLink.topOfPage").click()
        time.sleep(1)
        driver.find_element_by_css_selector("li.showFinderListItem.selected").click()
        driver.find_element_by_css_selector("#showfinder_cities > li.showFinderListItem.selected").click()
        driver.find_element_by_css_selector("span.x").click()
    	    
    	########################################################################
    @unittest.skip("Develop later") 	
    def test_pop_shows(self):
        	
        driver = self.driver
        
        driver.find_element_by_css_selector("section.mostPopularShows nav.nextCarousel").click()
        driver.find_element_by_css_selector("section.mostPopularShows nav.prevCarousel").click()
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
        
    def test_images(self):
    	
    	try:
    	    self.assertNotEqual(self.total, -1) 
    	    self.assertNotEqual(self.total, 0)
    	    self.assertNotEqual(self.total, '-1') 
    	    self.assertNotEqual(self.total, '0')
    	    
        except AssertionError:
            self.results_writer(URL + " has 0 or -1 assets!")
    
        ########################################################################
    
    def response(self):
    	
    	try:
    	    response = urllib2.urlopen(URL)
    	            
    	except Exception, e:
    	    self.results_writer(URL + ' ' + str(e))
    	    
    	    #self.fail(str(e))
    
        ########################################################################
    
    def published(self):	        
    	 
        try:
            self.assertNotEqual(self.page_activation[0]['activated'], 'false')
            	
        except AssertionError:
            
            PUBLISHED.write(URL + " is not published!")
            PUBLISHED.write('\n')
            self.verificationErrors.append(URL + " NOT Published") 
            return False
            
        return True
    
        ########################################################################
      
    def test_thumbnails(self):
    	
    	if self.driver is not None:
    	
    	    #driver = self.driver
    	    #driver.get(URL)
    	    #driver.refresh()
    	    self.response()
    	    """
    	    try:
    	        driver.find_element_by_css_selector('div.error-wrap h2')
    	    
            except:
                driver.find_element_by_css_selector('section#opener-links.contentOpenerSlideshowLinks ul li a.contentOpenerSlideshowLink').click()
                driver.find_element_by_css_selector('a.ssViewThumbs span.miniCaps').click()
                on_prod = driver.find_elements_by_css_selector('ul.ssThumbsList li.ssThumbsListitem img.ssPhoto')
    	    
    	        try:
    	            self.assertEqual(str(len(on_prod)), str(self.total))
    	        
                except AssertionError:
                    self.results_writer(URL + " has " + str(len(on_prod)) + " images on prod, and " + str(tt['total']) + " images in JSON")
                    self.verificationErrors.append(URL + " has different number of images on prod and in JSON")
    	    
	    
    	    try:
    	    	time.sleep(5)
    	        driver.find_elements_by_xpath("//img[contains(@src,'" + re.compile('http://pixel.nymag.com/images/.*') + "')]")
    	    except Exception, e:
    	    	print str(e)
    	    	self.verificationErrors.append(URL + " has images that do not load all the way on prod")
    	    	self.results_writer(URL + " has images that don't load all the way in the production version of the show")
    	    	
    	    """	
    	        
                
        ########################################################################
        
    def results_writer(self, error):
    	    
    	RESULTS.write(error)
    	RESULTS.write('\n')
    	
    	########################################################################
        
    def tearDown(self):
    	    
    	if self.driver is not None:
    	    self.driver.quit()
    	self.assertEqual(self.verificationErrors, [])
    	
        ########################################################################
        ########################################################################
        
        
try:
    if DATA.keys()[1] == 'error':
    	print "ERROR" + URL
        RESULTS.write(URL + ' Is a Dummy Show')
        RESULTS.write('\n')
     
except IndexError:      
    
    y = 1
    print URL
    filename = str(URL.split('/'))
   # results = open('/Users/nsmith/Desktop/runwayresults/' + str(filename[-1]) + '.html', 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(ShowMigration)
    unittest.TextTestRunner(verbosity=2).run(suite)
   # runner = HTMLTestRunner.HTMLTestRunner(stream=results, title="TESTING", description='Results for Show Runwaymig')
   # results.close()

RESULTS.close()
TAGGED.close()
PUBLISHED.close()
    
    

    
    
