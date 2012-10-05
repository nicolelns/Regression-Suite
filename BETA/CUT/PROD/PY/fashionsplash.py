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

STG = 'http://stg.nymetro.com/thecut/fashion/'
EC2 = 'http://ec2.qa.nymetro.com/thecut/fashion/'
PROD = 'http://nymag.com/thecut/fashion/'


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


class FashionSplash(unittest.TestCase):

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
    	
    def test_fashionshows(self):
    	    
    	pass

        ################################################################################
        
    def test_text(self):
    	    
    	    header = self.soup.find('h3', attrs={'class':None})
    	    
    	    self.assertNotEqual(header, None)
    	    self.assertEqual(header.string, "Fashions Newsfeed")
    	    
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
	    	
	    except AssertionError, e:
	    	#print article
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
    	
    	self.assertEqual(str(self.soup.find('title').string), 'Fashion Trends, Style Tips and Industry News – TheCut')
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'description', 'content':"What to wear? Get fashion advice on clothing and accessories. Plus, read the latest fashion news. It's a fashion site that just takes fashion seriously enough."}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'keywords', 'content':'style,clothing,fashion news,accessories,fashion'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.hierarchy', 'content':'The Cut:Fashion:Index'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.hierarchy.title', 'content':'The Cut Fashion Section'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.type', 'content':'Index'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.source', 'content':'Online'}), None)
    	self.assertNotEqual(self.soup.find('link', attrs={'rel':'canonical', 'href':'http://nymag.com/thecut/fashion/'}), None)

    	################################################################################

    def test_lpos(self):
    	    
    	#Test for Omniture link positions
    	
    	lpos = re.compile('&lpos.*')
    	self.assertNotEqual(self.spam('a', attrs={'name':lpos}), None)
    	    
    	################################################################################    
    	    
    def test_entries(self):
    	    
    	#Entries
    	
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
                
                self.assertEqual(article.find('p', attrs='class':'excerpt'}), None)
                
            except AssertionError, e:
            	print article
            	self.verificationErrors.append(str(u) + ' Article Entry fail')
            	pass  
            	
    	    u += 1
    	    
    	self.assertEqual(u, 10)
    	
        ################################################################################
    	    
    def test_loadmore(self):

	self.assertNotEqual(self.soup.find('a', attrs={'id':'loadMoreEntries', 'class':'galleryOpen'}), None)
	
        ################################################################################
    
    def test_tracktrends(self):
    	    
    	self.assertNotEqual(self.soup.find('section', attrs={'class':'module trendsModule'}), None)
    	self.assertNotEqual(self.soup.find('h3', attrs={'class':'hed'}), None)
    	u = 0
    	
    	self.assertNotEqual(self.soup.find('ul', attrs={'class':'trendsList'}), None)
    	trend = self.soup.find('ul', attrs={'class':'trendsList'})
    	
    	for tag in trend.children:
    	    
    	    try:
    	    
    		self.assertNotEqual(trend.find_all('a', attrs={'href':True}), None)
    		self.assertNotEqual(trend.find('li', attrs={'class':'listItem'}), None)
    		self.assertNotEqual(trend.find('p', attrs={'class':'listText'}).contents, [])
    		
    	    except AssertionError, e:
    	    	print tag
    	    	self.verificationErrors.append(str(u) + ' Trend Fail')
    	    	pass
    	    
    	    u += 1
    	    
    	self.failUnless(u == 17)		# (Number of items/2) + 1
    	self.assertNotEqual(self.soup.find('img', attrs={'class':'imagePath', 'src':True}), None)
    	    
        ################################################################################
    	
    def test_bizdev(self):
    	    
    	bizdev = self.spam('script')[0]
    	    
    	self.failUnless(re.search('zone: "fashion"', str(bizdev), re.I))
    	self.failUnless(re.search('takeover: "fashion"', str(bizdev), re.I))
    	
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
    results = open('../../DATA/HTML/SPLASH/' + filename[-2] + '.' + ENV + '.fashionsplash.html', 'wb')
    print "TESTING " + BASEURL
    suite = unittest.TestLoader().loadTestsFromTestCase(FashionSplash)
    unittest.TextTestRunner(verbosity=2).run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=results, title=filename[-1], description='Results for Fashion Splash Page on ' + ENV)
    runner.run(suite)
    
    x += 1
