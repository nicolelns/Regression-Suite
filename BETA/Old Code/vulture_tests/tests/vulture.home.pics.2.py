#! /usr/bin/python

import unittest
import time, datetime
import re
import pickle
import Logger2 as Logger	# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "Pics Module - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.pics()

CSS = open('../data/vulture.home.pics.css.txt', 'r').readlines()
DATA = pickle.load(open('../data/vulture.home.pics.data.p', 'rb'))

articles = DATA.keys()
links = DATA.values()

x = 0

"""
This is a regression test for the Pics module on Vulture's home page:

Test 'a' is a 'presence' test:  Do the elements (via CSS selectors in the CSS file) appear on the page and in the correct spot?
Test 'b' is a 'content' test:  Do the elements contain the relevant data?  
Test 'c' is a 'functional' test:  Does the module work?  Do links work?  Do the right pages load?  

The DATA file is a pickle file generated by vultureSoup.Parser(), customized for this module.

IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!
"""	

#########################################################################
#########################################################################
	

class Pics(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
	
	########################################################################
    
    def test_a(self):
 
        """ 
        Tests for the presence of elements in the module using CSS locators.  The CSS file contains the locators.
        This test is an 'assert' test: if any element is not present, the test fails
        """
	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
	for each in CSS:

	    c = CSS[n].strip('\n') 
        
            try:
                self.failUnless(sel.is_element_present("css=" + c))
                
            except AssertionError, e:
            	print "FAILURE"
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], "Test A - Presence", "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            
            else:
                L.log(BROWSERS[x], "Test A - Presence", "PASS, ELEMENT FOUND", c)
                
            n += 1
            
        ########################################################################
	    
    def test_b(self):
    	    
        """
        Tests for the correct content within the module using data from the pickled data file, DATA
        This is a 'verify' test, it will not fail the whole test if one item fails
        """
    	
    	n = 0
	sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        """
        1. Gets the link text for each link
        2. Opens each page directly in the browser (as opposed to clicking on a link)
        3. Gets the page's title and checks that the link text is in the title (correct page loads)
        4. Verify that there are 2 urls for each article - one permalink and another with an associated image
        5. Verify that there are 5 picture articles in the pics module
        """
        
	for each in links:
	# Links is a list containing data for each <article> tag in the pics module
        	
            article = links[n]	
            
            m = 0
            llist = []                    # Rename llist
            
            for each in article:
            # Article contains the actual urls and images within each <article> tag in the pics module
            	    
            	datapoint = article[m]
                url = datapoint[0]
                data = datapoint[1]
                
                if data == None or data == "*":
        
                    try:
            	        text = sel.get_text('//a[@href="' + url + '"]')
            	
                    except AssertionError, e:
            	        L.log(BROWSERS[x], "Test B - Content", "FAIL, CANNOT GET LINK TEXT", url, exception=str(e))
                        print "FAILURE"
                        
                    else:
                    	L.log(BROWSERS[x], "Test B - Content", "PASS, GOT LINK TEXT", url)
           	
                    try:
            	        sel.open(url)
            	        sel.wait_for_page_to_load("50000")
                        title = sel.get_title()
                
                    except AssertionError, e:
            	        L.log(BROWSERS[x], "Test B - Content", "FAIL, CANNOT OPEN PAGE/GET TITLE", url, exception=str(e))
                        print "FAILURE"
                
                    else:
            	        L.log(BROWSERS[x], "Test B - Content", "PASS, PAGE OPENS/GOT TITLE", url)
            	
                    if re.search(text, title, re.I):
                        L.log(BROWSERS[x], "Test B - Content", "PASS, TEXT/TITLE MATCH", url)
                        
                    elif re.search("not found", title, re.I):
                        L.log(BROWSERS[x], "Test B - Content", "FAIL, 404/PAGE NOT FOUND", url)
                    	
                    else:
                        L.log(BROWSERS[x], "Test B - Content", "INCONCLUSIVE", url + " " + title)
                    
                    sel.go_back()
                    sel.wait_for_page_to_load("50000")
                    
                if data == "See All" or data == "Pics":
                	
                    try:
                    	sel.open(url)
                        sel.wait_for_page_to_load("50000")
                        title = sel.get_title()
                        self.assertEqual("Slideshow News - Vulture", title)
                        
                    except AssertionError, e:
          	        L.log(BROWSERS[x], "Test B - Content", "FAIL, CANNOT OPEN PAGE/GET TITLE", url, exception=str(e))
                        print "FAILURE"
                        
                    else:
            	        L.log(BROWSERS[x], "Test B - Content", "PASS, PAGE OPENS/GOT TITLE", url)
            	       
            	if data != None:
                    if re.search("300x235", data, re.I):
                        llist.append(url)
                    
                    elif data == "*":
                        if url in llist:
                            L.log(BROWSERS[x], "Test B - Content", "PASS, LINKS MATCH", url + " URL " + llist[0] + " LIST")
                    
                        else:
                    	    L.log(BROWSERS[x], "Test B - Content", "FAIL, LINKS DON'T MATCH", url + " URL " + llist[0] + " LIST")
                    
                m += 1
            
            n += 1
            
            if (len(articles) - 1) != 5:        # articles contains one extra element which is not a picture
                L.log(BROWSERS[x], "Test B - Content", "FAIL, MISSING/EXTRA PICS", str(len(articles)) + " articles found")
                
            else:
                L.log(BROWSERS[x], "Test B - Content", "PASS, CORRECT NUMBER OF PICS", str(len(articles)) + " articles found") 
            
        ########################################################################    	    
            
    def test_c(self):
    	    
        """
        Tests for the module's functionality
        1. Clicks on each link based on its address (href attribute)
        2. Clicks on each image based on its address (src attribute)
        3. Makes sure each page loads
        4. Tests that the arrow buttons work and display the proper pictures
        """
    
    	
    	n = 0 
        sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        img_list = []
        
            # First, make sure each link can be clicked on and that the page loads
        
        for each in links:
        	
            article = links[n]	
            
            m = 0
            
            for each in article:
            	    
            	datapoint = article[m]
                url = datapoint[0]
                data = datapoint[1]
        	
                try:
                    sel.click('//a[@href="' + url + '"]')
                    sel.wait_for_page_to_load("50000")
                
	        except Exception, e:
		    L.log(BROWSERS[x], "Test C - Functionality", "FAIL, PAGE DOES NOT LOAD", url, exception=str(e))
		
	        else:
	    	    L.log(BROWSERS[x], "Test C - Functionality", "PASS, PAGE LOADS", url)
		    sel.go_back()
	            sel.wait_for_page_to_load("50000")
	                   
	        if (data is not None) and (data != "*") and (data != "See All") and (data != "Pics"):
	        
	    	    img_list.append(data)	
	    	
	    	    try:
                        sel.click("//img[@src='" + data + "']")
                        sel.wait_for_page_to_load("50000")
                
	            except Exception, e:
		        print "FAILURE " + data, " image does not load"
		        L.log(BROWSERS[x], "Test C - Functionality", "FAIL, IMAGE DOES NOT LOAD", data, exception=str(e))
		 
                    else:
	    	        L.log(BROWSERS[x], "Test C - Functionality", "PASS, IMAGE LOADS", data)
		        sel.go_back()
	                sel.wait_for_page_to_load("50000")
	    
	        m += 1
	    
            n += 1
            
            # Check that the arrow buttons work and display the correct image
            
        sel.refresh()
        sel.wait_for_page_to_load("50000")
        
        nums_right_arrow = (1,2,3,4,0,1)
        nums_left_arrow = (0,4,3,2,1,0)
       
        for z in range(0,6): 
            num1 = nums_right_arrow[z]
            sel.click("css=" + CSS[3])
            
            try:
            	sel.is_visible("//img[@src='" + img_list[num1] + "']")
            
            except:
            	L.log(BROWSERS[x], "Test C - Functionality", "FAIL, INCORRECT IMAGE DISPLAYS AFTER CLICKING ARROW", img_list[num1], exception=str(e))
            
            else:
                L.log(BROWSERS[x], "Test C - Functionality", "PASS, CORRECT IMAGE DISPLAYS AFTER CLICKING ARROW", img_list[num1])
            
            z += 1
                
        for z in range(0,6):
            num2 = nums_left_arrow[z]
            sel.click("css=" + CSS[2])
	    
            try:
            	sel.is_visible("//img[@src='" + img_list[num1] + "']")
            	
            except:
            	L.log(BROWSERS[x], "Test C - Functionality", "FAIL, IMAGE DOES NOT LOAD", img_list[num2], exception=str(e))
            
            else:
                L.log(BROWSERS[x], "Test C - Functionality", "PASS, CORRECT IMAGE DISPLAYS AFTER CLICKING ARROW", img_list[num2])
            	    
            z += 1

        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(Pics)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()