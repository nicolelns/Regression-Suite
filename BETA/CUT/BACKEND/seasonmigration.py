#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re
import pickle
import string
import unittest
import json
import time
#import HTMLTestRunner

reload(sys)
sys.setdefaultencoding("utf-8")


DATA = json.loads(pickle.load(open('/Users/nsmith/Desktop/BETA/CUT/DATA/PICKLE/seasondict.p', 'rb')))


class SeasonMigration(unittest.TestCase):
	
    def setUp(self):
    	
    	self.f = open('/Users/nsmith/Desktop/RUNWAYMIGRATION/showdate_results.txt', 'a')
    	
    	self.season = DATA.values()[0] # List of shows
    	self.show = self.season[0]
    	self.date_data = []
    	self.verificationErrors = []
        
    #def test_process(self):
    	    
    	#self.assertEqual(len(self.show_list), len(self.v[0]))
    
    def test_test(self):
    	    
    	for show in self.season:
            
            self.show_assets(show)
            self.show_date(show)    
    
    def show_assets(self, show):
    	
    	self.show = show
    	try:
    	    asset = self.show['assetCount']
    	    self.assertNotEqual(asset, None)
    	    self.assertNotEqual(asset, '')
    	    self.assertNotEqual(asset, 0)
    	        
    	except KeyError:
    	    self.f.write(self.show['showName']) 
    	    self.f.write(" has no assetCount key in JSON")
    	    self.f.write('\n')	
    		
    	except AssertionError:
    	    self.f.write(self.show['showName'])
    	    self.f.write(" has 0 assets")
    	    self.f.write('\n')
    	    
    def show_date(self, show):
    	   
    	self.show = show
    	try:
    	    date = self.show['creationDate']
    	    self.assertTrue(date not in self.date_data)
    	    self.date_data.append(date)
    	        
    	except KeyError:
    	    self.f.write(self.show['showName'])
    	    self.f.write(" has no assetCount key in JSON data")
    	    self.f.write('\n')	
    		
    	except AssertionError:
    	    self.f.write(self.show['showName'])
    	    self.f.write(" has same creation date as another show!")
    	    self.f.write('\n')
    	
    def tearDown(self):
    	
    	self.assertEqual(self.verificationErrors, [])
    	self.f.close()
    	
#results = open('/Users/nsmith/desktop/SEASONrunwaymig.html', 'wb')
suite = unittest.TestLoader().loadTestsFromTestCase(SeasonMigration)
unittest.TextTestRunner(verbosity=2).run(suite)
#runner = HTMLTestRunner.HTMLTestRunner(stream=results, title="TESTING", description='Results for Season Runwaymig')
#runner.run(suite)
    
    
