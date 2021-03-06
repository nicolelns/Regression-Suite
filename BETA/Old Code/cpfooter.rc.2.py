#! /usr/bin/python
# -*- coding: latin-1 -*-

import unittest
import time, datetime
import re
import pickle
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox', 'safari')
TEST = "Copyright Footer Section Test (General Promo) - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.cpfooter()

CSS = open('../data/text/cpfooter.css.txt', 'r').readlines()			# CSS selectors	for elements
DATA = pickle.load(open ('../data/pickle/cpfooter.data.p', 'rb')) 		# List of links
CONTENT = "2010 2011, New York Media LLC. All Rights Reserved."			# Text that should be on page

x = 0


"""
This is a test for Vulture's Copyright and corporate links section of the footer.
The DATA file is a pickle file generated by vultureSoup.Parser(), customized for this module.
IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT, .P and .JSON FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!

"""	

#########################################################################
#########################################################################
	

class CpFooter(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
	
	########################################################################
    
    def test_cp_footer(self):

    	"""
        Preliminary test for the presence of various elements in the bottom section of the footer (with the copyright statement).
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
            
        self.b_title_test()    
        self.c_link_count()
        
        ########################################################################
	    
    def b_title_test(self):
    	    
    	"""
    	This test grabs the link text (text between <a></a> tags) for each link.  
    	Each page is clicked on to ensure that the link works.
    	The title of the opened page is acquired.
    	The title text is compared to the link text to make sure the right page opens.
    	NOTE:  There may be some exceptions to this string matching test - not all links
    	will pass this part.  Most of the articles use the link text as the page's title.  As long
    	as the pages load, this test is considered valid in that respect.
    	
    	PASSING CONDITIONS:  Each link has text associated with it
    			     Each link can be clicked on
    			     Each page loads and has a title
    			     **The page title matches the link text
    			     
    	FAILING CONDITIONS:  Links have no text for the user to see/click on
    			     Links cannot be clicked on
    			     Pages do not load or have "not found" in the title
    			     **The page title does not match the link text
    			     
    	** More important for articles, this specific test will have 2 exceptions.
    	
    	"""
    	
        n = 0
	sel = self.selenium
	test = "Test B - Do the Links Open the Right Pages?"
	print test
        
	for each in DATA:

	    d = DATA[n] 
        
            try:
            	text = sel.get_text("//a[@href='" + d + "']")
            	
            except AssertionError, e:
            	L.log(BROWSERS[x], test, "FAIL, CANNOT GET LINK TEXT", d, exception=str(e))
                print "FAILURE, CAN'T GET LINK TEXT " + d, "Error: " + str(e)
                self.verificationErrors.append(str(e))
                
            # Second, get the title and search the title for the link text
            	
            try:
            	sel.click("//a[@href='" + d + "']")
            	sel.wait_for_page_to_load("50000")
                title = sel.get_title()
                
            except AssertionError, e:
            	L.log(BROWSERS[x], test, "FAIL, CANNOT OPEN PAGE AND GET TITLE", d, exception=str(e))
                print "FAILURE, CAN'T OPEN PAGE AND GET TITLE " + d, "Error: " + str(e)
                self.verificationErrors.append(str(e))
                
            else:
            	L.log(BROWSERS[x], test, "PASS, PAGE OPENS, TITLE ACQUIRED", d)
            	
                if re.search(text, title, re.I):
                    L.log(BROWSERS[x], test, "PASS, CORRECT PAGE LOADS", d)
                        
                elif (re.search("not found", title, re.I) or re.search("500", title)):
                    L.log(BROWSERS[x], test, "FAIL, 404/500 ERROR", d)
                    self.verificationErrors.append(d)
                    	
                else:
                    print "Test has a bug / exception, verify:"
                    print "Link: " + d, "Title: " + title, "Text: " + text
                    
                sel.go_back()
                sel.wait_for_page_to_load("50000")
                 
            n += 1   
            
        ########################################################################    
            
    def c_link_count(self):
    	    
    	"""
    	This test counts the number of links in the copyright/corporate section of the vulture.com footer using CSS selectors
    	
    	PASSING CONDITIONS:	11 links are in the copyright footer (as of 5/9/12)
    				The copyright statement (CONTENT global variable) is present on the page
    				
    	FAILING CONDITIONS:	(Not) 11 links are present on the page in the copyright footer
    				(10 or fewer, 12 or more)
    				The copyright statement is not on the page
    				
    	"""
    	    
    	sel = self.selenium
    	test = "Test C - Counting Links in Footer, Verifying Copyright Statement"
    	print test
            
        count = sel.get_css_count("css=" + CSS[2])
        
        if count != 11:
            L.log(BROWSERS[x], test, "FAIL, MISSING LINKS IN COPYRIGHT FOOTER", str(count) + " links found")
            self.verificationErrors.append("Missing Links " + str(count))
            print "LINKS MISSING FROM FOOTER"
            
        # Make sure the copyright statement is on the page
            	
        if sel.is_text_present(CONTENT):
            L.log(BROWSERS[x], test, "PASS, COPYRIGHT STATEMENT IS PRESENT", CONTENT)
           
        else:
            L.log(BROWSERS[x], test, "FAIL, TEXT NOT PRESENT", CONTENT)
            self.verificationErrors.append("Copyright statement not present: " + CONTENT)
            print "COPYRIGHT STATEMENT NOT PRESENT" 	
            
        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(CpFooter)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
    
