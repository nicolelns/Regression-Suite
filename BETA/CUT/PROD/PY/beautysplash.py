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


class BeautySplash(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
    
        ################################################################################
        
    def json_organizer(self, _json):
        
        self.j = json.loads(_json)
        
        self.entry_type = self.j['entryType']
        self.feature_type = self.j['featureTypes']
        self.desc = self.j['jcr:description']
        self.title = self.j['jcr:title']
        
	self.i = self.j['primary_image'].split('.jpg')
        self.img = self.i[0]
        
        self.shorthead = self.j['shorterheadline']
        self.excerpt = self.j['excerpt']
        
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
	    dots = soup.find_all('ol', {'class':'ledeMarkers'})
    
        except KeyError, e:
            results_writer(str(u) + "articles in lede " + str(len(dots)) + " lede article markers", " Beauty lede markers fail.")
            
	self.assertEqual(int(self.u), len(dots))
    
    	################################################################################    
        
    def test_text(self):
    	  
    	try:  
    	    self.assertEqual(soup.find('h3').string, "Beauty Newsfeed")
    	    
        except KeyError, e:
            results_writer("", "Beauty Newsfeed Text in header does not match 'Beauty Newsfeed'")
        
        except AssertionError, e:
            results_writer("", "Beauty Newsfeed Text Not on page")
            	    
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
	    	
	    except KeyError:
	    	results_writer(link, "Link is missing from dataset.")
	    	pass
	
            else:
            	    
            	img_dataset = (('div', {'class':'ledeImage'}),
            	    ('div', {'data-picture':'true', 'data-alt':self.shorthead}),	
            	    ('div', {'data-src':str(self.img) + '.jpg/a_4x-horizontal.jpg'}),
            	    ('div', {'data-src':str(self.img) + '.jpg/a_3x-horizontal.jpg', 'data-media':'(max-width: 600px)'}),
            	    ('div', {'data-src':str(self.img) + '.jpg/a_4x-horizontal.jpg', 'data-media':'(min-width: 601px)'}),
            	    ('a', {None:None})
            	    )
            	
	        for arg in img_dataset:
    	            # Media Queries/Images
    	            try:
    	    	        self.assertNotEqual(self.key_test(arg), None)
    	        
    	            except AssertionError, e:
    	                results_writer(self.shorthead,  'failed.  Check the media queries for the lede on the beauty splash page.')
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
    	                results_writer(self.shorthead,  'failed.  Check the header for the lede on the beauty splash page.')
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
    	        results_writer(str(arg),  'failed.  Check the prev/next arrows for the lede on the beauty splash page.')
    	        pass
    	
    	################################################################################
    	    
    def test_metadata(self):
    	    
    	#Metadata test
    	
    	self.assertTrue('Beauty Tips and Products: Makeup, Hair, Skincare, Fragrances - TheCut' in soup.find('title').string)
    	
    	dataset = (('meta', {'name':'description', 'content':'Critical and obsessive, our beauty team reports on the latest beauty trends, reviews new beauty products, and shares tips on how to apply makeup, create hairstyles, take care of your skin, and more.'}), 
    	    ('meta', {'name':'keywords', 'content':'fitness,skincare,nails,fragrance,beauty,makeup,hair'}),
    	    ('meta', {'name':'content.hierarchy', 'content':'The Cut:Beauty:Index'}),
    	    ('meta', {'name':'content.hierarchy.title', 'content':'The Cut Beauty'}),
    	    ('meta', {'name':'content.source', 'content':'Online'}),
    	    ('meta', {'name':'content.type', 'content':'Index'}),
    	    ('link', {'rel':'canonical', 'href':'http://nymag.com/thecut/beauty/'})
    	)
    	
    	for arg in dataset:
    	    
    	    try:
    	    	self.assertNotEqual(self.key_test(arg), None)
    	        
    	    except AssertionError, e:
    	        results_writer(str(arg),  'failed.  Check the metadata on the beauty splash page.')
    	        pass
    	
        ################################################################################

    def test_lpos(self):
    	    
    	#Test for Omniture link positions
    	
    	lpos = re.compile('&lpos.*')
    	
    	try:
    	    self.assertNotEqual(soup.find_all('a', {'name':lpos}), [])
    	    
        except AssertionError:
            results_writer("Beauty Splash Page", " Link positioning not on beauty splash page!")
            	    
    	################################################################################    
      	    
    def test_entries(self):
    	    
    	#Entries
    	
    	u = 0
    	
    	for tag in soup.find_all('article', {'class':'feedEntry', 'id':'entry', 'data-publish-datetime':True}):
    	    
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
	    	
	    except KeyError:
	    	results_writer(link, "Link is missing from dataset.")
	    	pass
	
            else:
            	
            	dataset = (('div', {'class':'featureImage'}),
    		('div', {'data-picture':'true'}),
    		('div', {'data-src':str(self.img) + '.jpg/a_3x-square.jpg',}),
    		('div', {'data-src':str(self.img) + '.jpg/a_1x-square.jpg', 'data-media':'(max-width: 600px)'}),
    		('div', {'data-src':str(self.img) + '.jpg/a_3x-square.jpg', 'data-media':'(min-width: 601px)'}),
    		('a', {'href':link})
    		)
            	
	        for arg in dataset:
    	            # Media Queries/Images
    	            try:
    	    	        self.assertNotEqual(self.key_test(arg), None)
    	        
    	            except AssertionError, e:
    	                results_writer(self.shorthead,  'failed.  Check the media queries for entries on the beauty splash page.')
    	                pass
    	        
		try:
	            # Noscript
	            self.assertNotEqual(tag.find('noscript').contents, [])
	            
	        except KeyError, e:
	    	    results_writer(self.shorthead, "noscript tag not found - Front End.")
	    	    
	    	except AssertionError, e:
	    	    results_writer(self.shorthead, "Media query missing noscript data - Front End.")
	    	    
                try:
                    # Header
    	            tag.find('header')
    	        
    	        except KeyError, e:
                    results_writer(self.shorthead, "Header tag is not appearing on page - Front End.")
            
                try:
    	            # Timestamp
    	            tag.find('li', {'class':'metaTime'}).text
    	            
    	        except AttributeError, e:
                    results_writer(self.shorthead, "Timestamp is not appearing on page - Front End.")
            
                # Feature Rubric
                if self.feature_rub is not None:
    	            try:
    	            	re.search(tag.find('li', {'class':self.caps_feature_rub}).text, self.feature_rub, re.I)
    	            
                    except:    
                        results_writer("Article: " + self.shorthead, 'The feature rubric, ' + self.feature_rub +
		            	           " in the article has a problem - Rubric exists in CQ - Back End.")
    	              
    	    u += 1
    	
    	try:
    	    self.assertEqual(u, 10)
    	    
        except AssertionError:
            results_writer(str(u), " articles on beauty splash page.  Fail.")
     	
        ################################################################################
    	
    def test_bizdev(self):
    	    
    	bizdev = soup.find_all('script')[0]
    	
    	try:
    	    self.failUnless(re.search('zone: "beauty"', str(bizdev), re.I))
    	    self.failUnless(re.search('takeover: "beauty"', str(bizdev), re.I))
    
        except AssertionError, e:
            results_writer(str(bizdev), "Beauty Splash page has a problem with the bizdev script.")
            
    	################################################################################
    	    
    def test_loadmore(self):

        try:
	    self.assertNotEqual(soup.find('a', {'id':'loadMoreEntries', 'class':'galleryOpen'}), None)
	
        except AssertionError, e:
            results_writer("", "Load More button is not on beauty splash page")
            
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
    
    return BeautifulSoup(text)

def results_writer(info, message):
	
    m = open(path, 'a')
    m.write(info + ' ' +  message)
    m.write('\n')
    m.close()

if __name__ =='__main__':

    # Configure environment settings and tests to be run
    C = splashconfig.BeautyConfig()
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
    

        results_writer(str(datetime.datetime.now()), " BEGINNING BEAUTY SPLASH PAGE TEST")
        results_writer(data['url'], " ")
        soup = page_parser()    
        suite = unittest.TestLoader().loadTestsFromTestCase(BeautySplash)
        unittest.TextTestRunner(verbosity=2).run(suite)
        #results = open(path[:-4] + '.html', 'wb')
        #runner = HTMLTestRunner.HTMLTestRunner(stream=results, title="Beauty Splash Page", description='Test Results for Beauty Splash Page')
        #runner.run(suite)
    
