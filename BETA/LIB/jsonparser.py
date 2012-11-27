#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import urllib
import urllib2
import socket


reload(sys)
sys.setdefaultencoding("utf-8")


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
    
    def get_data(self):
    	
    	# Return the page result
    	
        return self.result.read()
        
    #########################################################################
    #########################################################################
    
if __name__ == '__main__':

    query = raw_input("Enter a URL to query:")
    J = JSONParser(query)
    J.get_data()
