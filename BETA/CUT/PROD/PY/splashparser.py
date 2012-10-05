#! /usr/bin/python                                                                                                                                                                                  
# -*- coding: utf-8 -*-

import sys
import os
import re
import httplib
import urllib
import urlparse
import string
import time
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


class Splash():

    def __init__(self, baseurl):

        self.baseurl = baseurl
        
        self.data = {'lede':[], 'article':[]}
        
        self.req = MyOpener()
        self.page = self.req.open(self.baseurl)
        self.text = self.page.read()
        self.page.close()
        self.soup = BeautifulSoup(self.text)
        self.spam = self.soup.find_all
        
        ################################################################################
        
    def get_lede_data(self):
    
        link_list = []
        for tag in self.spam('li', attrs={'class':'ledeArticle'}):
    		    
            link = tag.find('a')['href']
            link_list.append(link)
            
        self.data['lede'] = link_list  
        
        ################################################################################
        
    def get_article_data(self):
    	
    	link_list = []
        for tag in self.spam('article', attrs={'class':'feedEntry'}):
    		    
            link = tag.find('a')['href']
            link_list.append(link)
            
        self.data['article'] = link_list  
    
        ################################################################################
        
    def return_data(self):
    	
	return self.data
    	
    	################################################################################

if __name__ == '__main__':
	
    baseurl = raw_input('Enter a URL (ex. http://ec2.qa.nymetro.com/thecut/beauty/):')	
    b = Splash(baseurl)
    b.get_lede_data()
    b.get_article_data()
    print b.return_data()
    
