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

e = open('/Users/nsmith/Desktop/publishresults.txt', 'a')

class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'
    

class PublishTest():
	
    def __init__(self, pub_url, PUB):
    	    
    	self.pub_url = pub_url
    	self.PUB = PUB
    	self.html = []
    	self.make_publish_urls()
    	
        ########################################################################
        
    def make_publish_urls(self):
    	    
        self.publist = [self.pub_url[:15] + str(n) + self.pub_url[16:] for n in range(1,int(self.PUB) + 1)]
    
        ########################################################################
    
    def get_src(self):
    	
    	for url in self.publist:
    	    self.req = MyOpener()
    	    self.page = self.req.open(url)
    	    self.text = self.page.read()
            self.page.close()
            self.soup = BeautifulSoup(self.text)
            self.spam = self.soup.find_all
            tag = self.soup('body')
    	    string = str(tag[0])
    	    self.html.append(string) 
    	return self.html
    	
        ########################################################################
   
    def instance_test(self):
    	
    	time = datetime.datetime.now()
        t = time.strftime("%Y/%m/%d-%H:%M:%S")
    	
    	data = self.get_src()
    	
        for n in range(0,len(data) - 1):
            result = list(difflib.unified_diff(data[0], data[n + 1], lineterm=''))
            if result != []:
            	print '\n'.join(result), "NEW RESULT"
                self.results_writer('\n'.join(result), "PUBLISH 0" + str(int(self.PUB) - len(data)) + " vs. PUBLISH0" + str(n + 1), t)
            n += 1    
            self.publist.pop(0)
                
        ########################################################################
    
    def results_writer(self, data, string, time):
    	
    	e = open('/Users/nsmith/Desktop/publishresults.txt', 'a')
    	
    	self.d = str(data)
    	self.s = string
    	self.t = time
    	
    	e.write(self.s + '\t' + self.t)
    	e.write('\n')
    	e.write('_________________________________________')
        e.write(self.d)
        e.write('\n')
        e.close()
        
    ########################################################################
    
def main(url, PUB):
	
    """
    Open the publishurls.txt file and for each url in the file, create a version of
    the url for each publisher.  Example:  http://publish01.nymetro.com:4502/content/<slug>
    would become publish02.nymetro... etc.  Pass these urls to the PublishSrc class
    to open and parse each page.
    
    """
	
    print url + " is being tested!"	
    time = datetime.datetime.now()
    t = time.strftime("%Y/%m/%d-%H:%M:%S")
    
    P = PublishTest(url, PUB)    
    P.results_writer("STARTING PUBLISH TEST", str(url.split(':')[-1]), t)    
    P.instance_test()
    
    
if __name__ == '__main__':
    
    flag = 1
    while flag == 1:
    	    
    	PUB = raw_input('How many publishers are there? (Enter a digit from 1-99 and hit Return):')
    	
        try:
            type(PUB) is int
            	
        except ValueError:
    	    print "That was not valid input, try again"
    	    
        else:
    	    flag = 0
    	    
        f = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/publishurls.txt', 'r').readlines()
    
        for url in f:
    	    main(url, PUB)
    
    
    
    
