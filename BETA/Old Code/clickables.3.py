#! /usr/bin/python

import unittest
import time, datetime
import re
import pickle
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox')
TEST = "Clickables Module - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.clickables()			# Call the relevant BeautifulSoup function (usually same name as test)

CSS = open('../data/text/clickables.css.txt', 'r').readlines()		# CSS Selectors for elements
DATA = pickle.load(open('../data/pickle/clickables.data.p', 'rb')) 	# Dictionary with data
      
keys = DATA.keys()
values = DATA.values()
      
print DATA      
      
x = 0

"""
This is a test for Vulture's Clickables module on the home page for desktop (non-mobile).
The DATA file is a pickle file generated by vultureSoup.Parser(), customized for this module.
IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT, .P and .JSON FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!

"""	

#########################################################################
#########################################################################
	

class Clickables(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
	
	########################################################################
    
    def test_a(self):

    	"""
        Preliminary test for the presence of various elements in the clickables module.
        CSS selectors are in a .txt file, and this test makes sure each element exists on the page before proceeding.
        Failures will fail the whole test.  (No point in continuing if links aren't present, right?).
        The other tests are called from this function to avoid repetitive and unnecessary SetUp and TearDown of the browser.
        In addition, the other tests can be commented out and not run - easy to select which tests run.  None are dependent on 
        results from other tests.  Only test_splash_feed needs to be run for the sub-tests to run.
        
        PASSING CONDITIONS:  All elements are present on the page.
        FAILING CONDITIONS:  Any ONE element is not present on the page.
        
        """
	
	n = 0
	sel = self.selenium
        sel.open(BASEURL)
        sel.wait_for_page_to_load("50000")
        test = "Test A - Presence of Elements via CSS"
        print test
        
	for each in CSS:

	    c = CSS[n].strip('\n') 
        
            try:
                self.failUnless(sel.is_element_present("css=" + c))
                
            except AssertionError, e:
            	print "FAILURE, ELEMENT NOT FOUND" + c, "Error: " + str(e)
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], test, "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            
            else:
                L.log(BROWSERS[x], test, "PASS, ELEMENT FOUND", c)
                
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
        4. 
        """
        
	for each in keys:
	# Links is a list containing data for each entry in the clickables module
        	
            article = values[n]	# Re-name variable
            
            m = 0
            a_list = []                 # Re-name, list isn't a good choice, either
            permalinks = []
            
            for each in article:
            # Contains data for the clickables entries
            	    
                datapoint = article[m]
                url = datapoint[0]
                data = datapoint[1]
                
                if len(article) > 1:
               
                    link1 = article[0]
                    link2 = article[1]
                	
                    a_list.append(link1)
                    permalinks.append(link2)
        
                try:
            	    if len(article) > 1:    
            	        text = sel.get_text("//a[@href='" + url + "']")
            	
                except AssertionError, e:
            	    L.log(BROWSERS[x], TEST, "FAIL, Cannot get link Text", url)
                    print "FAILURE, can't get link text " + url
                    self.verificationErrors.append(str(e))
                
            # Second, get the title and search the title for the link text
            	
                try:
            	    sel.open(url)
            	    sel.wait_for_page_to_load("50000")
            	    if len(article) > 1:
                        title = sel.get_title()
                
                except AssertionError, e:
            	    L.log(BROWSERS[x], TEST, "FAIL, Cannot open page and get title", url)
                    print "FAILURE, can't open page and get title " + url
                    self.verificationErrors.append(str(e))
                
                else:
            	    L.log(BROWSERS[x], TEST, "PASS, page opens and title has been acquired", url)
            	
            	    if len(article) > 1:
                        if re.search(text, title, re.I):
                            L.log(BROWSERS[x], TEST, "PASS, Correct page loads", url)
                        
                        elif re.search("not found", title, re.I):
                            L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", url)
                    	
                        else:
                    	    print "Test has a bug / exception", url, title, text
               
                    
                    sel.go_back()
                    sel.wait_for_page_to_load("50000")
            
                    m += 1
            
                n += 1
                   
            if len(a_list) != len(permalinks):
            	L.log(BROWSERS[x], TEST, "FAIL, MISMATCHED LINKS", url)
            else:
                L.log(BROWSERS[x], TEST, "PASS, Clickables article has permalink and regular link", url)
                if (len(a_list) > 23 or len(a_list) < 7):
                    L.log(BROWSERS[x], TEST, "FAIL, TOO MANY/TOO FEW ARTICLES IN CLICKABLES", str(len(a_list)) + " articles")
        

    ########################################################################    	    
            
    def c_clicky_test(self):
    	    
    # Tests for the module's functionality
    # Clicks on each link based on its address (href attribute)
    # Makes sure the page loads
    	
    	n = 0 
        sel = self.selenium
        sel.open("/")
        sel.wait_for_page_to_load("50000")
        
        # First, make sure each link can be clicked on and that the page loads
        
        for n in range(0,8):
        	
            article = articles[n]
            datapoint = article[m]
            d = datapoint[0]
            c = datapoint[1]
            print d
            print c
        	
            try:
                sel.click("//a[@href='" + d + "']")
                sel.wait_for_page_to_load("50000")
                
	    except Exception, e:
		print "FAILURE " + d, " does not load"
		L.log(BROWSERS[x], TEST, "FAIL, PAGE DOES NOT LOAD", str(e) + d)
		
	    else:
	    	L.log(BROWSERS[x], TEST, "PASS, Page loads", d)
		sel.go_back()
	        sel.wait_for_page_to_load("50000")
	    
            n += 1
            
        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(Clickables)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()