#! /usr/bin/python

import sys
import re
import httplib
import urllib
import urlparse
import pickle
import string
import time
import html5lib
import Logger
import bs4 as BeautifulSoup
from BeautifulSoup import BeautifulSoup

""" 
NYMAG BeautifulSoup module
This module contains customized, callable functions that scrape www.nymag.com for relevant data.
For example, the relatedstories() function will only pull urls and images, etc. from the related stories section of a given page
Data scraped from the page is pickled and sent to a pickle folder where it is later read by the module test
"""

class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


class Parser():
	
    def __init__(self, baseurl):
    	 
    	 
    	self.BASEURL = baseurl 
    	self.req = MyOpener()
    	self.page = self.req.open(self.BASEURL)
    	self.text = self.page.read()
        self.page.close()
        self.soup = BeautifulSoup(self.text)
        self.spam = self.soup.findAll
        
        self.L = Logger.MainLogger(self.BASEURL, "nymagSoup")   
        
    #########################################################################
  
    def relatedstories(self):
    	    
    	TEST = "Related Stories - nymagSoup"
    	L = self.L    
    	related_dict = {}
    	for tag in self.spam('div', attrs={'class':'relatedstories2 section'}):
    		
    	    section = tag
    	    
    	    link = None
    	    img = None
    	    image = None
    	    permalink = None
    	    title = None
    	    
    	    for tag in section('div', attrs={'class':re.compile('related-story-first')}):
    	    	
                if re.search('href', str(tag), re.I):
    	            L.log("N/A", TEST, "PASS", "Story Found")
    	    		    	    
    	    	else:
    	    	    L.log("N/A", TEST, "FAIL, NO STORY", str(tag.contents))
    	    
    	    for tag in section('div', attrs={'class':re.compile('related-story')}):
    	    	
                if re.search('href', str(tag), re.I):
    	            L.log("N/A", TEST, "PASS", "Story Found")
    	    		    	    
    	    	else:
    	    	    L.log("N/A", TEST, "FAIL, NO STORY", str(tag.contents))
    	    		    	    
            for tag in section('a'):
    	
    	        try:
    	    	    link = tag['href']
    	    	    
    	        except:
    	    	    print "none"
    	    	    
    	        else:
    	    	    contents = tag.contents
    	    	    
    	    	    if len(contents) > 1:
    	    	    	img = tag.contents[1]
    	    	    	    
    	    	        try:
    	    	    	    image = img['src']
    	    	    	    
    	    	        except:
    	    	            pass
    	    	    
    	    	    elif len(tag.contents) == 1:
    	    	    	title = tag.contents[0]    
    	            	
    	    	    
    	        related_dict[link] = (image, title, permalink)
    	   	
        pickle.dump(related_dict, open('../data/pickle/qa.relatedstories.data.p', 'wb'))
        L.save()

#############################################################################
#############################################################################
    
if __name__ == "__main__":
    P = Parser("http://qa.nymetro.com/daily/intel/2012/04/test-for-eve-vl-191.html")
    P.relatedstories()
