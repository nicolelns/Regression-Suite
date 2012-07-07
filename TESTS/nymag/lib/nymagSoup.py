#! /usr/bin/python

import sys
import re
import httplib
import urllib
import urlparse
import string
import time
import html5lib
import json
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

    ############################################################################
 
    def suggest_date_pickler(self):  
    	    
    	url_list = ["listings/restaurant/la_pizza_fresca/?df=dsgddfgdfghsdgsdghghjghj"]
 
        pickle.dump(url_list, open('../data/pickle/qa.dateUrlList.data.p', 'wb')) 
        
    ############################################################################
    
    def lazy_load(self):
    	 
    	for tag in self.spam('iframe', attrs={'height':'250,300'}):
    		
            try:
            	script = tag['src']
            	
            except Exception, e:
            	print "LAZY LOAD IFRAME NOT FOUND!", str(e)
            	
            else:
            	if re.search("test=true", script, re.I):
            	    print "LAZY LOAD OK"
   
    ############################################################################
            	    
    def utilitynav(self):
    	    
    	links = {'http://nymag.com/':('/html/body/div[2]/div/div/div[2]/div/ul/li/a','http://nymag.com/index.htm','nymag.com', 'New York Magazine -- NYC Guide to Restaurants, Fashion, Nightlife, Shopping, Politics, Movies'), \
    		 'http://nymag.com/nymag/toc/20120625/':('/html/body/div[2]/div/div/div[2]/div/ul/li[2]/div/ul/li/a', 'http://nymag.com/includes/tableofcontents.htm', 'Table of Contents', 'Table of Contents -- '), \
    		 'https://ssl.palmcoastd.com/03921/apps/-180323?iKey=I**BMD&':('/html/body/div[2]/div/div/div[2]/div/ul/li[2]/div/ul/li[2]/a', 'http://nymag..com/redirects/circ_subscribe/utility-bar.html', 'Subscribe Now', 'New York magazine Subscriptions'), \
    		 'https://secure.palmcoastd.com/pcd/eSv?iMagId=03921&i4Ky=IGH5':('/html/body/div[2]/div/div/div[2]/div/ul/li[2]/div/ul/li[3]/a', 'http://nymag.com/redirects/circ_gifts/utility-bar.html', 'Give a Gift Subscription', 'https://secure.palmcoastd.com/pcd/eSv?iMagId=03921&i4Ky=IGH5'), \
    		 'http://nym.shopviapcd.com/cart/Home/c-5037.htm':('/html/body/div/div[2]/div/div[2]/div/ul/li[2]/div/ul/li[4]/a', 'https://secure.palmcoastd.com/pcd/eServCart?iServ=MDM5MjEzODM0Mg==', 'Buy Back Issues', 'New York Magazine Back Issues - Home '), \
    		 'http://nymag.com/nymag/toc/2012/':('/html/body/div/div[2]/div/div[2]/div/ul/li[2]/div/ul/li[5]/a', 'http://nymag.com/includes/issuearchive.htm', 'Online Issue Archive', '2012 Issue Archive - New York Magazine'), \
    		 'https://ssl.palmcoastd.com/03921/apps/-179080?iCp=A30F9CF5AE439771A8B9887D7B5FB553A767C8F659C5A5B9469E57DB92005402':('/html/body/div/div[2]/div/div[2]/div/ul/li[2]/div/ul/li[6]/a', 'https://secure.palmcoastd.com/pcd/eServ?iServ=MDM5MjEyNDE2Ng==', 'Customer Service: Contact Us!', 'NEW YORK MAGAZINE - Subscriber Services'),\
    		 'http://mediakit.nymag.com/':('/html/body/div/div[2]/div/div[2]/div/ul/li[2]/div/ul/li[7]/a', 'http://nymag.com/newyork/mediakit/', 'Media Kit', 'New York Media'), \
    		 'http://www.vulture.com/':('/html/body/div[2]/div/div/div[2]/div/ul/li[3]/a', 'http://www.vulture.com', 'Vulture', 'Vulture - Entertainment News - Celebrity News, TV Recaps, Movies, Music, Art, Books, Theater'), \
    		 'http://newyork.grubstreet.com/':('/html/body/div/div[2]/div/div[2]/div/ul/li[4]/a', 'http://newyork.grubstreet.com/', 'Grub Street', "Grub Street: New York Magazine's Food and Restaurant Blog"), \
    		 'http://nymag.com/daily/fashion/':('/html/body/div[2]/div/div/div[2]/div/ul/li[5]/a', 'http://nymag.com/daily/fashion/', 'The Cut', 'The Cut -- Fashion Week, Models, Street Style, Red Carpet Dresses and Fashion News'), \
               	 'http://nymag.com/daily/intel/':('/html/body/div/div[2]/div/div[2]/div/ul/li[6]/a', 'http://nymag.com/daily/intel/', 'Daily Intel', 'Daily Intel -- New York News -- New York Magazine')} 
    	
    	return links
    		 
 
#############################################################################
#############################################################################
    
if __name__ == "__main__":
	
	main()
