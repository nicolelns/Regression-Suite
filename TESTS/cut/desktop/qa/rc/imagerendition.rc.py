#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import time, datetime
import re
import pickle
import Logger			# Logging module (for test results, outputs results to a .txt file)
import cutSoup     		# BeautifulSoup page scraper collects relevant data from qa.nymetro
from selenium import selenium 

reload(sys)
sys.setdefaultencoding("utf-8")	# Sets encoding

BASEURL = 'http://ec2.qa.nymetro.com/thecut/celebrity/'
BROWSERS = 'chrome'	
TEST = "Image Rendition Service - Tools - Author"

L = Logger.MainLogger(BASEURL, TEST)

S = cutSoup.Parser(BASEURL)
S.image_rendition_tool()

DATA = pickle.load(open('../data/pickle/imagerendition.data.p', 'rb'))

keys = DATA.keys()
values = DATA.values()

x = 0

"""
Image rendition service test

"""	

#########################################################################
#########################################################################
	

class ImageRendition(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL)
        self.selenium.start()
        print "TESTING THE IMAGE RENDITION SERVICE"

        ########################################################################
        
    def test_imagerendition(self):
    	   
        sel = self.selenium
        sel.open(BASEURL)
        test = "Test A - Image Rendition Present"
        print test
        m = 0
        
        #Verify image
        
        for each in keys:
        	
            alt = values[m]
            image = keys[m]
            
            try:
                sel.is_element_present("//img[@src='" + image + "']")
                    
            except Exception, e:
                L.log(BROWSER, test, "FAIL, IMG NOT PRESENT", image, exception=str(e))
                self.verificationErrors.append(image + " is not on page")
                
            else:
	        dimensions = self.b_size(image)
	        dimensions_dict[image] = dimensions
	     
	    m += 1   
            
    	########################################################################

    def b_size(self):
    	    
    	sel = self.selenium
    	test = "Test B - Correct Image Sizes"
    	print test
    	
    	self.image = image
    	
    	try:
    	    height = sel.get_element_height("//img[@src='" + self.image + "']")
	    width = sel.get_element_width("//img[@src='" + self.image + "']")
	    
        except Exception, e:
            L.log(BROWSER, test, "FAIL, CANNOT GET HEIGHT/WIDTH", self.height + ": height " + self.width + ": width", exception=str(e))
            self.verificationErrors.append(self.image " cannot get height/width")
            print self.image, str(e)
            
        else:
            L.log(BROWSER, test, "PASS, GOT HEIGHT/WIDTH", self.height + ": height " + self.width + ": width")
            
        return (height, width)


        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

suite = unittest.TestLoader().loadTestsFromTestCase(CelebritySplash)
unittest.TextTestRunner(verbosity=2).run(suite)
   
L.save()