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

STG = 'http://stg.nymetro.com/thecut/news/'
EC2 = 'http://ec2.qa.nymetro.com/thecut/news/'
PROD = 'http://nymag.com/thecut/news/'


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


class NewsSplash(unittest.TestCase):

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
        
    def test_metadata(self):
    	
    	self.assertEqual(str(self.soup.find('title').string), 'Fashion News: A Fashion Blog and Style Site - TheCut')
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'description', 'content':"The Cut's news section takes the form of a fashion blog with a continuous feed of the latest Cut articles."}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'keywords', 'content':'fashion news'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.hierarchy', 'content':'The Cut:News:Index'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.hierarchy.title', 'content':'The Cut News Feed'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.type', 'content':'Index'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.source', 'content':'Online'}), None)
    	self.assertNotEqual(self.soup.find('link', attrs={'rel':'canonical', 'href':'http://nymag.com/thecut/news/'}), None)

    	################################################################################

    def test_lpos(self):
    	    
    	#Test for Omniture link positions
    	
    	lpos = re.compile('&lpos.*')
    	self.assertNotEqual(self.spam('a', attrs={'name':lpos}), None)
    	    
        ################################################################################
    	    
    def test_thumbnail_entries(self):
    	
    	c = 0
    	
    	for tag in self.spam('article', attrs={'class':'feedEntry thumbnail', 'id':'entry', 'data-publish-datetime':True}):
    	    
	    article = tag 
            try:    
            	self.assertNotEqual(article.find('div', attrs={'class':'featureImage thumbnail'}).contents, [])
                self.assertNotEqual(article.find('a', attrs={'href':True}), None)
                self.assertNotEqual(article.find('ul', attrs={'class':'meta metaAuthor'}), None)
                self.assertNotEqual(article.find('cite').contents, [])
                self.assertNotEqual(article.find('img', attrs={'src':True}), None)
                self.assertNotEqual(article.find('li', attrs={'class':'metaTime'}).contents, [])
                self.assertNotEqual(article.find('h2').contents, [])
                self.assertNotEqual(article.find('div', attrs={'class':'excerpt'}).contents, [])
                self.assertNotEqual(article.find('p').contents, [])
                
            except AssertionError, e:
            	print article
            	self.verificationErrors.append(str(c) + ' Thumbnail Article Entry fail')
            	pass 
            	
    	    c += 1
    	    
    	################################################################################
    	    
    def test_vert_entries(self):
    	
    	c = 0
    	
    	for tag in self.spam('article', attrs={'class':'feedEntry vert', 'id':'entry', 'data-publish-datetime':True}):
    	    
	    article = tag 
            try:    
            	self.assertNotEqual(article.find('div', attrs={'class':'featureImage vert'}).contents, [])
                self.assertNotEqual(article.find('a', attrs={'href':True}), None)
                self.assertNotEqual(article.find('ul', attrs={'class':'meta metaAuthor'}), None)
                self.assertNotEqual(article.find('cite').contents, [])
                self.assertNotEqual(article.find('img', attrs={'src':True}), None)
                self.assertNotEqual(article.find('li', attrs={'class':'metaTime'}).contents, [])
                self.assertNotEqual(article.find('h2').contents, [])
                self.assertNotEqual(article.find('div', attrs={'class':'excerpt'}).contents, [])
                self.assertNotEqual(article.find('p').contents, [])
                
            except AssertionError, e:
            	self.verificationErrors.append(str(c) + ' Vertical Article Entry fail')
            	pass 
            	
    	    c += 1	
    	    
    	################################################################################
    	    
    def test_square_entries(self):
    	
    	c = 0
    	
    	for tag in self.spam('article', attrs={'class':'feedEntry square', 'id':'entry', 'data-publish-datetime':True}):
    	    
	    article = tag 
            try:    
            	self.assertNotEqual(article.find('div', attrs={'class':'featureImage square'}).contents, [])
                self.assertNotEqual(article.find('a', attrs={'href':True}), None)
                self.assertNotEqual(article.find('ul', attrs={'class':'meta metaAuthor'}), None)
                self.assertNotEqual(article.find('cite').contents, [])
                self.assertNotEqual(article.find('img', attrs={'src':True}), None)
                self.assertNotEqual(article.find('li', attrs={'class':'metaTime'}).contents, [])
                self.assertNotEqual(article.find('h2').contents, [])
                self.assertNotEqual(article.find('div', attrs={'class':'excerpt'}).contents, [])
                self.assertNotEqual(article.find('p').contents, [])
                
            except AssertionError, e:
            	print article
            	self.verificationErrors.append(str(c) + ' Square Article Entry fail')
            	pass 
            	
    	    c += 1
    	    
    	################################################################################
    	    
    def test_horiz_entries(self):
    	
    	c = 0
    	
    	for tag in self.spam('article', attrs={'class':'feedEntry horiz', 'id':'entry', 'data-publish-datetime':True}):
    	    
	    article = tag 
            try:    
            	self.assertNotEqual(article.find('div', attrs={'class':'featureImage horiz'}).contents, [])
                self.assertNotEqual(article.find('a', attrs={'href':True}), None)
                self.assertNotEqual(article.find('ul', attrs={'class':'meta metaAuthor'}), None)
                self.assertNotEqual(article.find('cite').contents, [])
                self.assertNotEqual(article.find('img', attrs={'src':True}), None)
                self.assertNotEqual(article.find('li', attrs={'class':'metaTime'}).contents, [])
                self.assertNotEqual(article.find('h2').contents, [])
                self.assertNotEqual(article.find('div', attrs={'class':'excerpt'}).contents, [])
                self.assertNotEqual(article.find('p').contents, [])
                
            except AssertionError, e:
            	print article
            	self.verificationErrors.append(str(c) + ' Horizontal Article Entry fail')
            	pass 
            	
    	    c += 1
    	    
    	################################################################################
    	    
    def test_interstitial_entries(self):
    	
    	c = 0
    	
    	for tag in self.spam('article', attrs={'class':'feedEntry interstitial', 'id':'entry', 'data-publish-datetime':True}):
    	    
	    article = tag 
            try:    
            	self.assertNotEqual(article.find('div', attrs={'class':'featureImage thumbnail'}).contents, [])
                self.assertNotEqual(article.find('a', attrs={'href':True}), None)
                self.assertNotEqual(article.find('ul', attrs={'class':'meta metaAuthor'}), None)
                self.assertNotEqual(article.find('cite').contents, [])
                self.assertNotEqual(article.find('img', attrs={'src':True}), None)
                self.assertNotEqual(article.find('li', attrs={'class':'metaTime'}).contents, [])
                self.assertNotEqual(article.find('h2').contents, [])
                self.assertNotEqual(article.find('div', attrs={'class':'excerpt'}).contents, [])
                self.assertNotEqual(article.find('p').contents, [])
                
            except AssertionError, e:
            	print article
            	self.verificationErrors.append(str(c) + ' Interstitial Article Entry fail')
            	pass 
            	
    	    c += 1
    	    
    	################################################################################
    	
    def test_cont_scroll(self):
    	    
    	self.assertNotEqual(self.spam('section', attrs={'class':'feed', 'id':'feedList', 'data-continuous-scroll':'true'}), None)
    	
    	################################################################################
    	
    def test_bizdev(self):
    	    
    	bizdev = self.spam('script')[0]
    	    
    	self.failUnless(re.search('zone: "other"', str(bizdev), re.I))
    	self.failUnless(re.search('takeover: "news"', str(bizdev), re.I))
    	
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
    results = open('../../DATA/HTML/SPLASH/' + filename[-2] + '.' + ENV + '.newssplash.html', 'wb')
    print "TESTING " + BASEURL
    suite = unittest.TestLoader().loadTestsFromTestCase(NewsSplash)
    unittest.TextTestRunner(verbosity=2).run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=results, title=filename[-2], description='Results for News Splash Page on ' + ENV)
    runner.run(suite)
    
    x += 1
    
