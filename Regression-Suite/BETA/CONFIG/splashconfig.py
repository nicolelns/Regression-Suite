#! /usr/bin/python                                                                                                                                                                                  
# -*- coding: utf-8 -*-

import sys
import os
import re
import string

class BeautyConfig():

    def __init__(self):
        pass
        
    def tests(self):
        test_list = ['test_entries',
                     'test_lede',
                     'test_bizdev']
        return test_list
        
    def staging(self):
    	
        return {'author':"http://author.stg.nymetro.com/",
        	'url':"http://stg.nymetro.com/thecut/beauty/",
        	'env':'stg',
        	'usr':'admin',
                'pwd':'admin'}
        
    def qa(self):
    	
    	return {'author':"http://author.ec2.qa.nymetro.com/",
        	'url':"http://ec2.qa.nymetro.com/thecut/beauty/",
        	'env':'ec2',
        	'usr':'admin',
                'pwd':'admin'}
        
    def production(self):
    	
    	return {'author':"http://author.nymetro.com/",
        	'url':"http://nymag.com/thecut/beauty/",
        	'env':'prod',
        	'usr':'nsmith',
                'pwd':'Guanwuk5'}
    
    # This function does the work - toggle an environment on or off here.
    # You do not need to edit the environment functions.
    # To toggle tests, comment out tests in the tests() function.
    # To change the log output path, modify the 'path' lookup value.
    
    def configuration(self):
    	
    	return {'tests':self.tests(),
    	       'path':'/Users/nsmith/Desktop/beautyfail.txt',
    	       'env':{ 
    	       #'stg':self.staging(),
    	       #'qa':self.qa(),
    	       'prod':self.production()}}
    	       
    	       
class FameConfig():

    def __init__(self):
        pass
        
    def tests(self):
        test_list = ['test_entries',
                     'test_lede',
                     'test_bizdev']
        return test_list
        
    def staging(self):
    	
        return {'author':"http://author.stg.nymetro.com/",
        	'url':"http://stg.nymetro.com/thecut/celebrities/",
        	'env':'stg',
        	'usr':'admin',
                'pwd':'admin'}
        
    def qa(self):
    	
    	return {'author':"http://author.ec2.qa.nymetro.com/",
        	'url':"http://ec2.qa.nymetro.com/thecut/celebrities/",
        	'env':'ec2',
        	'usr':'admin',
                'pwd':'admin'}
        
    def production(self):
    	
    	return {'author':"http://author.nymetro.com/",
        	'url':"http://nymag.com/thecut/celebrities/",
        	'env':'prod',
        	'usr':'nsmith',
                'pwd':'Guanwuk5'}
    
    # This function does the work - toggle an environment on or off here.
    # You do not need to edit the environment functions.
    # To toggle tests, comment out tests in the tests() function.
    # To change the log output path, modify the 'path' lookup value.
    
    def configuration(self):
    	
    	return {'tests':self.tests(),
    	       'path':'/Users/nsmith/Desktop/famefail.txt',
    	       'env':{ 
    	       #'stg':self.staging(),
    	       #'qa':self.qa(),
    	       'prod':self.production()}}
    	       
    	       
class GoodsConfig():

    def __init__(self):
        pass
        
    def tests(self):
        test_list = ['test_entries',
                     'test_lede',
                     'test_bizdev']
        return test_list
        
    def staging(self):
    	
        return {'author':"http://author.stg.nymetro.com/",
        	'url':"http://stg.nymetro.com/thecut/goods/",
        	'env':'stg',
        	'usr':'admin',
                'pwd':'admin'}
        
    def qa(self):
    	
    	return {'author':"http://author.ec2.qa.nymetro.com/",
        	'url':"http://ec2.qa.nymetro.com/thecut/goods/",
        	'env':'ec2',
        	'usr':'admin',
                'pwd':'admin'}
        
    def production(self):
    	
    	return {'author':"http://author.nymetro.com/",
        	'url':"http://nymag.com/thecut/goods/",
        	'env':'prod',
        	'usr':'nsmith',
                'pwd':'Guanwuk5'}
    
    # This function does the work - toggle an environment on or off here.
    # You do not need to edit the environment functions.
    # To toggle tests, comment out tests in the tests() function.
    # To change the log output path, modify the 'path' lookup value.
    
    def configuration(self):
    	
    	return {'tests':self.tests(),
    	       'path':'/Users/nsmith/Desktop/goodsfail.txt',
    	       'env':{ 
    	       #'stg':self.staging(),
    	       #'qa':self.qa(),
    	       'prod':self.production()}}
    	       
    	       
class LoveConfig():

    def __init__(self):
        pass
        
    def tests(self):
        test_list = ['test_entries',
                     'test_lede',
                     'test_bizdev']
        return test_list
        
    def staging(self):
    	
        return {'author':"http://author.stg.nymetro.com/",
        	'url':"http://stg.nymetro.com/thecut/love/",
        	'env':'stg',
        	'usr':'admin',
                'pwd':'admin'}
        
    def qa(self):
    	
    	return {'author':"http://author.ec2.qa.nymetro.com/",
        	'url':"http://ec2.qa.nymetro.com/thecut/love/",
        	'env':'ec2',
        	'usr':'admin',
                'pwd':'admin'}
        
    def production(self):
    	
    	return {'author':"http://author.nymetro.com/",
        	'url':"http://nymag.com/thecut/love/",
        	'env':'prod',
        	'usr':'nsmith',
                'pwd':'Guanwuk5'}
    
    # This function does the work - toggle an environment on or off here.
    # You do not need to edit the environment functions.
    # To toggle tests, comment out tests in the tests() function.
    # To change the log output path, modify the 'path' lookup value.
    
    def configuration(self):
    	
    	return {'tests':self.tests(),
    	       'path':'/Users/nsmith/Desktop/lovefail.txt',
    	       'env':{ 
    	       #'stg':self.staging(),
    	       #'qa':self.qa(),
    	       'prod':self.production()}}
    	       
    	       
    	       
  
if __name__ == '__main__':
    B = BeautyConfig()
    B.configuration()

