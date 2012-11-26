#! /usr/bin/python                                                                                                                                                                                  
# -*- coding: utf-8 -*-

import sys
import os
import re
import httplib
import urllib
import urlparse
import unittest
import time
import datetime
from bs4 import BeautifulSoup


reload(sys)
sys.setdefaultencoding("utf-8")


"""
Author:  Nicole Smith 2012; New York Magazine

Purpose:  This test checks for missing images on articles on production
This code will open a page and check for the presence of <div> tags containing
media queries.  No clicking or other interaction with the page is necessary.

Pass:  Article has all <div> tags
Fail:  Article does not have <div> tags or has incorrect image path

"""

URLS = open('/Users/nsmith/Desktop/articlesnoimages.txt', 'r').readlines()


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'
    

class ArticleImage(unittest.TestCase):
	
    def setUp(self):
    	    
    	self.verificationErrors = []
    	
        ################################################################################
   

    def test_div_wrap(self):
    	
    	try:
    	    self.assertNotEqual(soup.find('div', {'class':'image primaryImageWrap'}), None)
    	    
        except AssertionError:
            results_writer(url, " is missing primary image wrap div tag.")	
        
    def test_data_picture(self):
    	
    	try:
    	    self.assertNotEqual(soup.find('div', {'data-picture':'true', 'data-assetnodepath':True, 'data-alt':True}), None)
    	
    	except AssertionError:
            results_writer(url, " is missing data picture div tag.")
            
    def test_data_source_main(self):
    	 
    	try: 
    	    self.assertNotEqual(soup.find('div', {'data-picture':True, 'data-media':False}), None)
    	
    	except AssertionError:
            results_writer(url, " is missing main data source div tag.")
            
    def test_data_source_mobile(self):
    	   
    	try:
            self.assertNotEqual(soup.find('div', {'data-picture':True, 'data-media':'(max-width: 600px)'}), None)
    	
    	except AssertionError:
            results_writer(url, " is missing data source div tag for mobile.")
            
    def test_data_source_mobile_retina(self):
    	   
    	try:
            self.assertNotEqual(soup.find('div', {'data-picture':True, 'data-media':'(max-width: 600px) and (min-device-pixel-ratio: 1.5)'}), None)
    	
    	except AssertionError:
            results_writer(url, " is missing data source div tag for mobile retina.")
            
    def test_data_source_tablet(self):
    	   
    	try:
            self.assertNotEqual(soup.find('div', {'data-picture':True, 'data-media':'(min-width: 601px) and (max-width: 800px)'}), None)
    	
    	except AssertionError:
            results_writer(url, " is missing data source div tag for tablet.")
    
    def test_data_source_tablet_retina(self):
    	   
    	try:
            self.assertNotEqual(soup.find('div', {'data-picture':True, 'data-media':'(min-width: 601px) and (max-width: 800px) and (min-device-pixel-ratio: 1.5)'}), None)
    	
    	except AssertionError:
            results_writer(url, " is missing data source div tag for tablet retina.")
            
    def test_data_source_desktop(self):
    	   
    	try:
            self.assertNotEqual(soup.find('div', {'data-picture':True, 'data-media':'(min-width: 801px)'}), None)
    	
    	except AssertionError:
            results_writer(url, " is missing data source div tag for desktop.")
    
    def test_data_source_desktop_retina(self):
    	   
    	try:
            self.assertNotEqual(soup.find('div', {'data-picture':True, 'data-media':'(min-width: 801px) and (min-device-pixel-ratio: 1.5)'}), None)
    	
    	except AssertionError:
            results_writer(url, " is missing data source div tag for desktop retina.")
            
    def test_noscript(self):
    	   
    	try:
            self.assertNotEqual(soup.find('noscript'), None)
    	
    	except AssertionError:
            results_writer(url, " is missing noscript tag.")
            
    def tearDown(self):

        self.assertEqual([], self.verificationErrors)
        
        ################################################################################
        ################################################################################

def page_parser(url):
	
    req = MyOpener()
    page = req.open(url)
    text = page.read()
    page.close()
    
    return BeautifulSoup(text, from_encoding = 'utf-8')
    
def results_writer(info, message):
	
    m = open('/Users/nsmith/Desktop/article_image_fail.txt', 'a')
    m.write(info + ' ' +  message)
    m.write('\n')
    m.close()
    
if __name__ =='__main__':
    
    results_writer(str(datetime.datetime.now()), " BEGINNING MISSING ARTICLE IMAGE TEST")
    
    for url in URLS:
        soup = page_parser(url)
        results_writer(url, " ") 
        suite = unittest.TestLoader().loadTestsFromTestCase(ArticleImage)
        unittest.TextTestRunner(verbosity=2).run(suite)
