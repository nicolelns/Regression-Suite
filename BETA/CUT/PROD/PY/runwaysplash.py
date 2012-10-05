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

x = 0
y = 0

STG = 'http://stg.nymetro.com/thecut/runway/'
EC2 = 'http://ec2.qa.nymetro.com/thecut/runway/'
PROD = 'http://nymag.com/thecut/runway'


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


class RunwaySplash(unittest.TestCase):

    def setUp(self):

        self.BASEURL = BASEURL
        
        self.req = MyOpener()
        self.page = self.req.open(self.BASEURL)
        self.text = self.page.read()
        self.page.close()
        self.soup = BeautifulSoup(self.text)
        self.spam = self.soup.find_all
        self.verificationErrors = []
        
        ################################################################################
    
    def test_text(self):
    	    
    	header = self.soup.find('h3', attrs={'class':None})
    	    
        self.assertNotEqual(header, None)
 	self.assertEqual(header.string, "Runway Newsfeed")
    	    
    	################################################################################
        
    def test_metadata(self):
    	
    	self.assertEqual(str(self.soup.find('title').string), 'Runway & Fashion Shows: Fashion Week in New York, Europe, Asia - TheCut')
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'description', 'content':'Complete coverage of fashion weeks in cities worldwide with slideshows, videos, and reviews of runway shows and collections for all seasons. Get the latest fashion show reports from Milan, Paris, London and New York.'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'keywords', 'content':'london fashion week,rtw,new york fashion week,runway,runway shows,menswear,haute couture,milan fashion week,mercedes-benz fashion week,paris fashion week,collections,couture'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.hierarchy', 'content':'The Cut:Fashion:Runway:Index'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.hierarchy.title', 'content':'The Cut Runway Section'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.type', 'content':'Index'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.source', 'content':'Online'}), None)
    	self.assertNotEqual(self.soup.find('link', attrs={'rel':'canonical', 'href':'http://nymag.com/thecut/runway/'}), None)
    	
    	################################################################################

    def test_lpos(self):
    	
    	lpos = re.compile('&lpos.*')
    	self.assertNotEqual(self.spam('a', attrs={'name':lpos}), None)
    	
        ################################################################################
    	    
    def test_entries(self):
    	
    	u = 0
    	
    	for tag in self.spam('article', attrs={'class':'feedEntry', 'id':'entry', 'data-publish-datetime':True}):
    	    
	    article = tag 
	    
            try:    
                self.assertNotEqual(article.find('div', attrs={'class':'featureImage'}), None)
                self.assertNotEqual(article.find('a', attrs={'href':True}), None)
                
                self.assertNotEqual(article.find('div', attrs={'data-picture':'true'}), None)
                self.assertNotEqual(article.find('div', attrs={'data-src':True, 'data-media':None}), None)
                self.assertNotEqual(article.find('div', attrs={'data-src':True, 'data-media':'(max-width: 600px)'}), None)
                self.assertNotEqual(article.find('div', attrs={'data-src':True, 'data-media':'(min-width: 601px)'}), None)
                self.assertNotEqual(article.find('noscript').contents, [])
                
                self.assertNotEqual(article.find('header'), None)
		self.assertNotEqual(article.find('li', attrs={'class':'metaTime'}).contents, [])
                #self.assertNotEqual(article.find('li', attrs={'class':'comments'}), None)
                self.assertNotEqual(article.find('h2'), None)
                self.assertNotEqual(article.find('p', attrs={'class':'excerpt'}).contents, [])
                
            except AssertionError, e:
            	print article
            	self.verificationErrors.append(str(u) + ' Article Entry fail')
            	pass  
            	
    	    u += 1
    	    
    	self.assertEqual(u, 10)
    	
       ################################################################################
    	
    def test_videos(self):
    	
    	c = 0
    	
    	for tag in self.spam('li', attrs={'class':'runwayVideoListItem'}):
    		
    	    video = tag
    	    try:
    	    	self.assertNotEqual(video.find('a', attrs={'href':True}), None)
    	    	self.assertNotEqual(video.find('div', attrs={'class':'image'}), None)
    	    	self.assertNotEqual(video.find('div', attrs={'class':'overlay'}), None)
    	    	self.assertNotEqual(video.find('img', attrs={'src':True}), None)   
    	        self.assertNotEqual(video.find('p', attrs={'class':'label'}).contents, [])
    	        
    	    except AssertionError, e:
    	    	print video
            	self.verificationErrors.append(str(c) + ' Video fail')
            	pass 
            	
    	    c += 1
    	    
    	self.assertEqual(c, 4)
    	self.assertNotEqual(self.spam('p', attrs={'class':'allDevice'}).contents, [])
    	self.assertNotEqual(self.spam('p', attrs={'class':'mobileDevice'}).contents, [])
    	
    ################################################################################
    
    @unittest.skip('Not Yet Implemented')
    def test_runway_top(self):
    	
    	c = 0
    	for tag in self.spam('li', attrs={'class':'runwayLedeModule topShows'}):
    		
    	    top = tag
    	    
    	    self.assertNotEqual(top.find('div', attrs={'class':'titleTab'}), None)
    	    self.assertNotEqual(top.find('div', attrs={'class':'ledeWindow'}), None)
    	    self.assertNotEqual(top.find('h3', attrs={'class':'seasonTitle'}), None)
    	    self.assertNotEqual(top.find('li', attrs={'class':'designer'}), None)
    	    self.assertNotEqual(top.find('div', attrs={'class':'designerName'}), None)
    	    self.assertNotEqual(top.find('img', attrs={'src':True}), None)
    	    self.assertNotEqual(top.find('a', attrs={'href':True}), None)
    	    self.assertNotEqual(top.find('div', attrs={'class':'siloWindow'}), None)
    	    self.assertNotEqual(top.find('div', attrs={'class':'designSilo'}), None)
    	    self.assertNotEqual(top.find('img', attrs={'alt':'silhouette', 'src':True}), None)
    	    self.assertNotEqual(top.find('div', attrs={'class':'designerLabel'}), None)
    	 
        c += 1
        
    ################################################################################
    	 
    def test_runway_az(self): 	 
    	
    	c = 0
    	a = 0
    	for tag in self.spam('li', attrs={'class':'runwayLedeModule azShows'}):
    		
    	    az = tag
    		
            self.assertNotEqual(az.find('div', attrs={'class':'titleTab'}), None)
    	    self.assertNotEqual(az.find('div', attrs={'class':'ledeWindow'}), None)
    	    
    	    alpha = az.find('ol', attrs={'class':'alphaFinder'})
    	    for tag in alpha('a'):
    	    	letter = tag['href']
    	    	a += 1
    	    	
    	    self.assertEqual(a,27)	# 26 Letters plus # for Nums
    	    
    	    self.assertNotEqual(az.find('ul', attrs={'class':'designerList'}), None)
    	    self.assertNotEqual(az.find('a', attrs={'class':'designerLink', 'href':True}), None)
    	    
    	c += 1
            
        ################################################################################    
            
    def test_runway_latest(self):        
        
        c = 0
        for tag in self.spam('li', attrs={'class':'runwayLedeModule latestShows'}):
    		
            latest = tag
            
            self.assertNotEqual(latest.find('div', attrs={'class':'titleTab'}), None)
    	    self.assertNotEqual(latest.find('ul', attrs={'class':'designerList'}), None)
    	    self.assertNotEqual(latest.find('h3', attrs={'class':'seasonTitle'}), None)
    	    self.assertNotEqual(latest.find('li', attrs={'class':'dateMarker'}), None)
    	    self.assertNotEqual(latest.find('li', attrs={'class':'designer'}), None)
    	    self.assertNotEqual(latest.find('div', attrs={'class':'designerName'}), None)
    	    self.assertNotEqual(latest.find('img', attrs={'src':True}), None)
    	    self.assertNotEqual(latest.find('a', attrs={'href':True}), None)
    	    self.assertNotEqual(latest.find('div', attrs={'class':'siloWindow'}), None)
    	    self.assertNotEqual(latest.find('div', attrs={'class':'designSilo'}), None)
    	    self.assertNotEqual(latest.find('img', attrs={'alt':'silhouette', 'src':True}), None)
    	    self.assertNotEqual(latest.find('p', attrs={'class':'review'}), None)
    	    
        c += 1
        
        ################################################################################
    	
    def test_bizdev(self):
    	    
    	bizdev = self.spam('script')[0]
    	    
    	self.failUnless(re.search('zone: "fashion"', str(bizdev), re.I))
    	self.failUnless(re.search('takeover: "runway"', str(bizdev), re.I))
    	
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
    	BASEURL = STG
    	ENV = 'stg'	
    
    elif x == 1:
    	BASEURL = EC2
    	ENV = 'ec2'
        
    else:
    	BASEURL = PROD
    	ENV = ''
    
    filename = BASEURL.split('/')
    results = open('../../DATA/HTML/SPLASH/' + filename[-2] + '.' + ENV + '.runwaysplash.html', 'wb')
    print "TESTING " + BASEURL
    suite = unittest.TestLoader().loadTestsFromTestCase(RunwaySplash)
    unittest.TextTestRunner(verbosity=2).run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=results, title=filename[-2], description='Results for Runway Splash Page on ' + ENV)
    runner.run(suite)
    
    x += 1
    
