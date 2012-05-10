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
TEST = "Vulture Footer Section (Vulture and Network Promos - Desktop - Vulture Home Page)"

L = Logger.MainLogger(BASEURL, TEST)
S = vultureSoup.Parser()

S.footer()

CSS = open('../data/text/footer.css.txt', 'r').readlines()		
DATA = pickle.load(open('../data/pickle/footer.data.p', 'rb')) 
CONTENT = "Also In Our Network:"
      
x = 0

"""
This is a regression test for the footer of Vulture's home page
IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!  LINE ORDER FOR DATA INSIDE FILES MATTERS!	

"""
#########################################################################
#########################################################################
	

class Footer(unittest.TestCase):

    def setUp(self):

        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*" + BROWSERS[x], BASEURL + '/')
        self.selenium.start()
	print "TESTING " + BASEURL + " in " + BROWSERS[x]
	
	########################################################################
    
    def test_footer(self):

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
        
        # Loops through the data in the CSS file asserting each element is on the page
        
	for each in CSS:

	    c = CSS[n].strip('\n') 
        
            try:
                self.failUnless(sel.is_element_present("css=" + c))
                
            except AssertionError, e:
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], test, "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            
            else:
                L.log(BROWSERS[x], test, "PASS, ELEMENT FOUND", c)
                
            n += 1
            
        self.b_title_test()
        self.c_link_count_test()
            
        ########################################################################
	    
    def b_title_test(self):
    	    
    	"""
    	This test grabs the link text (text between <a></a> tags) for each link.  
    	Each page is clicked on to ensure that the link works.
    	The title of the opened page is acquired.
    	The title is searched for "not found", "404", etc to verify page load
    	
    	PASSING CONDITIONS:  Each link has text associated with it
    			     Each link can be clicked on
    			     Each page loads and has a title
    			     
    	FAILING CONDITIONS:  Links have no text for the user to see/click on aka headline does not show
    			     Links cannot be clicked on
    			     Pages do not load or have "not found" in the title
    			     
    	
    	"""
    	
        #n = 0	# http://www.vulture.com causes a bug
	sel = self.selenium
	test = "Test B - Do the Links Open the Right Pages?"
	print test
        
	#for each in DATA:
	
	for n in range(1,len(DATA)):
	
	    d = DATA[n] 
            
            try:
            	if d == "http://www.vulture.com":
            	    title = "Vulture"
            	    pass
            
            	else:
            	    sel.click("//a[@href='" + d + "']")
            	    sel.wait_for_page_to_load("50000")
            	    title = sel.get_title()
                
            except AssertionError, e:
            	L.log(BROWSERS[x], test, "FAIL, CANNOT OPEN PAGE AND GET TITLE", d, exception=str(e))
                print "FAILURE, CAN'T OPEN PAGE AND GET TITLE " + d, "Error: " + str(e)
                self.verificationErrors.append(str(e))
                
            else:
            	L.log(BROWSERS[x], test, "PASS, PAGE OPENS", d)
            	
                if (re.search("not found", title, re.I) or re.search("500", title)):
                    L.log(BROWSERS[x], test, "FAIL, 404/500 ERROR", d)
                    self.verificationErrors.append("404 Error" + d)
                    
                else:
                    L.log(BROWSERS[x], test, "PASS, NO 404/500 ERROR", d)
                    
                sel.go_back()
                sel.wait_for_page_to_load("50000")
                 
            n += 1    
            
        ########################################################################   
            
    def c_link_count_test(self):
    	    
        """
    	This test counts the number of links in the footer.  This test runs agains the part of the footer
        on vulture.com containing vulture links, nymag links and grub street links, etc.
    	
    	PASSING CONDITIONS:  All links appear in the footer
    			     Network Promo statement on page
    			     
    	FAILING CONDITIONS:  Some links are missing from the footer
    			     Network Promo statement not on page
    	
    	"""
    	
        n = 0
	sel = self.selenium
	test = "Test C - Number of Links in Footer"
	print test  
	
	try:
            count_v = sel.get_css_count("css=" + CSS[2])            # Vulture links
            count_ny = sel.get_css_count("css=" + CSS[8])           # NY Mag, MenuPages and Grub Street links
            count_p = sel.get_css_count("css=" + CSS[7])            # Paragraphs for NY Mag and Grub Street Promos
        
	except Exception, e:
		L.log(BROWSERS[x], test, "FAIL, CANNOT GET CSS COUNTS FOR ITEMS", "Vulture Links: " + str(count_v) + " NY Mag Links: " + str(count_ny) + " Grub Street Promos: " + str(count_p), exception=str(e))
		self.verificationErrors.append("FAILURE, SEE LOGS FOR CSS COUNTS")
		return
		
	if ((count_v != 8) or (count_ny != 10) or (count_p != 2)):
            L.log(BROWSERS[x], test, "FAIL, MISSING FOOTER LINKS", str(count_p) + " paragraphs, " + str(count_ny) + " NY Mag links, and "+ str(count_v) + " vulture links found")
            
        if sel.is_text_present(CONTENT):
            L.log(BROWSERS[x], test, "PASS, TEXT PRESENT", CONTENT)
           
        else:
            L.log(BROWSERS[x], TEST, "FAIL, TEST NOT PRESENT", CONTENT)
            print "Network statement is NOT present, FAIL" 	
            
        ########################################################################

    def tearDown(self):

        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################

for each in BROWSERS:

    suite = unittest.TestLoader().loadTestsFromTestCase(Footer)
    unittest.TextTestRunner(verbosity=2).run(suite)
    x += 1
L.save()
