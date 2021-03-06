#! /usr/bin/python

import unittest
import time, datetime
import re
import pickle
import Logger			# Logging module (for test results, outputs results to a .txt file)
import vultureSoup		# BeautifulSoup page scraper collects relevant data from vulture.com
from selenium import selenium   # Update to WebDriver 

BASEURL = 'http://www.vulture.com'
BROWSERS = ('chrome', 'firefox', 'safari')
TEST = "Big Interview Module - Desktop - Vulture Home Page"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.biginterview()		# Call the relevant BeautifulSoup function (usually same name as test)

CSS = open('../data/text/biginterview.css.txt', 'r').readlines()		
DATA = pickle.load(open('../data/pickle/biginterview.data.p', 'rb')) 

keys = DATA.keys()
values = DATA.values()

x = 0
"""
This is a test for Vulture's large Interview Module.
The DATA file is a pickle file generated by vultureSoup.Parser(), customized for this module.
IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT, .P and .JSON FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!

"""	

#########################################################################
#########################################################################
	

class BigInterview(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING www.vulture.com in " + BROWSERS[x]
	
	########################################################################
    
    def test_biginterview(self):

        """
        Preliminary test for the presence of various elements in the Large Interview module.
        CSS selectors are in a .txt file, and this test makes sure each element exists on the page before proceeding.
        Failures will fail the whole test.  (No point in continuing if links aren't present, right?).
        The other tests are called from this function to avoid repetitive and unnecessary SetUp and TearDown of the browser.
        In addition, the other tests can be commented out and not run - easy to select which tests run.  None are dependent on 
        results from other tests.  Only test_biginterview needs to be run for the sub-tests to run (unless you comment them out)
        
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
            
        self.b_title_test()	#Comment these out in order to control what tests run
        self.c_interview_logo_test()
        self.d_image_link_match_test()
        self.e_author_test() 
         
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
    			     Verifies that headline is showing
    			     **The page title matches the link text
    			     
    	FAILING CONDITIONS:  Links have no text for the user to see/click on aka headline does not show
    			     Links cannot be clicked on
    			     Pages do not load or have "not found" in the title
    			     **The page title does not match the link text
    			     
    	
    	"""
    	
        n = 0
	sel = self.selenium
	test = "Test B - Do the Links Open the Right Pages?"
	print test
        
	for each in DATA:

	    d = keys[n] 
        
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
                    self.verificationErrors.append("404 Error" + d)
                    
                else:
                    print "Test has a bug / exception, verify:"
                    print "Link: " + d, "Title: " + title, "Text: " + text
                    
                sel.go_back()
                sel.wait_for_page_to_load("50000")
                 
            n += 1    
            
        ########################################################################

    def c_interview_logo_test(self):
    	    
        """
	This test makes sure that there are two links to the interviews splash page.
	The Interview header at the top of the module and the More Interviews image at the bottom of the 
	module both direct the user to the Interviews splash page.
	
	PASSING CONDITIONS:	The logos are both present and clicking on both links directs the user to
				the vulture.com/news/chat-room/ splash page
	FAILING CONDITIONS:	The logos are not present or the links do not direct the user to the correct
				page or the page returns a 404/500 error
	
	"""
    	
    	m = 0 
        sel = self.selenium
        test = "Test C - Interview Logo/Link Functionality"
        print test
        TEXT = ("More Interviews", "interview")
        
        # First, make sure each link can be clicked on and that the page loads
        
        for each in TEXT:
	    
	    try:
	    	sel.click("link=" + TEXT[m])
                sel.wait_for_page_to_load("50000")
                
	    except Exception, e:
	    	print "FAILURE " + TEXT[m], str(e)
		self.verificationErrors.append("Failure " + TEXT[m])
		L.log(BROWSERS[x], test, "FAIL, IMAGE DOES NOT LOAD", TEXT[m], exception=str(e))
		
	    else:
	        title = sel.get_title()
	        if not (re.search('404', title) or re.search('500', title) or re.search('not found', title, re.I)):
	            L.log(BROWSERS[x], test, "PASS, Page loads", TEXT[m])
		    
	        else:
	            self.verificationErrors.append("Failure" + title)
	            L.log(BROWSERS[x], test, "FAIL, PAGE RETURNS AN ERROR", title)
		sel.go_back()
	        sel.wait_for_page_to_load("50000")
	            
	    m += 1

        ########################################################################
        
    def d_image_link_match_test(self):
    	    
    	"""
    	This test clicks on the interview module's silo image and gets the title.
    	It clicks on the link via the link text, gets the title and makes sure the same page loads both times
    	
    	PASSING CONDITIONS:	Image silo can be clicked on 
    				Title can be acquired
    				Link text (headline) can be clicked on
    				Title can be acquired
    				Titles match - same page loads
    				No 404/500 errors, etc
    	
	FAILING CONDITIONS:	One of the above fails
	
    	"""
    	    
    	m = 0 
        sel = self.selenium
        test = "Test D - Image Link Matches Permalink"
        print test
        
        for each in keys:
		
	    d = keys[m]
	    data = values[m]
	    c = data[0]           
	   
	    if c is not None:
	    
	        try:
                    sel.click("//img[@src='" + c + "']")
                    sel.wait_for_page_to_load("50000")
                    img_title = sel.get_title()
                
	        except Exception, e:
		    print "FAILURE " + c, str(e)
		    self.verificationErrors.append("Failure " + c)
		    L.log(BROWSERS[x], test, "FAIL, IMAGE DOES NOT LOAD/CANNOT GET TITLE", c, exception=str(e))
		
	        else:
	            L.log(BROWSERS[x], test, "PASS, IMAGE/PAGE LOADS", c)
		    sel.go_back()
	            sel.wait_for_page_to_load("50000")
	            
	            try:
	            	sel.click("link=" + img_title[:-11])
	            	sel.wait_for_page_to_load("50000")
	            	link_title = sel.get_title()
	            	
	            except Exception, e:
		        print "FAILURE " + d, str(e)
		        self.verificationErrors.append("Failure " + d)
		        L.log(BROWSERS[x], test, "FAIL, LINK DOES NOT LOAD/CANNOT GET TITLE", d, exception=str(e))
		    
		    else:
		    	if re.search(img_title, link_title, re.I):
	                    L.log(BROWSERS[x], test, "PASS, IMAGE HREF MATCHES LINK HREF", "Img: " + img_title + " Link: " + link_title)
	                else:
	                    L.log(BROWSERS[x], test, "FAIL, IMAGE HREF DOES NOT MATCH LINK HREF", "Img: " + img_title + " Link: " + link_title)
	                    self.verificationErrors.append("Failure" + d)
	                    
	    else:
	    	self.verificationErrors.append("ERROR NO IMAGE!")
	    	L.log(BROWSERS[x], test, "NO IMAGE ERROR", d)
	    	
	    m += 1
    	    
        ########################################################################	    
    	   
    def e_author_test(self):
    	
    	"""
    	This test clicks on the interview article author's link.
    	
    	PASSING CONDITIONS:	The author's link can be clicked and the page loads properly
    		
	FAILING CONDITIONS:	The author's link cannot be clicked or the page does not load	
	
    	"""
    	    
    	n = 0 
        sel = self.selenium
        test = "Test E - Author Link"
        print test
        
        data = values[0]
	author_list = data[2] 
        author = author_list[n]
        
        for each in author_list:
        
	    try:
	    	#sel.click("//a[@href='" + author + "']")  # Bug - does not work 
	    	sel.open(author)
		sel.wait_for_page_to_load("50000")
		title = sel.get_title()
			
	    except Exception, e:
		print "FAILURE " + author, str(e)
		self.verificationErrors.append("Failure " + author)
		L.log(BROWSERS[x], test, "FAIL, LINK DOES NOT LOAD/CANNOT GET TITLE", author, exception=str(e))
		    
	    else:
		#if re.search(author, title, re.I):	#Incorrect logic, add failure condition
		L.log(BROWSERS[x], test, "PASS, AUTHOR HREF LOADS CORRECT PAGE", author)

	    sel.go_back()
	    sel.wait_for_page_to_load("50000")
	    
	    n += 1

        ########################################################################

    def f_comment_test(self):
    	pass

        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(BigInterview)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()