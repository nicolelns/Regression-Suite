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
VULTURE BeautifulSoup module
This module contains customized, callable functions that scrape www.vulture.com for relevant data.
For example, the pics() function will only pull urls and images, etc. from the pics section of the home page
Data scraped from the page is pickled and sent to a pickle folder where it is later read by the module test
"""

#BASEURL = raw_input("Enter a BaseURL: ")


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
        
    def SEO(self):
    	    
    	f = open('../data/text/SEO.data.txt', 'r').readlines()
    	
    	SEO_dict = {}
    	n = 0
    	
    	for line in f:
    		
    	    page = f[n].strip('\n')
    		
            self.req3 = MyOpener()
    	    self.page3 = self.req3.open(page)
    	    self.text3 = self.page3.read()
            self.page3.close()
            self.soup3 = BeautifulSoup(self.text3)
            self.spam3 = self.soup3.findAll
    
            for tag in self.spam3('title'):
            	
            	try:
                    title = tag.string
                
                except:
                    title = None
        
            for tag in self.spam3('meta', attrs={'name':"description"}):
                	
                try:
                    description = tag['content']
                
                except:
                    description = None
                
            for tag in self.spam3('meta', attrs={'name':"keywords"}):
                	
                try:
                    keywords = tag['content']

                except:
                    keywords = None
            	    
            SEO_dict[title] = (description, keywords)
            
            n += 1
        
        pickle.dump(SEO_dict, open('../data/pickle/SEO.data.p', 'wb'))
        f.close()
        
    #########################################################################
    
    def ads(self):
    	    
    	f = open('../data/vulture.home.ads.data.txt', 'r')
    	
    	for tag in self.spam('a'):
    	
    	    pass
    	
    	f.close()

    #########################################################################

    def biginterview(self):
    	
    	interview_dict = {}
    	    
    	for tag in self.spam('section', attrs={'id':'feature-secondary-promo'}):    
    		
    	    article = tag
    	    link = None
    	    author = None
    	    image = None
    	    comments = None
    	    
    	    for tag in article('a', attrs={'class':'permalink'}):
    		
    	        try:
    	            link = tag['href']
    	    
                except:
            	    print "none"
            
            for tag in article('img'):
            	    
                try:
    	            image = tag['src']
   
                except:
                    print "none"
                        
            for tag in article('cite'):
                
                author_list = []
                
                try:
                    cite = tag
                    
		    for tag in cite('a'):
                        author = tag['href']
                        author_list.append(author)
            
    		except:
    		    print "none"
    		    	
            interview_dict[link] = (image, comments, author_list)       
                
    	pickle.dump(interview_dict, open('../data/pickle/biginterview.data.p', 'wb'))
    	print interview_dict
        
    #########################################################################
    
    def cpfooter(self):
    	    
        cpfooter_list = []
        
        for tag in self.spam('section', attrs={'class':'general-promo'}):
        	
            cpfooter = tag
            
	    for tag in cpfooter('a'):
			
		try:
		    link = tag['href']
			
		except:
		    print "none"
			
		else:
	            cpfooter_list.append(link)
                
        pickle.dump(cpfooter_list, open('../data/pickle/cpfooter.data.p', 'wb'))
    
    #########################################################################
    
    def masthead(self):
    	    
        editor_list = []
        
        for tag in self.spam('section', attrs={'class':'masthead module module-small'}):
        	
            editor = tag
            
        for tag in editor('a'):
        	
            try:
            	link = tag['href']
            	
            except:
        	print "none"
        	
            else:
                editor_list.append(link)
                
        pickle.dump(editor_list, open('../data/pickle/masthead.data.p', 'wb'))
    
    #########################################################################
    
    def footer(self):
    	    
        footer_list = []
        
        for tag in self.spam('section', attrs={'class':'vulture-promo'}):
        	
            footer = tag
            
        for tag in footer('a'):
        	
            try:
            	link = tag['href']
            	
            except:
        	print "none"
        	
            else:
                footer_list.append(link)
                
        for tag in self.spam('section', attrs={'class':'network-promo'}):
        	
            network_footer = tag
            
        for tag in network_footer('a'):
        	
            try:
            	link = tag['href']
            	
            except:
        	print "none"
        	
            else:
                footer_list.append(link)
                
        pickle.dump(footer_list, open('../data/pickle/footer.data.p', 'wb'))
    
    #########################################################################

    def clickables(self):
    	    
    	clickables_dict = {}
    	a = 0
    	
    	for tag in self.spam('section', attrs={'id':'feature-clickables'}):
    		
    	    clickables = tag
    	    click_class = None
    	    permalink = None
    	
    	    for tag in clickables('article'):
    		
    	        article = tag
    			
    	        try:		
    	            permalink = tag['data-permalink']
    	            click_class = tag['class']
    	    
                except:
    	    	    print 'none'    
          
                a += 1
    	        
    	        clickables_dict[permalink] = (click_class, None)	#Placeholder for comments
    	        
    	pickle.dump(clickables_dict, open('../data/pickle/clickables.data.p', 'wb'))
    	     	
    #########################################################################
    
    def latestnews(self):
    	    
    	news_list = []
    	
    	for tag in self.spam('section', attrs={'class':'latest-news lastest-news-alt1'}):
    		
    	    news = tag
    	
    	for tag in news('a'):
    		
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:	
    	    	news_list.append(link)
    	    	
    	pickle.dump(news_list, open('../data/pickle/latestnews.data.p', 'wb'))
    
    #########################################################################
    
    def partners(self):
    	    
    	self.req2 = MyOpener()
    	self.page2 = self.req2.open('http://nymag.com/partners/feeds/vulture-splash.html')
    	self.text2 = self.page2.read()
        self.page2.close()
        self.soup2 = BeautifulSoup(self.text2)
        self.spam2 = self.soup2.findAll
    	    
    	partners_dict = {}
    	
    	for tag in self.spam2('div', attrs={'class':'content feed'}):
    		
    	    partner = tag['id']
    	    section = tag  
    	    partner_list = []
        
            for tag in section('a'):
    		
    	        try:
    	    	    link = tag['href']
    	    	    foo = tag
    	    
                except:
    	    	    print "none"
    	    
                else:	
            	    for tag in foo('img'):	
                    
                        try:
                    	    img = tag['src']
    
                        except:
	                    print "none"
	                    
                        else:
	                    partner_list.append((link, img))
	                    
	            partner_list.append((link, None))
    
            partners_dict[partner] = partner_list
            
        pickle.dump(partners_dict, open('../data/pickle/partners.data.p', 'wb'))
    
    #########################################################################
    
    def tvrecap(self):
    	    
    	tv_recap_dict = {}
    	show_list = []
    	
    	for tag in self.spam('div', attrs={'class':'parbase tvrecap section'}):
    	
    	    section = tag
    	    
    	for tag in section('article'):
    		
    	    img = None
    	    comments = None
    	    link = None
    	    topic = None
    	    image = None
    	    permalink = None
    	    show = None
    	    
    	    foo = tag
    		
            try:
            	permalink = tag['data-permalink']
            	    
            except:
            	pass
        
            for tag in section('a'):
        	
        	try:
        	    show = tag['href']
        	
                except:
                    pass
            
                if show not in show_list:
                    if not re.search('#tab', show, re.I):
            
                        show_list.append(show)
        
    	    for tag in foo('a'):
    	    	    
    	    	try:
    	    	    link = tag['href']
    	
                except:
                    print "none"
                    
                else:
                    if re.search("Topic Page", str(tag), re.I):
                        topic = link

                    img = tag.contents[0]
                    
                if img is not None:
                    
                    try:
                        image = img['src']
                    	    
                    except:
                        pass
             
            tv_recap_dict[link] = (image, permalink, topic, comments)
                        	
        pickle.dump(tv_recap_dict, open('../data/pickle/tvrecap.data.p', 'wb'))
        pickle.dump(show_list, open('../data/pickle/tvrecap_shows.data.p', 'wb'))
    
    #########################################################################
    
    def starmarket(self):
    	    
    	star_dict = {}
    	
    	for tag in self.spam('div', attrs={'class':'parbase starmarket_gallery section'}):
    	
    	    section = tag
    	    
    	for tag in section('article'):
            
            article = tag
            
    	    img = None
    	    link = None
    	    permalink = None
    	
    	    for tag in article('a'):
    	 
    	        try:
    	    	    link = tag['href']
                except:
    	    	    pass
    	    
                else:
                    if len(tag.contents) > 1:
                    	img = tag.contents[1]
                    	    
                    else:
                    	permalink = tag.contents[0]
                    	
            if img is not None:
            	    
                try:
                    image = img['src']
                
                except:
            	    pass
            
            if re.search('/news/the-star-market/', link, re.I):
            	image = None
            	
            
            star_dict[link] = (image, permalink)
         
        pickle.dump(star_dict, open('../data/pickle/starmarket.data.p', 'wb'))
    
    #########################################################################
    
    def recommends(self):
    	    
    	recommends_dict = {}
    	a = 0
    	    
        for tag in self.spam('div', attrs={'class':'parbase vulturerecommends section'}):
            	
            recommends = tag 
	    recommends_dict['header'] = [('http://www.vulture.com/recommends/', None)]   
            
        for tag in recommends('article'):
        	
            article = tag
            recommends_list = []
            
        for tag in recommends('p'):
            	    
            para = tag
            paragraph = str(para)
            p = paragraph.find("&nbsp;")
            
            if p == -1:
            	p1 = paragraph[11:-4]
            else:
            	p1 = paragraph[3:p]
            	
            recommends_list.append(('paragraph', p1))
            
            if tag in para('a'):
            
                para_link = tag['href']
                recommends_list.append((para_link, "comment"))
            
            for tag in article('a'):

                data = tag

                try:
	            link = tag['href']
        
                except:
	            print "none for recommends"

                else:
            	    
	            for tag in data('img'): 
		     
                        try:
	                    img = tag['src']
	    	
	                except:
    	                    print "none for homepage recommends links"
		
	                else:
	                    recommends_list.append((link, img))
	        
	            if re.search('permalink', str(data), re.I):
	                recommends_list.append((link, "permalink"))
	            
	            else:
	                recommends_list.append((link, None))
	            
	    a += 1
	    recommends_dict[a] = recommends_list
	    
        pickle.dump(recommends_dict, open('../data/pickle/recommends.data.p', 'wb'))
        print recommends_dict
    
    #########################################################################
    
    def newreviews(self):
    	    
    	review_list = []
    	
    	for tag in self.spam('section', attrs={'class':'feature-reviews pretab modtabs startTab0'}):
    		
    	    article = tag
    	    
    	for tag in article('a'):
    		
    	    foo = tag
    	    
    	    try:
    		link = tag['href']
    	    
            except:
    	        print "no links"
    	        
    	    else:
    	    	for tag in article('img'):
    	    	
    	    	    try:
    	    	    	img = tag['src']
    	    	    	
    	    	    except: 	
    	                print "no imgs"
    	             	
    	    if re.search('<img', str(foo), re.I):
    	        review_list.append((link, img))
    	    elif re.search('#tab', str(foo), re.I):
    	        review_list.append((link, "tab"))		
    	    elif re.search('permalink', str(foo), re.I):
    	        review_list.append((link, "permalink"))
    	    else:
    	        review_list.append((link, None))
    	   
        pickle.dump(review_list, open('../data/pickle/newreviews.data.p', 'wb'))	
    
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
    	
    	pickle.dump(pics_dict, open('../data/pickle/pics.data.p', 'wb'))
    	    	
    #########################################################################
    
    def popstories(self):
    	    
    	pop_view_list = []
    	
    	for tag in self.spam('a', attrs={'name':"&lpos=Vulture: HomePage: Most Popular: Most Viewed"}):
    		
    	    try:
    	    	link = tag['href']
    	    except:
    	    	print "none"
    	    else:	
    	    	pop_view_list.append(link)
    	    	
    	    """
    	    Add a section for the most commented links
    	    Add functionality to pull most viewed links/check that they really are the most viewed
    	    """
    	    
    	pickle.dump(pop_view_list, open('../data/pickle/popstories.data.p', 'wb'))
    
    #########################################################################
    
    def tmmatb(self):   # TV, Music, Movies, Art, Theater, Books   
    	    
    	tmmatb_dict = {}
    	x = 0
    	
    	attr = ('first vertical-tv', 'vertical-art', 'first vertical-movies', 'vertical-theater', 'first vertical-music', 'vertical-books')
    	
    	for each in attr:

            for tag in self.spam('section', attrs={'class':attr[x]}):
    	
    	        section = tag
    	        permalink = None
    	        link = None
    	        comment = None
    	        
    	        for tag in section('li', attrs={'class':'entry'}):
    	
		    try:
		        permalink = tag['data-permalink']
                    except:
		        print "none"
		   
                for tag in section('a'):
            	  
                    try:	  
                        link = tag['href']
                
                    except:
		        print "none"
		        
		    if link in tmmatb_dict:
		    	link = link + "^^"
		    	print "Duplicate links:  some urls are in multiple sections", link, attr[x]
		
	            tmmatb_dict[link] = (attr[x], permalink, comment)
	        x += 1
    	pickle.dump(tmmatb_dict, open('../data/pickle/tmmatb.data.p', 'wb'))
    
    #########################################################################
    
    def hottopics(self):
    	    
    	hottopic_dict = {}
    	
    	for tag in self.spam('dl', attrs={'class':"hotTopics"}):
            
            topic = tag
            
            for tag in topic('a'):
            	    
            	img = None
    	        image = None
    	        link = None    
            	    
    	        try:
    	    	    link = tag['href']
    	        except:
    	    	    print "none"
    	        else:
    	    	    if re.search('<img', str(tag), re.I):
    	    	    	img = tag.contents[1]
    	    	    	
    	    	if img is not None:  
    	    		 
                    try:    
    	    	        image = img['src']
    	    	            
    	    	    except:
    	    	        pass
    	          
    	        hottopic_dict[link] = image    	
    	
    	pickle.dump(hottopic_dict, open('../data/pickle/hottopics.data.p', 'wb'))
    	
    #########################################################################
       
    def latesttalk(self):
    	    
    	talk_list = []
    	
    	for tag in self.spam('section', attrs={'class':'vulture-talk'}):
    		
    	    talk = tag
    	
    	    for tag in talk('a'):
    		
    	        try:
    	    	    link = tag['href']
    	    	except:
    	    	    print "none"
    	    	else:	
    	    	    talk_list.append(link)
    	    	
    	pickle.dump(talk_list, open('../data/pickle/latesttalk.data.p', 'wb'))
    
    ######################################################################### 
    
    def smallinterview(self):
    	    
    	interview_list = []    
    	    
    	for tag in self.spam('section', attrs={'class':'promo-feature promo-rubric-interview promo-silo promo-mini'}):
    	
            smallinterview = tag
            
        for tag in smallinterview('a'):
        	
            foo = tag
    		
    	    try:
    	    	link = tag['href']
    	    
            except:
    	    	print "none"
    	    
            else:	
    	    	
    	        for tag in foo('img'):
    	 	 
    	            try:
                        img = tag['src']
    	            
                    except:  
    	     	        print "none"
    	            
                    else:
                    	if re.search('lpos=Vulture: HomePage: Interview module', str(foo), re.I) and not img:
    	    	            interview_list.append((link, None))   
    	    	            
    	    	        else:
    	    	            interview_list.append((link, img))
    	    	            
    	pickle.dump(interview_list, open('../data/pickle/smallinterview.data.p', 'wb'))
    
    #########################################################################
    
    def viralvideo(self):
    	    
    	viral_dict = {}
    	
    	for tag in self.spam('div', attrs={'class':"vulturevideos parbase section"}):
    		
            section = tag
            
            img = None
            image = None
            arrow = None
    	    link = None
    	    arrow_img = None
    	    permalink = None
    	    
        for tag in section('a'):
        	
            header = tag
    	    
    	    try:
    	    	link = tag['href']
    	
            except:
                pass
                    
            else:
                if re.search('video-arrow', str(tag.contents[0]), re.I):
                    arrow = tag.contents[0]
                
                elif re.search('146x97', str(tag.contents[0]), re.I):
                    img = tag.contents[0] 
        	
        	else: 
        	    permalink = tag.contents[0]
        	        
                if img is not None:
            	    
                    try:
                        image = img['src']
                    
                    except:
                        pass
            	    
                if arrow is not None:
            	    
                    try:
                        arrow_img = arrow['src']
            
                    except:
                        pass
            
            if re.search('/news/video/', link, re.I):
            	image = None
            	arrow_img = None
            
            viral_dict[link] = (image, arrow_img, permalink)
            
        pickle.dump(viral_dict, open('../data/pickle/viralvideo.data.p', 'wb'))
        
    #########################################################################
        
    def thefeed(self):
    	
    	feed_dict = {}
    	
    	for tag in self.spam('div', attrs={'class':"vulturefeed parbase section"}):
    		
    	    section = tag	
    	   
        for tag in section('article'):
            
            foo = tag
            img = None
    	    link = None
    	    time = None
    	    permalink = None
    	    image = None
            
            try:
                permalink = tag['data-permalink']
            
            except:
    	        pass
    	
            for tag in foo('li', attrs={'class':'timestamp'}):
            	
                time = tag.string
            	
            for tag in foo('a'):
              	    
                try:
            	    link = tag['href']
    	         
                except:
                    print "none"
                  
                else:
                    if len(tag.contents) == 1:
                        img = tag.contents[0]
                    	   
                if img is not None:
            	    
                    try:
                        image = img['src']
                
                    except:
                        pass
                
                if re.search('www.vulture.com/blog/', link, re.I):
            	    image = None
                
                feed_dict[link] = (image, permalink, time)
            
    	
        pickle.dump(feed_dict, open('../data/pickle/thefeed.data.p', 'wb'))
        
    #########################################################################
    
    def rotatorlede(self):
    	    
    	rotator_dict = {}

        for tag in self.spam('div', attrs={'class':'parbase ledeRotator lederotator'}):
        	
            section = tag
            
            img = None
            image = None
	    link = None
	    topic = None
	    permalink = None
            
	    for tag in section('a'):
		    
		    foo = tag
		    
		    if re.search('class="image"', str(foo), re.I):
			try:
			    permalink = tag['href']
			
			except:
			    pass
		    
			else:
			    if len(tag.contents) > 1:
				img = tag.contents[1]
				
		        if img is not None:
            	    
                            try:
                                image = img['src']
                    
                            except:
                                pass	
			
		    elif re.search('class="headline"', str(foo), re.I):
				
			try:
			    link = tag['href']
			
			except:
			    pass
		    
		    else:
			try:
			    topic = tag['href']
			
			except:
			    pass   
		    
                    rotator_dict[permalink] = (image, link, topic)
            	   
        pickle.dump(rotator_dict, open('../data/pickle/rotatorlede.data.p', 'wb'))
        
    ######################################################################### 
     
    def search(self):
    	    
    	search_dict = {}
        
        for tag in self.spam('span', attrs={'class':'results'}):
        	
            num = tag.string
            #results = results[:-9]
        
        for tag in self.spam('dl', attrs={'class':'result'}):
        	
            results = tag
            
            for tag in results('a'):
            	    
            	link = tag['href']
            	
            for tag in results('li', attrs={"class":"pubDate first>"}):
            	    
            	pub = tag.contents[0]
            	newpub = [pub.strip() for item in pub.split('\n') if item]
            	
            for tag in self.spam('p'):
            	    
            	a_type = tag.string
            	# Needs more work.
            	
            for tag in results('dd', attrs={'class':'dek'}):
            	    
	 	try:    
              	    excerpt = tag.contents[1]
              	    
                except Exception, e:
                    raise
                    
            search_dict[link] = (newpub[0], a_type, excerpt)
            
        if len(search_dict) == 0:
            print "NO RESULTS!"
            return
            
        else:
            return search_dict
    
    #########################################################################
    
    def globalnav(self):
    	    
    	nav_list = []    
    	    
    	for tag in self.spam('nav', attrs={'id':'navGlobal'}):
    	
            foo = tag
            
            for tag in foo('a'):
            	    
    	        try:
    	    	    link = tag['href']
    
                except:
	            raise
	            
	        else:
	            if link != "#":
	            	nav_list.append(link)
                
        return nav_list
        
    #########################################################################    
        
    def utilitynav(self):
    	    
    	# UPDATE XPATH
    	    
    	links = {'http://nymag.com/':('/html/body/div[2]/div/header/nav[2]/div/ul/li/a','http://nymag.com/index.htm','nymag.com', 'New York Magazine -- NYC Guide to Restaurants, Fashion, Nightlife, Shopping, Politics, Movies'), \
    		 'http://nymag.com/nymag/toc/20120625/':('/html/body/div[2]/div/header/nav[2]/div/ul/li[2]/div/ul/li/a', 'http://nymag.com/includes/tableofcontents.htm', 'Table of Contents', 'Table of Contents -- June 25, 2012 Issue of New York Magazine'), \
    		 'https://ssl.palmcoastd.com/03921/apps/-180323?iKey=I**BMD&':('/html/body/div[2]/div/header/nav[2]/div/ul/li[2]/div/ul/li[2]/a', 'http://stg.nymetro.com/redirects/circ_subscribe/utility-bar.html', 'Subscribe Now', 'New York magazine Subscriptions'), \
    		 'https://secure.palmcoastd.com/pcd/eSv?iMagId=03921&i4Ky=IGH5':('/html/body/div[2]/div/header/nav[2]/div/ul/li[2]/div/ul/li[3]/a', 'http://stg.nymetro.com/redirects/circ_gifts/utility-bar.html', 'Give a Gift Subscription', 'https://secure.palmcoastd.com/pcd/eSv?iMagId=03921&i4Ky=IGH5'), \
    		 'http://nym.shopviapcd.com/cart/Home/c-5037.htm':('/html/body/div[2]/div/header/nav[2]/div/ul/li[2]/div/ul/li[4]/a', 'https://secure.palmcoastd.com/pcd/eServCart?iServ=MDM5MjEzODM0Mg==', 'Buy Back Issues', 'New York Magazine Back Issues - Home '), \
    		 'http://nymag.com/nymag/toc/2012/':('/html/body/div[2]/div/header/nav[2]/div/ul/li[2]/div/ul/li[5]/a', 'http://nymag.com/includes/issuearchive.htm', 'Online Issue Archive', '2012 Issue Archive - New York Magazine'), \
    		 'https://ssl.palmcoastd.com/03921/apps/-179080?iCp=A30F9CF5AE439771A8B9887D7B5FB553A767C8F659C5A5B9469E57DB92005402':('/html/body/div[2]/div/header/nav[2]/div/ul/li[2]/div/ul/li[6]/a', 'https://secure.palmcoastd.com/pcd/eServ?iServ=MDM5MjEyNDE2Ng==', 'Customer Service: Contact Us!', 'NEW YORK MAGAZINE - Subscriber Services'),\
    		 'http://mediakit.nymag.com/':('/html/body/div[2]/div/header/nav[2]/div/ul/li[2]/div/ul/li[7]/a', 'http://nymag.com/newyork/mediakit/', 'Media Kit', 'New York Media'), \
    		 #'http://www.vulture.com/':('/html/body/div[2]/div/header/nav[2]/div/ul/li[4]/a', 'http://www.vulture.com', 'Vulture', 'Vulture - Entertainment News - Celebrity News, TV Recaps, Movies, Music, Art, Books, Theater'), \
    		 'http://newyork.grubstreet.com/':('/html/body/div[2]/div/header/nav[2]/div/ul/li[6]/a', 'http://newyork.grubstreet.com/', 'Grub Street', "Grub Street: New York Magazine's Food and Restaurant Blog"), \
    		 'http://stg.nymetro.com/daily/fashion/':('/html/body/div[2]/div/header/nav[2]/div/ul/li[5]/a', 'http://stg.nymetro.com/daily/fashion/', 'The Cut', 'The Cut -- Fashion Week, Models, Street Style, Red Carpet Dresses and Fashion News'), \
               	 'http://stg.nymetro.com/daily/intel/':('/html/body/div[2]/div/header/nav[2]/div/ul/li[3]/a', 'http://stg.nymetro.com/daily/intel/', 'Daily Intel', 'Daily Intel -- New York News -- New York Magazine')} 
    	
    	# When live, change stg.nymetro to nymag
    	return links

    #########################################################################
    
    def mainnav(self):
    	    
    	nav_list = []    
    	    
    	for tag in self.spam('div', attrs={'class':'main navUtil'}):
    	
            foo = tag
            
            for tag in foo('a'):
    		
    	        try:
    	    	    link = tag['href']
    
                except:
	            print "none"
	
                else:
                    if not re.search("http://www.vulture.com", link, re.I):
                        nav_list.append(link)
                
        return nav_list
    
#############################################################################
#############################################################################
    
if __name__ == "__main__":
    P = Parser()
