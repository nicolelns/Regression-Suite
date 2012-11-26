#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import urllib
import urlparse
import sys
import unittest
import time
import re
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

STG = 'http://stg.nymetro.com/thecut/runway/'
EC2 = 'http://ec2.qa.nymetro.com/thecut/runway/'
PROD = 'http://nymag.com/thecut/runway/'

class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'
    

class GetShows():
	
    def __init__(self):
    	    
    	self.BASEURL = BASEURL    
    	self.req = MyOpener()
    	self.page = self.req.open(self.BASEURL)
    	self.text = self.page.read()
        self.page.close()
        self.soup = BeautifulSoup(self.text)
        self.spam = self.soup.find_all
        
        self.f = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/' + ENV + '.runway_shows.txt', 'w')
        print self.BASEURL
        ########################################################################
        
    def get_shows(self):
    	    
        for tag in self.spam('a', attrs={'class':'designerLink'}):
    		
    	    designer = tag['href']
    	    self.f.write(designer + '\n')
    	    
        self.f.close()
    	    
        ########################################################################
         
for x in range(0,3):
	
    if x == 0:
    	BASEURL = STG
    	ENV = 'stg'	
    
    elif x == 1:
    	BASEURL = EC2
    	ENV = 'ec2'
        
    else:
    	BASEURL = PROD
    	ENV = 'prod'
    
    
    g = GetShows()
    g.get_shows()
    
    x += 1
