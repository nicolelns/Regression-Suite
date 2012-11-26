#! /usr/bin/python                                                                                                                                                                                  
# -*- coding: utf-8 -*-

import sys
import os
import re
import httplib
import urllib
import urlparse
import unittest
import HTMLTestRunner
import string
import time
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


class RunwayShowOpener(unittest.TestCase):

    def setUp(self):

        self.BASEURL = str(show)
        
        self.req = MyOpener()
        self.page = self.req.open(self.BASEURL)
        self.text = self.page.read()
        self.page.close()
        self.soup = BeautifulSoup(self.text)
        self.spam = self.soup.find_all
        self.verificationErrors = []
        
        ################################################################################
        
    def test_style(self):
    	    
    	self.assertNotEqual(self.soup.find('style', attrs={'type':'text/css'}).contents, [])
    	
    	################################################################################
    	
    def test_breadcrumb(self):
    	    
    	self.assertEqual(str(self.soup.find('a', attrs={'href':'/thecut/fashion/', 'class':'breadCrumbsLink'}).string), 'Fashion')
    	self.assertEqual(str(self.soup.find('a', attrs={'href':'/thecut/runway/', 'class':'breadCrumbsLink'}).string), 'Runway')
    	self.assertNotEqual(self.soup.find('a', attrs={'href':'javascript:;', 'class':'breadCrumbsLink openShowFinder'}).contents, [])
    	self.assertNotEqual(self.soup.find('span', attrs={'class':'openerShowChooserLink topOfPage'}).contents, [])
    	
        ################################################################################
        
    def test_opener(self):
    	    
    	self.assertNotEqual(self.soup.find('div', attrs={'id':'content-opener', 'class':'contentOpener'}), None)
        self.assertNotEqual(self.soup.find('header', attrs={'class':'contentOpenerShowInfo'}), None)
        
        self.assertNotEqual(str(self.soup.find('h1', attrs={'class':'contentOpenerShowTitle'}).string), '')
        self.assertNotEqual(str(self.soup.find('h2', attrs={'class':'contentOpenerSeasonYearType'}).string), '')
        
        self.assertNotEqual(self.soup.find('section', attrs={'id':'opener-links', 'class':'contentOpenerSlideshowLinks'}), None)
        
        self.assertNotEqual(str(self.soup.find('a', attrs={'class':'contentOpenerSlideshowLink contentOpenerCollectionLink', 'href':'javascript:;', 'data-runway-section':'collection-full-length'}).contents), [])
        #self.assertNotEqual(str(self.soup.find('a', attrs={'class':'contentOpenerSlideshowLink contentOpenerVideoLink', 'href':'javascript:;', 'data-runway-section':'videos'}).contents), [])
        
        ################################################################################
        
    def test_sharetools(self):
    	    
    	self.assertEqual(str(self.soup.find('span', attrs={'class':'shareLinksTitle'}).string), 'Share This Show')
    	self.assertNotEqual(self.soup.find('i', attrs={'class':'iconFacebook'}), None)
    	self.assertNotEqual(self.soup.find('i', attrs={'class':'iconTwitter'}), None)
    	
    	################################################################################
        
    def test_metadata(self):
    	
    	#self.assertEqual(str(self.soup.find('title').string), 'REPLACE_WITH_TITLE_LATER')
    	
    	self.assertNotEqual(self.soup.find('title').contents, [])
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'description', 'content':True}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'keywords', 'content':True}), None)
    	
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.hierarchy', 'content':'The Cut:Fashion:Runway:Shows'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.hierarchy.title', 'content':'Runway Show Openers'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.type', 'content':'Runway Show'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.source', 'content':'Online'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.subtype', 'content':'Runway Show Opener'}), None)
    	self.assertNotEqual(self.soup.find('link', attrs={'rel':'canonical', 'href':self.BASEURL}), None)
     
        ################################################################################
     
    def test_pop_shows(self):
    	
    	self.assertEqual(str(self.soup.find('h1', attrs={'class':'runwayHeader sectionHeader'}).string), "Most Popular Shows")
    	u = 0
    	
    	for tag in self.spam('ul', attrs={'class':'mostPopularShowsList jcarousel-skin-cutTopShows'}):
    		
    	    popshow = tag
    	    
    	    try:
    	        self.assertNotEqual(popshow.find('li', attrs={'class':'mostPopularShowsListitem'}), None)
    	        self.assertNotEqual(popshow.find('a', attrs={'class':'mostPopularShowLink', 'href':True}), None)
    	        self.assertNotEqual(popshow.find('img', attrs={'class':'silo', 'src':True}), None)
    	        self.assertNotEqual(str(popshow.find('h3', attrs={'class':'runwayHeader'}).string), '')
    	        self.assertNotEqual(str(popshow.find('h4', attrs={'class':'runwaySeasonHeader'}).string), '')
    	        
    	    except AssertionError:
    	    	self.verificationErrors.append("Pop Show Fail " + str(u))
    	    	print popshow
    	    	pass
    	
    	    u += 1
    	    
    	#self.assertEqual(u, 8)
  
        ################################################################################
    	 
    def tearDown(self):

        self.assertEqual([], self.verificationErrors)
        
        ################################################################################

"""   
FUTURE FEATURE:

def fail_writer(test):
	
    test = test	
    t = datetime.time
    print t
    f = open('../failures.txt')
    f.write(t + '\t' + BASEURL + '\n')
    print test

"""

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
    	
    for s in range(len(SHOWS)):	
    	show = SHOWS[s].strip('\n')
        filename = show.split('/')
        
        results = open('../../DATA/HTML/RUNWAY/OPENER/' + filename[-1] + '.runwayshowopener.html', 'wb')
        print "TESTING " + show
        suite = unittest.TestLoader().loadTestsFromTestCase(RunwayShowOpener)
        unittest.TextTestRunner(verbosity=2).run(suite)
        runner = HTMLTestRunner.HTMLTestRunner(stream=results, title=show, description='Results for Runway Show Opener on ' + ENV)
        runner.run(suite)
        
        s += 1
    
    x += 1
    
