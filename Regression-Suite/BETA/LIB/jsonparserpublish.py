#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re
import string
import urllib
import urllib2
import time
import pickle
import socket
#from bs4 import BeautifulSoup


reload(sys)
sys.setdefaultencoding("utf-8")


class MyOpener(urllib.FancyURLopener):
	
    # Used with the old login version, ignore for now
    
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'
    
    #########################################################################
    #########################################################################
    

class JSONParserPublish():
	
    def __init__(self, query):
        
        timeout = 10
        socket.setdefaulttimeout(timeout)
        
        # Set up authorization in header and open page
        # request.add_header()'s second arg is the usr/pwd in base64
        
        request = urllib2.Request(query)
        request.add_header("Authorization", "Basic bnNtaXRoOkd1YW53dWs1")   
        self.result = urllib2.urlopen(request)
        
    #########################################################################
    
    def login(self):
    	
    	# Open a file and write the JSON data (result) to the file
    	
        d = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/s.txt', 'w')
        d.write(self.result.read())
        d.close()
        
    #########################################################################
    #########################################################################
    
if __name__ == '__main__':

    query = pickle.load(open('/Users/nsmith/Desktop/BETA/CUT/DATA/PICKLE/query.p', 'rb'))
    J = JSONParser(query)
    J.login()
