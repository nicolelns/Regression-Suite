#! /usr/bin/python

import sys
import re
import httplib
import urllib
import urlparse
import pickle
import string
import time
from BeautifulSoup import BeautifulSoup

# VULTURE BeautifulSoup module
# Instead of running the Soup before running tests (to scrape relevant data from www.vulture.com), consider adding soup.py 
# as a module and calling the relevant function.  Example: s. = soup.Parser(), s.SEO, s.ads, etc. and remove main()

BASEURL = 'http://www.vulture.com/'


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


class Parser():
	
    def __init__(self):
    	    
    	self.req = MyOpener()
    	self.page = self.req.open(BASEURL)
    	self.text = self.page.read()
        self.page.close()
        self.soup = BeautifulSoup(self.text)
        self.spam = self.soup.findAll
        
    #########################################################################
        
    def SEO(self):
    	    
    	f = open('../data/vulture.home.SEO.data.txt', 'r').readlines()
    	g = open('../data/vulture.home.SEO.content.txt', 'w')
    	
    	n = 0
    	
    	for line in f:
    		
    	    p = f[n].strip('\n')
    		
            self.req3 = MyOpener()
    	    self.page3 = self.req3.open(p)
    	    self.text3 = self.page3.read()
            self.page3.close()
            self.soup3 = BeautifulSoup(self.text3)
            self.spam3 = self.soup3.findAll
    
            for tag in self.spam3('meta'):
        
                if tag in self.spam3('meta', attrs={'name':"keywords"}):
                    try:
                        keywords = tag['content']
                    
                    except:
                        print "none"
                    
                    else:
                        g.write(keywords + '\n')
                
                elif tag in self.spam3('meta', attrs={'name':"description"}):
                    try:
                        description = tag['content']
                
                    except:	
                        print "none"
                
                    else:
                        g.write(description + '\n')
                        
            n += 1
        
        g.close()
        
    #########################################################################
    
    def ads(self):
    	    
    	f = open('../data/vulture.home.ads.data.txt', 'w')
    	
    	for tag in self.spam('a'):
    	
    	    pass
    	
    	    #if tag in self.spam('a', attrs={'href':'}):
    	
    	f.close()

    #########################################################################

    def biginterview(self):
    	    
    	f = open('../data/vulture.home.biginterview.data.txt', 'w')
    	g = open('../data/vulture.home.biginterview.content.txt', 'w')
    	
    	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Interview module"}):
    		
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:	
    	    	f.write(link + '\n')
    	    	
    	for tag in self.spam('img'):
    	 	 
    	    try:
                img = tag['src']
    	    except:  
    	     	print "none"
    	    else:
    	    	if re.search("160x240", img, re.I):    
    	    	    g.write(img + '\n')
    	    	
    	f.write("http://www.vulture.com/news/chat-room/" + '\n')
    	f.write("/news/chat-room/" + '\n')
    	    		
    	f.close()
    	g.close()

    #########################################################################

    def clickables(self):
    	    
    	f = open('../data/vulture.home.clickables.data.txt', 'w')
    	g = open('../data/vulture.home.clickables.content.txt', 'w')
    	    
    	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Clickables: Logo"}):
    	
            try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:
    	    	f.write(link + '\n')
    	    	
	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Clickables: Stories"}):
    	
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:	
    	    	f.write(link + '\n')
    	    	    
    	g.write("http://images.nymag.com/gfx/sect/vulture/clickables-hp-promo.png" + '\n')
    	    	
    	f.close()
    	g.close()
    	    	
    #########################################################################
    
    def latestnews(self):
    	    
    	f = open('../data/vulture.home.latestnews.data.txt', 'w')
    	
    	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Latest News"}):
    		
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:	
    	    	f.write(link + '\n')
    	    	
    	f.close()
    
    #########################################################################
    
    def partners(self):
    	    
    	self.req2 = MyOpener()
    	self.page2 = self.req2.open('http://nymag.com/partners/feeds/vulture-splash.html')
    	self.text2 = self.page2.read()
        self.page2.close()
        self.soup2 = BeautifulSoup(self.text2)
        self.spam2 = self.soup2.findAll
    	    
    	f = open('../data/vulture.home.partners.data.txt', 'w')
    	g = open('../data/vulture.home.partners.content.txt', 'w')
    	
    	for tag in self.spam2('a'):
    		
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:	
    	    	f.write(link + '\n')
    	    	
    	for tag in self.spam2('img'):
    		
    	    try:
    	    	img = tag['src']
    	    except:
    	    	print "none"
    	    else:	
    	    	g.write(img + '\n')
    	    	
    	f.close()
    	g.close()
    
    #########################################################################
    
    def tvrecap(self):
    	    
    	img_list = []
    	link_list = []
    	    
    	foo = ('logo', 'The Latest', 'Topic Page', 'All Shows')
    	
    	f = open('../data/vulture.home.tvrecap.data.txt', 'w')
    	g = open('../data/vulture.home.tvrecap.content.txt', 'w')
    	
    	for n in range(0,4):
    		
    	    for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: TV Recaps: " + foo[n]}):
    		
    	        try:
    	    	    link = tag['href']
    	    	    
    	        except:
    	    	    pass
    	    	    
    	        else:
    	            if re.search("<img", str(tag)):
    	            	img_list.append(link)
    	            
    	            elif link in img_list:
    	            	link_list.append(link)
    	            
    	            f.write(link + '\n')
    	            
    	    n += 1
    	    	 
        for tag in self.spam('img'): 
    	
    	   try:
               img = tag['src']
    	                  
           except:
    	       pass
    	                   
           else:
    	       if re.search("60x60", img, re.I):
    	    	   g.write(img + '\n')
    	
    	if len(link_list) != len(img_list):
    	    print "ERROR, MISMATCHED LINKS"
    	    print link_list, "LINK LIST"
    	    print img_list, "IMG LIST"
    	    
    	return len(link_list), len(img_list)
    	    	    	
    	f.close()
        g.close()	
    
    #########################################################################
    
    def starmarket(self):
    	    
    	f = open('../data/vulture.home.starmarket.data.txt', 'w')
    	g = open('../data/vulture.home.starmarket.content.txt', 'w')
    	
    	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Star Market"}):
    		
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:	
    	    	f.write(link + '\n')
    	    	
    	for tag in self.spam('img'):
    	 	 
    	    try:
                img = tag['src']
    	    except:  
    	     	print "none"
    	    else:
    	    	if re.search("74x74", img, re.I):
    	    	    g.write(img + '\n')	
    	    		
    	f.close()
    	g.close()
    
    #########################################################################
    
    def recommends(self):
    	    
    	f = open('../data/vulture.home.recommends.data.txt', 'w')
    	g = open('../data/vulture.home.recommends.content.txt', 'w')
    	
    	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Recommends"}):
    		
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:
    	    	if not re.search("<img", str(tag), re.I):
    	            if not re.search("#comment", str(tag)):
    	    	        f.write(link + '\n')
    	    	
    	for tag in self.spam('img'):
    	 	 
    	    try:
                img = tag['src']
    	    except:  
    	     	print "none"
    	    else:
    	    	if re.search("84x84", img, re.I):
    	    	    g.write(img + '\n')
    	    		
    	f.close()
    	g.close()
    
    #########################################################################
    
    def newreviews(self):
    	
    	pages = ("Movies", "Tv", "Music", "Theater", "Books")
    	
    	img_list = []
    	link_list = []
    	n = 0
    	
    	for each in pages:
    		
    	    m = 0	
    	
    	    for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Reviews: " + pages[n]}):
    		
    	        try:
    	    	    link = tag['href']
    	        except:
    	    	    print "none"
    	        else:	
    	    	    if re.search("<img", str(tag)):
    	                img_list.append(link)
    	            
    	            elif link in img_list:
    	                link_list.append(link)
    	            
    	        if m % 2 == 1:	
            	    f.write(link + '\n')
            	    
            	m += 1
            	
            n += 1
    	    	 
        for tag in self.spam('img'):
    	 	 
            try:
                img = tag['src']
    	        
            except:  
    	   	print "none"
    	        
            else:
    	    	if re.search("300x170", img, re.I):
    	            g.write(img + '\n')
    	            
        if len(link_list) != len(img_list):
    	    print "ERROR, MISMATCHED LINKS"
    	    print link_list, "LINK LIST"
    	    print img_list, "IMG LIST"
    	    
    	return len(link_list), len(img_list)
    	    		
    	f.close()
    	g.close()
    
    #########################################################################
    
    def pics(self):
    	    
    	pics_dict = {}
    	a = 0
    	
    	for tag in self.spam('section', attrs={'id':'feature-pics'}):
    		
    	    pics = tag    
    	
    	for tag in pics('article'):
    		
    	    article = tag
    	    pics_list = []
    	    
    	    for tag in article('a'):

                try:
    	    	    link = tag['href']
    	    	    foo = tag
    	        
                except:
    	    	    print "none"
    	        
                else:	
    	    	
    	    	    for tag in foo('img'):
    	    	        img = tag['src']	
    	                pics_list.append((link, img))
    	            	  
    	            if re.search('lpos=Vulture: HomePage: Picture Gallery', str(foo), re.I):
    	                pics_list.append((link, "*"))
    	            	    
    	            elif re.search('/news/slideshow/', link, re.I):    
    	                pics_list.append((link, "See All"))
    	                
    	            else:
    	                pics_list.append((link, None))
    	                    
    	    a += 1
    	        
    	    pics_dict[a] = pics_list
    	    	
    	pics_dict['header'] = [('http://www.vulture.com/news/slideshow/', 'Pics')]
    	
    	pickle.dump(pics_dict, open('../data/vulture.home.pics.data.p', 'wb'))
    	    	
    #########################################################################
    
    def popstories(self):
    	    
    	f = open('../data/vulture.home.popstories.data.txt', 'w')
    	
    	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Most Popular: Most Viewed"}):
    		
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:	
    	    	f.write(link + '\n')
    	    
    	f.close()
    
    #########################################################################
    
    def tmmatb(self):   # TV, Music, Movies, Art, Theater, Books   
    	    
    	# Crawls the TMMATB module for links and writes them to a file
    	    
    	foo = ('tv', 'movies', 'music', 'art', 'theater', 'books')              # Tuple with data, easier than several 'for-loops'
    	y = 0       # Counter for foo
    	
    	f = open('../data/vulture.home.tmmatb.data.txt', 'w')                   # File containing crawled links
    	
    	for each in foo:
    		
    	    f.write("http://www.vulture.com/" + foo[y] + "/" + '\n')
    	    y += 1
    	
    	for x in range(0,6):
    	
            for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Vertical: " + foo[x]}):
			
		try:
		    link = tag['href']
		except:
		    print "none"
		else:	
		    f.write(link + '\n')
				
		x += 1
    	
    	f.close()
    
    #########################################################################
    
    def hottopics(self):
    	    
    	f = open('../data/vulture.home.hottopics.data.txt', 'w')
    	#g = open('../data/vulture.home.hottopics.content.txt', 'w')
    	
    	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Hot Topics"}):
    		
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:	
    	    	f.write(link + '\n')
    	    		
    	f.close()
    	#g.close()
    
    #########################################################################
       
    def latesttalk(self):
    	    
    	f = open('../data/vulture.home.latesttalk.data.txt', 'w')
    	
    	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Latest Talk"}):
    		
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:	
    	    	f.write(link + '\n')
    	    	
    	f.close()
    
    ######################################################################### 
    
    def smallinterview(self):
    	    
    	f = open('../data/vulture.home.smallinterview.data.txt', 'w')
    	g = open('../data/vulture.home.smallinterview.content.txt', 'w')
    	
    	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Interview module"}):
    		
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:	
    	    	f.write(link + '\n')
    	    	
    	for tag in self.spam('img', attrs={"alt":"Placehold Small Silo"}):
    	 	 
    	    try:
                img = tag['src']
    	    except:  
    	     	print "none"
    	    else:
    	    	g.write(img + '\n')
    	    		
    	f.close()
    	g.close()
    
    #########################################################################
    
    def viralvideo(self):
    	    
    	img_list = []
    	link_list = []
    	
    	n = 0
    	    
    	f = open('../data/vulture.home.viralvideo.data.txt', 'w')
    	g = open('../data/vulture.home.viralvideo.content.txt', 'w')
    	
    	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Viral Videos"}):
    		
            try:
            	link = tag['href']
            	    
            except:
            	print "none"
            	
            else:
            	if re.search("<img", str(tag)):
    	            img_list.append(link)
    	            
    	        elif link in img_list:
    	            link_list.append(link)
    	            
    	        if n % 2 == 1:	
            	    f.write(link + '\n')
            	    
            n += 1
            	
        num = len(link_list)*2
        i = 0
        
        for tag in self.spam('img'):
    	 	 
    	    try:
                img = tag['src']
    	        
            except:  
    	     	print "none"
    	        
            else:
    	    	if (re.search("146x97", img, re.I) or re.search("arrow", img, re.I)):
    	            if i < num:
    	    	        g.write(img + '\n')
    	    	        i += 1
    	    	
        if len(link_list) != len(img_list):
    	    print "ERROR, MISMATCHED LINKS"
    	    print link_list, "LINK LIST"
    	    print img_list, "IMG LIST"
    	    
    	return len(link_list), len(img_list)
    	    	
        f.close()
        g.close()
        
    #########################################################################
        
    def thefeed(self):
    	    
    	f = open('../data/vulture.home.thefeed.data.txt', 'w')
    	#g = open('../data/vulture.home.thefeed.content.txt', 'w')
    	
    	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: The Feed: Stories"}):
    		
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:	
    	    	f.write(link + '\n')
        
        f.close()
        
    #########################################################################
    
    def rotatorlede(self):
    	    
    	img_list = []
    	link_list = []
    	
    	f = open('../data/vulture.home.rotatorlede.data.txt', 'w')
    	g = open('../data/vulture.home.rotatorlede.content.txt', 'w')
    	
    	for n in range(1,7):
    		
    	    for tag in self.spam('a', attrs={'name':"&lpos=Vulture: Homepage: Rotating Lede " + str(n)}):
    		
    	        try:
    	    	    link = tag['href']
    	    	    
    	        except:
    	    	    pass
    	    	    
    	        else:
    	            if re.search("<img", str(tag)):
    	            	img_list.append(link)
    	            
    	            elif link in img_list:
    	            	link_list.append(link)
    	            
    	            f.write(link + '\n')
    	            
    	    n += 1
    	    	 
        for tag in self.spam('img'): 
    	
    	   try:
               img = tag['src']
    	                  
           except:
    	       pass
    	                   
           else:
    	       if re.search("480x320", img, re.I):
    	    	   g.write(img + '\n')
    	
    	if len(link_list) != len(img_list):
    	    print "ERROR, MISMATCHED LINKS"
    	    print link_list, "LINK LIST"
    	    print img_list, "IMG LIST"
    	    
    	return len(link_list), len(img_list)
    	    	    	
    	f.close()
        g.close()	
    
    #########################################################################
    
#############################################################################
#############################################################################
    
if __name__ == "__main__":
    main()
