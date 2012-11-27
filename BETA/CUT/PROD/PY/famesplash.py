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
import splashconfig
import splashparser
import article_json_parser
import string
import datetime
import json
import time
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


class FameSplash(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
    
        ################################################################################

    def json_organizer(self, _json):
        
	"""
        NOTE TO SELF:
        This needs to be a bunch of tiny functions that are only eval'd at runtime.  
        This section of code is way too long and has too many try blocks
        Example: 
        def test_myFunc(self, data)
        data = self.json_organizer_imgs(json)
        where self.json_organizer_imgs() is some function that just returns the 
        value for the key 'primary-image' inside the article's json object
        when this data is needed, not beforehand.
        
        """
        
        self.j = json.loads(_json)
        
        self.entry_type = self.j['entryType']
        self.feature_type = self.j['featureTypes']
        self.desc = self.j['jcr:description']
        self.title = self.j['jcr:title']
        
        try:
	    self.i = self.j['primary_image'].split('.jpg')
            self.img = str(self.i[0])
        except KeyError:
            self.img = None
            
        self.shorthead = str(self.j['shorterheadline'])
        self.excerpt = str(self.j['excerpt'])
        
        try:
            self.longhead = self.j['longerheadline']
        except KeyError:
            self.longhead = None
            
        try:
            self.author = self.j['authors'][0]
        except KeyError:
            self.author = None
            
        try:
            self.tags = self.j['cq:tags']
        except KeyError:
            self.tags = None
            
        try:
            self.f = self.j['feature_rubric'].split('/')
            self.feat = self.f[-1]
            w = self.feat.split('-')
            wordlist = []
            caps_wordlist = []
            for word in w:
            	l = word.lower()
            	if len(word) > 0:
            	    u = word[0].upper() + word[1:]
                else:
                    u = word.upper()
            	wordlist.append(l)
            	caps_wordlist.append(u)
            self.feature_rub = ' '.join(wordlist)
            self.caps_feature_rub = ' '.join(caps_wordlist)
            	    
        except KeyError:
            self.feature_rub = None
            self.caps_feature_rub = None
        
        try:
            self.primary_tag = self.j['primary_tag']
        except KeyError:
            self.primary_tag = None
            
        ################################################################################
       
    def key_test(self, data_set):
    	
    	key = data_set[0]
    	val = data_set[1]
    	return soup.find(key, val)

        ################################################################################
   
    def lede_markers(self, u):
    	    
    	#Tests for lede markers
    	
    	self.u = u
    	
    	try:
    	    o = soup.find_all('ol')
    	    # Bug - list inside list
    	    dots = [tag.find_all('li') for tag in o]
        except KeyError, e:
            results_writer(str(u) + "articles in lede " + str(len(dots)) + " lede article markers", " Fame lede markers fail.")
            
	self.assertEqual(int(self.u), len(dots[0]))
    
    	################################################################################
        
    def test_text(self):
    	  
    	try:  
    	    self.assertEqual(soup.find('h3').string, "Fame Newsfeed")
    	    
        except KeyError, e:
            results_writer("", "Beauty Newsfeed Text in header does not match 'Fame Newsfeed'")
        
        except AssertionError, e:
            results_writer("", "Fame Newsfeed Text Not on page")
    	    
    	################################################################################
    	
    def test_lede(self):
    	    
    	#Tests the articles in the rotating lede
    	  
    	u = 0
    	
    	for tag in soup.find_all('li', {'class':'ledeArticle'}):
    	    
	    link = tag.find('a')['href']
	    
	    """
	    TypeError is thrown when JSON data for an article is not in the dataset.
	    KeyError is thrown if the article link is not in the dataset.
	    This test is not broken out into smaller portions, because the for-loop iterates over all 
	    articles on the splash page nested inside of a specific <article> tag in order
	    to test each article with more granularity.
	    
	    """
	    try:
	        if DATA[link] is not None:
	            self.json_organizer(DATA[link])
	            
	        else:
	            raise TypeError
	            
	    except TypeError:
	    	results_writer(link, "No JSON available for this article.")
	    	pass
	    	
	    except KeyError, e:
	    	results_writer(link, "Link is missing from dataset.")
	    	pass
	
            else:
            	
            	img_dataset = (('div', {'class':'ledeImage'}),
            	    ('div', {'data-picture':'true', 'data-alt':self.shorthead}),	
            	    ('div', {'data-src':str(self.img) + '.jpg/a_4x-horizontal.jpg'}),
            	    ('div', {'data-src':str(self.img) + '.jpg/a_3x-horizontal.jpg', 'data-media':'(max-width: 600px)'}),
            	    ('div', {'data-src':str(self.img) + '.jpg/a_4x-horizontal.jpg', 'data-media':'(min-width: 601px)'}),
            	    ('a', {'href':link})
            	    )
            	
	        for arg in img_dataset:
    	            # Media Queries/Images
    	            try:
    	    	        self.assertNotEqual(self.key_test(arg), None)
    	        
    	            except AssertionError, e:
    	                results_writer(self.shorthead,  'failed.  Check the media queries for the lede on the fame splash page.')
    	                print arg, " FAILED"
    	                pass
            
                header_dataset = (('header', {'class':'ledeHeader'}),
                	('div', {'class':'ledeFeatureRubric'}),
                	('a', {'class':'ledeFeatureRubricLink', 'href':link}),
                	('h2', {'class':'ledeHeadline'}),
                	('a', {'class':'ledeHeadlineLink', 'href':link})
                	)
    	        
    	        for arg in header_dataset:
    	            # Header
    	            try:
    	    	        self.assertNotEqual(self.key_test(arg), None)
    	        
    	            except AssertionError, e:
    	                results_writer(self.shorthead,  'failed.  Check the header for the lede on the fame splash page.')
    	                pass
    	        
    	        # Feature Rubric
    	        if self.feature_rub is not None:
    	            
		    try:
    	            	re.search(tag.find('a', {'class':'ledeFeatureRubricLink', 'href':link}).text, self.feature_rub, re.I)
    	        
                    except:
		        results_writer("Article: " + self.shorthead, 'The lede feature rubric, ' + self.feature_rub +
		            	           " in the lede article has a problem - rubric exists in CQ - Back End.")
		# Headline Link
                try:
    	            self.assertEqual(tag.find('a', {'class':'ledeHeadlineLink', 'href':link}).text, self.shorthead)
    	            
    	        except AssertionError:
    	            results_writer(self.shorthead, "Lede headline text is not short headline")
    	        
    	        # Byline
    	        if self.author is not None:
    	            try:
    	                by = tag.find('div', {'class':'ledeByline'})
    	                
    	            except KeyError:
    	                results_writer(self.shorthead, "Lede byline fail - missing link or div tag")
    	            	    
    	            try:
    	                self.assertEqual(by.find('a', {'href':link}).text, self.author)
    	            
    	            except AssertionError:
    	                results_writer(self.shorthead, "Lede byline fail - author is not displaying")
               
	    u += 1
	
	self.lede_markers(u)
	
        #self.assertEqual(u, 4)
     
	################################################################################
	
    def test_prev_next(self):
    	    
    	#Tests the previous/next arrows
    	
    	dataset = (('nav', {'class':'next'}), 
    	    ('nav', {'class':'prev'}),
    	    ('a', {'href':'javascript:;', 'class':'ledeNext'}),
    	    ('a', {'href':'javascript:;', 'class':'ledePrev'})
    	)
    	
    	for arg in dataset:
    	    
    	    try:
    	    	self.assertNotEqual(self.key_test(arg), None)
    	        
    	    except AssertionError, e:
    	        results_writer(str(arg),  'failed.  Check the prev/next arrows for the lede on the fame splash page.')
    	        pass
    	
    	################################################################################
    @unittest.skip("DEVELOP LATER")	
    def test_lookbook_prev_next(self):
    	    
    	#Tests prev/next in lookbook module
    	    
    	self.assertNotEqual(soup.find('nav', {'class':'next'}), None)
    	self.assertNotEqual(soup.find('nav', {'class':'prev'}), None)
    	self.assertNotEqual(soup.find('a', {'href':'javascript:;', 'class':'prev prevCarousel'}).contents, [])
    	self.assertNotEqual(soup.find('a', {'href':'javascript:;', 'class':'next nextCarousel'}).contents, [])
    	
    	################################################################################
    @unittest.skip("SKIP FOR NOW")	    
    def test_metadata(self):
    	    
    	#Metadata test
    	
    	self.assertEqual(str(self.soup.find('title').string), 'Fame - Celebrity Style News, Look Books, Red Carpet Pictures - TheCut')
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'description', 'content':'Follow fashion icons and celebrity trendsetters on the red carpet, at parties, and on the street. Browse hundreds of slideshows of celebrities. Get the latest celebrity news.'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'keywords', 'content':'red carpet,famous people,fame,celebrity style'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.hierarchy', 'content':'The Cut:Fame:Index'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.hierarchy.title', 'content':'The Cut Fame Index'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.type', 'content':'Index'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'content.source', 'content':'Online'}), None)
    	self.assertNotEqual(self.soup.find('link', attrs={'rel':'canonical', 'href':'http://nymag.com/thecut/'}), None)
    	
        ################################################################################
    	
    
    def test_lpos(self):
    	    
    	#Test for Omniture link positions
    	
    	lpos = re.compile('&lpos.*')
    	
    	try:
    	    self.assertNotEqual(soup.find_all('a', {'name':lpos}), [])
    	    
        except AssertionError:
            results_writer("Fame Splash Page", " Link positioning not on fame splash page!")
    	    
    	################################################################################    
    @unittest.skip("SKIP FOR NOW")	    
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
                
            except AssertionError, e:
            	print article
            	self.verificationErrors.append(str(u) + ' Article Entry fail')
            	pass  
            	
    	    u += 1
    	    
    	self.assertEqual(u, 10)
    	
        ################################################################################
    @unittest.skip("SKIP FOR NOW")   
    def test_lookbook_mag(self):
    	    
    	for tag in self.spam('section', attrs={'class':'module lookbookMag'}):
    		
            mag = tag
            
            self.assertNotEqual(mag.find('a', attrs={'href':True}), None)
    	    self.assertNotEqual(mag.find('h3', attrs={'class':'hed'}).contents, [])
    	    self.assertNotEqual(mag.find('p', attrs={'class':'contentText'}).contents, [])
    	    self.assertNotEqual(mag.find('img', attrs={'class':'image', 'src':True}), None)
    	    self.assertNotEqual(mag.find('span', attrs={'class':'quoteText'}).contents, [])
    	
    	################################################################################
    @unittest.skip("SKIP FOR NOW")	
    def test_lookbook_module(self):
    	    
    	u = 0
    	
    	header = self.soup.find('h3', attrs={'class':'hed'})
    	
    	self.assertNotEqual(header, None)
    	self.assertEqual(header.string, "Look Books")
    	self.assertEqual(str(self.soup.find('h4', attrs={'class':'tout'}).string), "Newly Updated!")
    	    
    	for tag in self.spam('li', attrs={'class':'lookbookListitem'}):
    	    
	    article = tag
	    
	    try:
    	    
    	        self.assertNotEqual(article.find('div', attrs={'class':'lookbookImage'}), None)
    	        self.assertNotEqual(article.find('a', attrs={'class':'lookbookLink','href':True}), None)
    	        self.assertNotEqual(article.find('div', attrs={'data-picture':'true', 'data-alt':True}), None)
    	        self.assertNotEqual(article.find('div', attrs={'data-src':True, 'data-media':None}), None)
                self.assertNotEqual(article.find('div', attrs={'data-src':True, 'data-media':'(-webkit-min-device-pixel-ratio: 1.5)'}), None)
                self.assertNotEqual(article.find('noscript').contents, [])
    	    
    	        self.assertNotEqual(article.find('h3', attrs={'class':'lookbookTitle'}).contents, [])
	    	
	    except AssertionError, e:
	    	print article
	    	self.verificationErrors.append(str(u) + " LookBook Failure")
	    	pass
	    
	    u += 1
	    
	self.assertNotEqual(self.soup.find('a', attrs={'class':'readMoreLink raquo','href':'/tags/look%20book/'}).contents, [])    
	self.failUnless(u == 8)
	
        ################################################################################
    	
    def test_bizdev(self):
    	    
    	bizdev = soup.find_all('script')[0]
    	
    	try:
    	    self.failUnless(re.search('zone: "fame"', str(bizdev), re.I))
    	    self.failUnless(re.search('takeover: "fame"', str(bizdev), re.I))
    
        except AssertionError, e:
            results_writer(str(bizdev), "Fame Splash page has a problem with the bizdev script in the header.")
            
    	################################################################################
    	    
    def test_loadmore(self):

        try:
	    self.assertNotEqual(soup.find('a', {'id':'loadMoreEntries', 'class':'galleryOpen'}), None)
	
        except AssertionError, e:
            results_writer("", "Load More button is not on fame splash page")
            
        ################################################################################    
    	 
    def tearDown(self):

        self.assertEqual([], self.verificationErrors)
        
        ################################################################################
        ################################################################################


def page_parser():
	
    req = MyOpener()
    page = req.open(data['url'])
    text = page.read()
    page.close()
    
    return BeautifulSoup(text, from_encoding = 'utf-8')

def results_writer(info, message):
	
    m = open(path, 'a')
    m.write(info + ' ' +  message)
    m.write('\n')
    m.close()

if __name__ =='__main__':

    # Configure environment settings and tests to be run
    C = splashconfig.FameConfig()
    configuration = C.configuration()
    envs = configuration['env']
    path = configuration['path']
    
    # Parse Splash Page for links
    for key in envs.keys():
    	data = envs[key]
        S = splashparser.Splash(data['url'])
        
        S.get_lede_data()
        S.get_article_data()
        parse_data = S.return_data()
        
        # Get corresponding article JSON data for each link and store in dict
        A = article_json_parser
        article = parse_data['article']
        lede = parse_data['lede']
        A.Configure(data['author'], data['usr'], data['pwd'])
        articles = A.Run(article)
        ledes = A.Run(lede)
        
        # Better way to do this?
        global DATA
        DATA = A.D
    

        results_writer(str(datetime.datetime.now()), " BEGINNING FAME SPLASH PAGE TEST")
        results_writer(data['url'], " ")
        soup = page_parser()    
        suite = unittest.TestLoader().loadTestsFromTestCase(FameSplash)
        unittest.TextTestRunner(verbosity=2).run(suite)
        #results = open(path[:-4] + '.html', 'wb')
        #runner = HTMLTestRunner.HTMLTestRunner(stream=results, title="Fame Splash Page", description='Test Results for Fame Splash Page')
        #runner.run(suite)
    
