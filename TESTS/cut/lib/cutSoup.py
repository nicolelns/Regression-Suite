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
    
    def image_rendition_tool(self):
    	    
    	image_dict = {}
    	pass
    	
    	"""
    	for tag in self.spam('img'):
    	
    	    try:
    	        src = tag['src']
    	        alt = tag['alt']
    	   
    	    except Exception, e:
    	        src = None
    	        alt = None

            image_dict[src] = alt
    	    
    	    x += 1
    	
    	pickle.dump(image_dict, open('../data/pickle/imagerendition.data.p', 'wb'))
    	
    	"""
    	
       #########################################################################
    	
    def feed(self):
    	
    	blog_feed_dict = {}
    	n = 0
    	
    	for tag in self.spam('div', attrs={'class':"parbase newsfeed"}):
    		
    	    section = tag
    	    d_img = None
    	    m_img = None
    	    link = None
    	    t_img = None
    	    comment = None
    	    time = None
    	    p = None
    	    header = None
    	    
            for tag in section('article', attrs={'class':'entry'}):
            
                foo = tag
                
                for tag in foo('img', attrs={'class':'hidden imageDesktop'}):
            
                    try:
                    	d_img = tag['src'] # d is for desktop
		    
		    except:
			pass
		
                for tag in foo('img', attrs={'class':('hidden imageTablet')}):
            
                    try:
		        t_img = tag['src'] # t is for tablet
		    
		    except:
			pass
		
    		for tag in foo('img', attrs={'class':'hidden imageMobile'}):
            
                    try:
		        m_img = tag['src'] # m is for mobile
		    
		    except:
			pass
		
    		for tag in foo('li', attrs={'class':'listItem timestamp'}):
            
                    try:
		        time = tag.string
		    
		    except:
			pass
			
		for tag in foo('a', attrs={'class':'permalink'}):
			
		    try:
		    	link = tag['href']
		    
		    except:
			pass
		
                for tag in foo('li', attrs={'class':'listItem articleCommentCount'}):
            	
            	   try:
	 	       comment = tag.string
			    
		   except:
		       pass
		       
		for tag in foo('h3', attrs={'class':'permalinkWrap'}):
            	
            	   try:
	 	       header = tag.string
			    
		   except:
		       pass
		       
	        for tag in foo('p', attrs={'class':'articleText'}):
	        	
	            try:
	            	p = tag.contents
	            	
	            except:
	            	pass
	            	  
		blog_feed_dict[link] = (header, (d_img, t_img, m_img), comment, time, p)
	            
	return blog_feed_dict
   
       #########################################################################	    
    	    
            
    	  
#############################################################################
#############################################################################
    
if __name__ == "__main__":
    main()
