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

STG = 'http://stg.nymetro.com/thecut/shopping/'
EC2 = 'http://ec2.qa.nymetro.com/thecut/shopping/'
PROD = 'http://nymag.com/thecut/shopping/'


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


class GoodsSplash(unittest.TestCase):

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
    	
    def test_lede(self):
    	    
    	#Tests the articles in the rotating lede
    	    
    	u = 0
    	
    	for tag in self.spam('li', attrs={'class':'ledeArticle'}):
    	    
	    article = tag
	    
	    try:
    	    
    	        self.assertNotEqual(article.find('div', attrs={'class':'ledeImage'}), None)
    	        self.assertNotEqual(article.find('a', attrs={'href':True}), None)
    	        
    	        self.assertNotEqual(article.find('div', attrs={'data-picture':'true', 'data-alt':True}), None)
    	        self.assertNotEqual(article.find('div', attrs={'data-src':True}), None)
    	        self.assertNotEqual(article.find('div', attrs={'data-src':True, 'data-media':'(max-width: 600px)'}), None)
    	        self.assertNotEqual(article.find('div', attrs={'data-src':True, 'data-media':'(min-width: 601px)'}), None)
    	        self.assertNotEqual(article.find('noscript').contents, [])
    	    
	    	self.assertNotEqual(article.find('header', attrs={'class':'ledeHeader'}), None)
	    	self.assertNotEqual(article.find('div', attrs={'class':'ledeFeatureRubric'}), None)
	    	self.assertNotEqual(article.find('a', attrs={'class':'ledeFeatureRubricLink', 'href':True}), None)
	    	self.assertNotEqual(article.find('h2', attrs={'class':'ledeHeadline'}), None)
	    	self.assertNotEqual(article.find('a', attrs={'class':'ledeHeadlineLink', 'href':True}), None)
	    	self.assertNotEqual(article.find('div', attrs={'class':'ledeByline'}), None)
	    	
	    	self.assertEqual(article.find('p', attrs={'class':'excerpt'}), None)
	    	
	    except AssertionError, e:
	    	print article
	    	self.verificationErrors.append(str(u) + " Lede Article Failure")
	    	pass   
	    
	    u += 1
	     
	self.assertEqual(u, 4)
	
	################################################################################
	
    def test_prev_next(self):
    	    
    	#Tests the previous/next arrows
    	    
    	self.assertNotEqual(self.soup.find('nav', attrs={'class':'next'}), None)
    	self.assertNotEqual(self.soup.find('nav', attrs={'class':'prev'}), None)
    	self.assertNotEqual(self.soup.find('a', attrs={'href':'javascript:;', 'class':'ledeNext'}), None)
    	self.assertNotEqual(self.soup.find('a', attrs={'href':'javascript:;', 'class':'ledePrev'}), None)
    	
    	################################################################################
    	
    def test_lede_markers(self):
    	    
    	#Tests for lede markers
    	    
    	self.assertNotEqual(self.soup.find('ol', attrs={'class':'ledeMarkers'}), None)
    	
    	################################################################################
    	    
    def test_metadata(self):
    	
    	self.assertEqual(str(self.soup.find('title').string), 'Shopping Recommendations for the Fashionable: What to Buy - TheCut')
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'description', 'content':'What clothing, accessories, and beauty products are editors of The Cut obsessing over today? Check them out in the Goods Section of The Cut.'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'keywords', 'content':'goods,best bets'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.hierarchy', 'content':'The Cut:Shopping and Goods:Index'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.hierarchy.title', 'content':'The Cut Goods'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.type', 'content':'Index'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.source', 'content':'Online'}), None)
    	self.assertNotEqual(self.soup.find('link', attrs={'rel':'canonical', 'href':True}), None)

    	################################################################################

    def test_lpos(self):
    	    
    	#Test for Omniture link positions
    	
    	lpos = re.compile('&lpos.*')
    	self.assertNotEqual(self.spam('a', attrs={'name':lpos}), None)
    	    
    	################################################################################    
    	    
    def test_entries(self):
    	    
    	#Entries
    	
    	u = 0
    	
    	for tag in self.spam('article', attrs={'class':'goodsEntry', 'id':'entry', 'data-publish-datetime':True}):
    	    
	    article = tag 
	    
            try:    
                self.assertNotEqual(article.find('div', attrs={'class':'primaryImage'}), None)
                self.assertNotEqual(article.find('a', attrs={'href':True}), None)
                
                self.assertNotEqual(article.find('div', attrs={'data-picture':'true'}), None)
                self.assertNotEqual(article.find('div', attrs={'data-src':True, 'data-media':None}), None)
                self.assertNotEqual(article.find('div', attrs={'data-src':True, 'data-media':'(max-width: 600px)'}), None)
                self.assertNotEqual(article.find('div', attrs={'data-src':True, 'data-media':'(max-width: 800px)'}), None)
                self.assertNotEqual(article.find('div', attrs={'data-src':True, 'data-media':'(min-width: 801px)'}), None)
                self.assertNotEqual(article.find('div', attrs={'data-src':True, 'data-media':'(-webkit-min-device-pixel-ratio: 1.5)'}), None)
                self.assertNotEqual(article.find('noscript').contents, [])
                
            except AssertionError, e:
            	print article
            	self.verificationErrors.append(str(u) + ' Article Entry fail')
            	pass 
            	
    	    u += 1
    	    
    	self.failUnless(u == 11)
    	
        ################################################################################
        
    def test_loadmore(self):

	self.assertEqual(str(self.soup.find('a', attrs={'id':'loadMoreEntries', 'class':'galleryOpen'}).string), 'Show 12 More')
	
    	################################################################################
    	
    def test_bizdev(self):
    	    
    	bizdev = self.spam('script')[0]
    	    
    	self.failUnless(re.search('zone: "shopping"', str(bizdev), re.I))
    	self.failUnless(re.search('takeover: "goods"', str(bizdev), re.I))
           
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
    results = open('../../DATA/HTML/SPLASH/' + filename[-2] + '.' + ENV + '.goodssplash.html', 'wb')
    print "TESTING " + BASEURL
    suite = unittest.TestLoader().loadTestsFromTestCase(GoodsSplash)
    unittest.TextTestRunner(verbosity=2).run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=results, title=filename[-2], description='Results for Goods Splash Page on ' + ENV)
    runner.run(suite)
    
    x += 1
