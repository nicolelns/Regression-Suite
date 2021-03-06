#! /usr/bin/python

import sys
import re
import httplib
import urllib
import urlparse
import pickle
import string
import time
import json
from bs4 import BeautifulSoup

""" 
THE CUT BeautifulSoup module
This module contains customized, callable functions that scrape www.nymag.com for relevant data.
For example, the pics() function will only pull urls and images, etc. from the pics section of the home page
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
        self.spam = self.soup.find_all
        
    #########################################################################
  
    def qa_celebrity_splash_feed(self):
    	
    	feed_dict = {}
    	f = open('../data/json/cut.json').read()
    	data = json.loads(f)
    	keys = data.keys()
    	values = data.values()
    	
    	for tag in self.spam('article', attrs={'class':'feedEntry'}):
    	
    	    feed = tag
    	    img = None
    	    link = None
            image = None
    	    
    	    for tag in feed('a'):
    	      
                try:
    	    	    link = tag['href']
    	    	    
    	        except:
    	    	    print "none"
    	    	    
    	        else:
    	    	    if len(tag.contents) > 0:
    	    	        img = tag.contents[0]
    	    	    
    	        if img is not None:
    	    	      
    	            try:
    	                image = img['src']
    	        
                    except:
    	                pass
    	          
                if link != "javascript:;":
    	        
                    if link in keys:
            	        details = data.get(link)
            
        	    detail_keys = details.keys()
        	    detail_values = details.values()
        	    
                    feed_dict[link] = (image, detail_values[0], detail_values[1], detail_values[2], detail_values[3])
             	
        pickle.dump(feed_dict, open('../data/pickle/qa.celebritysplashfeed.data.p', 'wb'))
        
    #########################################################################
  
    def qa_celebrity_splash_lede(self):
    	   
    	lede_dict = {}
    	f = open('../data/json/cut.json').read()
    	data = json.loads(f)
    	keys = data.keys()
    	values = data.values()
    	
    	for tag in self.spam('article', attrs={'class':'ledeArticle'}):
    	  
    	    img_list = []
    	    lede = tag
    	    img = None
    	    link = None
            image = None
    	    
    	    for tag in lede('a'):
    	      
                try:
    	    	    link = tag['href']
    	    	    
    	        except:
    	    	    print "none"
    	    	    
    	        for tag in lede('source'):
    	    	    
    	    	    try:
    	    	        img = tag['src']
    	    	    	    
    	    	    except:
    	    	        pass
    	    	    
		    else:
    	    	        if img not in img_list:
    	    		    img_list.append(img)
    	    	
	        if link != "javascript:;":
	
	            if link in keys:
		        details = data.get(link)
		        detail_keys = details.keys()
		        detail_values = details.values()
	    
	                lede_dict[link] = (img_list, detail_values[0], detail_values[1], detail_values[2], detail_values[3])
        
        pickle.dump(lede_dict, open('../data/pickle/qa.celebritysplashlede.data.p', 'wb'))  
            	    
    #########################################################################	    	    
    	  
#############################################################################
#############################################################################
    
if __name__ == "__main__":
    p = Parser('http://ec2.qa.nymetro.com/thecut/celebrity/')
    p.qa_celebrity_splash_lede()
