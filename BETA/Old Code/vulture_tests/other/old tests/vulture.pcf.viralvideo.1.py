#! /usr/bin/python

import unittest
import time, datetime
import re
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "Viral Video Module on Vulture Home Page"

text_list = []                  # Contains all link text after test 'b' gets link text from data in CONTENT

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.viralvideo()			# Call the relevant BeautifulSoup function (usually same name as test)

CSS = open('../data/vulture.home.viralvideo.css.txt', 'r').readlines()		# a = presence; Is it there?
CONTENT = open('../data/vulture.home.viralvideo.content.txt', 'r').readlines()      # b = content; Does the module have the right stuff?
DATA = open('../data/vulture.home.viralvideo.data.txt', 'r').readlines()  	        # c = function; Does the module work?
      
x = 0

"""This is a regression test for the Viral Video module on Vulture's home page"""
""" Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements (via XPATH locators in the CONTENT file) contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  The DATA file contains this data"""
"""IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!"""	

#########################################################################
#########################################################################	

class ViralVideos(unittest.TestCase):
    
    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
	
	########################################################################
    
    def test_a(self):

    # Tests for the presence of elements in the module using CSS locators
    # This test is an 'assert' test: if any element is not present, the test fails
	
	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        # Loops through the data in the CSS file asserting each element is on the page
        
	for each in CSS:

	    c = CSS[n].strip('\n') 
        
            try:
                self.failUnless(sel.is_element_present("css=" + c))
                
            except AssertionError, e:
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], TEST, "FAIL, ELEMENT NOT FOUND", str(e) + c)
            
            else:
                L.log(BROWSERS[x], TEST, "PASS, ELEMENT FOUND", c)
                
            n += 1
            
        ########################################################################
        
    def test_content(self):
    	    
    	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("5000")
        n = 0
        
        link = DATA[7].strip('\n')
        link_count = sel.get_css_count('css=' + link)	# Links
        vid = DATA[6].strip('\n')
        vid_count = sel.get_css_count('css=' + vid)	# Video
        art = DATA[5].strip('\n')
        art_count = sel.get_css_count('css=' + art)	# Article Text
        
        if (link_count < 3) or (link_count > 6):
	    self.verificationErrors.append("Incorrect number of links, " + str(link_count) + " links found.")
	    L.log(BROWSERS[x], TEST, "FAIL", "Incorrect number of links in Viral Videos: " + str(link_count) + " links")
	    print link_count, "COUNT"
	else:
	    L.log(BROWSERS[x], TEST, "PASS", "Correct number of links in Viral Videos: " + str(link_count) + " links")
        
        if (vid_count < 3) or (vid_count > 6):
	    self.verificationErrors.append("Incorrect number of videos, " + str(vid_count) + " videos found.")
	    L.log(BROWSERS[x], TEST, "FAIL", "Incorrect number of videos in Viral Videos: " + str(vid_count) + " videos")
	else:
	    L.log(BROWSERS[x], TEST, "PASS", "Correct number of videos in Viral Videos: " + str(vid_count) + " videos")
	    
	if (art_count < 3) or (art_count > 6):
	    self.verificationErrors.append("Incorrect number of articles, " + str(art_count) + " articles found.")
	    L.log(BROWSERS[x], TEST, "FAIL", "Incorrect number of articles in Viral Videos: " + str(art_count) + " articles")
	else:
	    L.log(BROWSERS[x], TEST, "PASS", "Correct number of articles in Viral Videos: " + str(art_count) + " articles")
	    
	if not (vid_count == art_count) and (vid_count == link_count) and (art_count == link_count):
	    L.log(BROWSERS[x], TEST, "FAIL", "Number of articles and videos mismatched in Viral Videos: " + str(link_count) + " links, " + str(vid_count) + " videos, and " + str(art_count) + " articles.")
	else:
	    L.log(BROWSERS[x], TEST, "PASS", "Correct number of videos and articles in Viral Videos: " + str(link_count) + " links, " + str(vid_count) + " videos, and " + str(art_count) + " articles.")
	    
    def test_functionality(self):
    	    
    	pass
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(ViralVideos)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
