#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re
import json
import pickle
import subprocess
import string
import time

SLUG = 'http://author.nymetro.com/services/fashion/get.fashion.show.data.json:'
SEASONLIST = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/seasonmigrationlist.txt', 'r').readlines()
#SEASON = str(sys.argv[1])
#print SEASON, " is being tested"

class SeasonUtils():
	
    def __init__(self):
    	   
        self.f = open('../DATA/TEXT/runwayshowlist.txt', 'w')
        self.g = open('../DATA/TEXT/liveshowurls.txt', 'w')
        
        pickle.dump(SEASON, open('/Users/nsmith/Desktop/BETA/CUT/DATA/PICKLE/query.p', 'wb'))
        
        p = subprocess.Popen('/Users/nsmith/Desktop/BETA/LIB/jsonparserpublish.py', shell=True)
        p.wait()
        
        load = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/s.txt', 'r').read()
        
        pickle.dump(load, open('/Users/nsmith/Desktop/BETA/CUT/DATA/PICKLE/seasondict.p', 'wb'))
        
        self.data = json.loads(load).values()
        
        for show in self.data[0]:
	    self.make_show_query(show)
	    
	self.f.close()  
	self.g.close()
                                                  
    def make_show_query(self, show):
    
    	#re_str = re.compile('.*')
        #fashion-lists:seasons/fall
        #fashion-lists:collection-type/rtw
        #years:2012
        #fashion-lists:cities/ + re_str
        #fashion-lists:labels/ + re_str
       
        for key in show:
    	    	
            if "fashion-lists:seasons/" in key:
            	season = self.show_url_string(key)
            	    
            elif "fashion-lists:collection-type/" in key:
            	show_type = self.show_url_string(key)
            	    
            elif "fashion-lists:labels/" in key:
            	label = self.show_url_string(key)
            	    
            elif "fashion-lists:cities/" in key:
            	city = self.show_url_string(key)
            	        
            elif "years:" in key:   
            	year = self.show_url_string(key)
            	 
        path_list = [year[6:], season, city, show_type, label]
        self.f.write(SLUG + self.show_pathmaker(path_list) + '\n')
        self.g.write('http://nymag.com/thecut/fashion/shows/' + self.show_urlmaker(path_list) + '.html' + '\n')
        
    def show_url_string(self, string):
    	    
    	self.s = string
    	new_str = str(self.s).split('/')
        return new_str[-1]
    
    def show_urlmaker(self, ls):
    	    
    	for each in ls:
            url = "/".join(ls)
        return url
        
    def show_pathmaker(self, ls):
    	  
    	for each in ls:
    	    url = ".".join(ls)
        return url
        
    def run_season_tests(self):
    	 
    	ff = open('/Users/nsmith/Desktop/RUNWAYMIGRATION/showdate_results.txt', 'a')
        ff.write(SEASON)
        ff.write('\n')
        ff.close() 
    	 
    	proc = subprocess.Popen('/Users/nsmith/Desktop/BETA/CUT/BACKEND/seasonmigration.py', shell=True)
        proc.wait()
        
        
class ShowUtils():
	
    def __init__(self, show, url):
    	    
    	self.show = show    
    	self.url = url
    
    	pickle.dump(self.show, open('/Users/nsmith/Desktop/BETA/CUT/DATA/PICKLE/query.p', 'wb'))

        p = subprocess.Popen('/Users/nsmith/Desktop/BETA/LIB/jsonparserpublish.py', shell=True)
        p.wait()
        
        load = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/s.txt', 'r').read()
        self.data = json.loads(load)

        pickle.dump(self.data, open('../DATA/PICKLE/showdict.p', 'wb'))
        pickle.dump(self.url, open('../DATA/PICKLE/url.p', 'wb'))
        
    def run_show_tests(self):
    	    
    	proc = subprocess.Popen('/Users/nsmith/Desktop/BETA/CUT/BACKEND/showmigration.py', shell=True)
    	proc.wait()

"""
r = SeasonUtils()
f = open('../DATA/TEXT/runwayshowlist.txt', 'r').readlines()
g = open('../DATA/TEXT/liveshowurls.txt', 'r').readlines()
r.run_season_tests()
x = 0

for show in f:
    print x
    url = g[x]
    strip_show = show.strip('\n')
    s = ShowUtils(strip_show, url)
    s.run_show_tests()
    x += 1

"""
    ###############################

def format_results():
	
    #uncomment to debug
	
    f = open('/Users/nsmith/Desktop/RUNWAYMIGRATION/dupedunpublishedshows.txt', 'r').readlines()
    g = open('/Users/nsmith/Desktop/RUNWAYMIGRATION/unpublishedshows.txt', 'w')
    r = 0
    results = {}
    for line in f:
    
   	if r % 2 == 0:
   	    line1 = line.strip('\n')
   	    #print line1, "LINE1" 
        else:
            line2 = line.strip('\n')
            #print line2, "LINE2"
            concatenate = line1 + line2
            #print concatenate, "CONCAT"
            results[concatenate] = r

        r += 1

    rk = results.keys()

    for item in rk:
        g.write(item)
        g.write('\n')
    g.close()
    
    ###############################

for season in SEASONLIST:
    SEASON = season.strip('\n')
    print SEASON, " is being tested"
    r = SeasonUtils()
    f = open('../DATA/TEXT/runwayshowlist.txt', 'r').readlines()
    g = open('../DATA/TEXT/liveshowurls.txt', 'r').readlines()
    r.run_season_tests()
    x = 0
    
    for show in f:
        print x
        url = g[x]
        strip_show = show.strip('\n')
        s = ShowUtils(strip_show, url)
        s.run_show_tests()
        x += 1
    
format_results()

