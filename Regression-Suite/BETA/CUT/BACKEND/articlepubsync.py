#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import urllib
import urlparse
import sys
import datetime
import re
import difflib
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

e = open('/Users/nsmith/Desktop/articlepublishresults.txt', 'a')

class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'
    

class PublishSrc():
	
    def __init__(self, pub_url):
    	    
    	self.pub = pub_url 
    	self.req = MyOpener()
    	self.page = self.req.open(self.pub)
    	self.text = self.page.read()
        self.page.close()
        self.soup = BeautifulSoup(self.text)
        self.spam = self.soup.find_all
        self.link_list = []
        
        self.get_src()
        
        ########################################################################
        
    def get_src(self):
    	    
        tag = self.soup('body')
    	string = str(tag[0])
    	publist.append(string)
    	
        ########################################################################
   
    def make_article_files(self):
    	    
    	p = 1
        for each in self.link_list:
            
            g = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/publish0' + str(p) + '.ARTICLES.txt', 'w')
            g.write(each)
            g.write('\n')
            g.close
            p += 1
        
	########################################################################
        
    def article_instance_test(self):
    	    
    	#Don't repeat yourself - refactor into loops later
    	
    	time = datetime.datetime.now()
        t = time.strftime("%Y/%m/%d-%H:%M:%S")
    	
        _1 = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/publish01.ARTICLES.txt', 'r').readlines()
        _2 = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/publish02.ARTICLES.txt', 'r').readlines()
        _3 = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/publish03.ARTICLES.txt', 'r').readlines()
        _4 = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/publish04.ARTICLES.txt', 'r').readlines()
        _5 = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/publish05.ARTICLES.txt', 'r').readlines()
        _6 = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/publish06.ARTICLES.txt', 'r').readlines()
        
        html = (_1, _2, _3, _4, _5, _6)
        p = 1
        
        for each in html:
        
            result1 = list(difflib.unified_diff(each, _1, lineterm=''))
            result2 = list(difflib.unified_diff(each, _2, lineterm=''))
            result3 = list(difflib.unified_diff(each, _3, lineterm=''))
            result4 = list(difflib.unified_diff(each, _4, lineterm=''))
            result5 = list(difflib.unified_diff(each, _5, lineterm=''))
            result6 = list(difflib.unified_diff(each, _6, lineterm=''))
            
            if result1 != []:
                self.results_writer('\n'.join(result1), "PUBLISH 0" + str(p) + " vs. PUBLISH01", t)
            if result2 != []:
            	self.results_writer('\n'.join(result2), "PUBLISH 0" + str(p) + " vs. PUBLISH02", t)
            if result3 != []:
	        self.results_writer('\n'.join(result3), "PUBLISH 0" + str(p) + " vs. PUBLISH03", t)
            if result4 != []:    
                self.results_writer('\n'.join(result4), "PUBLISH 0" + str(p) + " vs. PUBLISH04", t)
            if result5 != []:
                self.results_writer('\n'.join(result5), "PUBLISH 0" + str(p) + " vs. PUBLISH05", t)
            if result6 != []:
                self.results_writer('\n'.join(result6), "PUBLISH 0" + str(p) + " vs. PUBLISH06", t)
                
            p += 1    
                    
    ########################################################################
    
    def results_writer(self, data, string, time):
    	
    	#e = open('/Users/nsmith/Desktop/articlepublishresults.txt', 'a')
    	
    	self.l = str(data)
    	self.s = string
    	self.t = time
    	
    	e.write(self.s + '\t' + self.t)
    	e.write('\n')
    	e.write('_________________________________________')
        e.write(self.l)
        e.write('\n')
        e.close()
        
    ########################################################################
    
f = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/articlepublishurls.txt', 'r').readlines()

def link_formatter(link):
    	    
    	s = link.split('/')    
    	slug = '/' + s[-3] + '/' + s[-2] + '/' + s[-1]
    	
    	if re.search('vulture', str(link)):
            base = 'http://publish01.nymetro.com:4502/content/nymag/daily/entertainment'
        elif re.search('thecut', str(link)):
            base = 'http://publish01.nymetro.com:4502/content/nymag/daily/fashion'
        elif re.search('entertainment', str(s[-4])):
            base = 'http://publish01.nymetro.com:4502/content/nymag/daily/entertainment'
        elif re.search('intel', str(s[-4])):
            base = 'http://publish01.nymetro.com:4502/content/nymag/daily/intel'
        elif re.search('sports', str(s[-4])):
            base = 'http://publish01.nymetro.com:4502/content/nymag/daily/sports'
        elif re.search('movies', str(link[-4])):
            base = 'http://publish01.nymetro.com:4502/content/nymag/daily/entertainment'
        elif re.search('fashion', str(s[-4])):
            base = 'http://publish01.nymetro.com:4502/content/nymag/daily/fashion'    
        else:
            print "LINK NOT CONVERTED!", self.link
        
        formatted = base + slug
        print formatted, "FORMATTED"
        
    	return formatted
    	
for url in f:
	
    print str(url) + " is being tested!"	
    publist = []
    formatted_link = link_formatter(url)
    for n in range(1,7):
    	u = formatted_link.strip('\n')
        pub_inst = u[:15] + str(n) + u[16:]
        P = PublishSrc(pub_inst)
        
        n += 1
        
    time = datetime.datetime.now()
    t = time.strftime("%Y/%m/%d-%H:%M:%S")
    
    P.make_files()
    P.results_writer("", str(pub_inst.split(':')[-1]), t)    
    P.instance_test()
    print str(url) + " is done."

e.close()    
    
    
    
