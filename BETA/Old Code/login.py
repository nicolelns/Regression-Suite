#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from selenium import webdriver
from selenium.webdriver.remote import command
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import pickle
import Logger

reload(sys)
sys.setdefaultencoding("utf-8")

chromedriver = '/Library/Python/2.7/site-packages/chromedriver'

"""
The below code is for the Internet Explorer remote driver; These tests were developed on a Mac :)
"""

x = 0

PROXY = "localhost:8080"

webdriver.DesiredCapabilities.INTERNETEXPLORER['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}

BROWSERS = ('chrome', 'firefox', 'ie')
TEST = "The Cut Login and Registration - Desktop - The Cut"

CSS = open('../data/text/nymaglogin.css.txt', 'r').readlines()
NYM_CREDS = pickle.load(open('../data/pickle/login.p', 'rb'))	# Dictionary with NYMag login credentials
#FB_CREDS = pickle.load(open('../data/pickle/fb_login.p', 'rb'))	# Dictionary with FB login credentials

nym_usr = NYM_CREDS.keys()		# Usernames
nym_pwd_list = NYM_CREDS.values()	# Password list for each username


"""
This is a test for the Cut Login and Registration.
The DATA file is a pickle file generated by cutSoup.Parser(), customized for this module.
IF ANY CHANGES TO THE MODULE HAPPEN, PLEASE ONLY CHANGE THE .TXT, .P and .JSON FILES IF YOU REALLY KNOW WHAT YOU ARE DOING!
"""	

#########################################################################
#########################################################################

class Login(unittest.TestCase):

    def setUp(self):
    	    
        if x == 0:
            self.driver = webdriver.Chrome(chromedriver)
            
        elif x == 1:    
            self.driver = webdriver.Firefox() 
            
        elif x == 2:
    	    self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.INTERNETEXPLORER)
            
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        print "TESTING qa.cut.com in " + BROWSERS[x]
 
	########################################################################
	
    def test_login(self):
        
        """
        Preliminary test for the presence of various elements in the updated NY Mag navigation bar.
        CSS selectors are in a .txt file, and this test makes sure each element exists on the page before proceeding.
        Failures will fail the whole test.  (No point in continuing if images and links aren't present, right?).
        The other tests are called from this function to avoid repetitive and unnecessary SetUp and TearDown of the browser.
        In addition, the other tests can be commented out and not run - easy to select which tests run.  None are dependent on 
        results from other tests.  Only test_splash_feed needs to be run for the sub-tests to run.
        
        PASSING CONDITIONS:  All elements are present on the page.
        FAILING CONDITIONS:  Any ONE element is not present on the page.
        """
	
        n = 0
        driver = self.driver
        driver.get(BASEURL)
        asdf
        #test = "Test A - Presence of elements via CSS"
        
        # Loops through the data in the CSS file asserting each element is on the page
        """
        for each in CSS:		
        	
	    c = CSS[n].strip('\n')
            
            try:
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, c))
                
            except AssertionError, e:
            	print "FAILURE " + c
            	self.verificationErrors.append(str(e))
                L.log(BROWSERS[x], test, "FAIL, ELEMENT NOT FOUND", c, exception=str(e))
            
            else:
                L.log(BROWSERS[x], test, "PASS, ELEMENT FOUND", c)
                
            n += 1
        """
            
        self.b_nymag_login()
        #self.e_facebook_login()
        
	########################################################################
	
    def lightbox_close(self):
    	    
    	driver = self.driver
    	
    	try:
    	    driver.find_element_by_class_name("closelightbox").click()
    	
	except Exception, e:
    	    return False
    	    
    	return True
    	  
	########################################################################
	
    def back_to_page(self):
    	    
    	driver = self.driver
    	
    	try:
    	    driver.find_element_by_id("returnpage").click()
    	
	except Exception, e:
    	    return False
    	    
    	return True
    	      
	########################################################################	
	    
    def status_error(self):
    	    
    	driver = self.driver    
    	    
    	try:
	    driver.find_element_by_id("login_status").is_displayed()
	    
	except Exception, e:
	    self.lightbox_close()
	    return False
	    
	return True
 
        ########################################################################
	    
    def nym_login_form_fill(self, usr, pwd):
    	    
    	"""
    	This portion of code fills out the NY Mag (non-Facebook) login form.
    	Variables: usr is the username, pwd is the password.  The data are stored in a pickle file
    	and include a correct email, a correct username, an incorrect email, an incorrect username and a blank
    	email/username, each with a correct, incorrect and blank password.
    	
    	If the status-wrp error message appears during filling out the form, the function will
    	return False, indicating that the nym_login function should take a different line of action.
    	"""
    	    
    	driver = self.driver
    	self.usr = usr
    	self.pwd = pwd
    	
    	try:
	    driver.find_element_by_id("id_login").send_keys(self.usr)
	    driver.find_element_by_id("id_password").send_keys(self.pwd)
	    driver.find_element_by_id("id_remember").click()	# Uncheck - remember me will be tested later in this script
	    
	except Exception, e:
	    print "FAIL with form fill NYMAG", str(e)
	    self.lightbox_close()
	    return False
	    
	return True
	    
	########################################################################
	
    
    def fb_login_form_fill(self, usr, pwd):
    	    
    	driver = self.driver
    	self.usr = usr
    	self.pwd = pwd
    	    
        driver.switch_to_window('f1-4')
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").send_keys('nicole.smith@nymag.com')
        driver.find_element_by_id("pass").click()
        driver.find_element_by_id("pass").send_keys('qatest1')
            
        ########################################################################
        
    def logout(self):
    	    
    	driver = self.driver
    	
    	try:
    	    driver.find_element_by_link_text("Log Out").click()
    	
    	except Exception, e:
    	    return False
    	    
    	return True
    	
	########################################################################
	
    def b_nymag_login(self):	
    	    
       	"""
    	The sign in function signs the user in to NY Mag/The Cut.
    	
    	PASSING CONDITIONS:  User can log in
    	FAILING CONDITIONS:  User can not log in
    	"""	
    
        m = n = 0
        driver = self.driver
        asdf
        test = "Test B - NY Mag Log In"
        print test
        
        for each in NYM_CREDS:
        	
            usr = nym_usr[m]
            pwd_list = nym_pwd_list[m]
                
            for n in range(0,3):
            	  
		pwd = pwd_list[n]
                
                try:
                    driver.find_element_by_class_name("login-lightbox").click()
                    self.nym_login_form_fill(usr, pwd)
                    if self.nym_login_form_fill(usr, pwd) is True:
                        driver.find_element_by_id("submit1").click()
                        time.sleep(3)
                        error = self.status_error()
                        if error is True:
                    	    raise Exception
                    	    
                    else:
                        raise Exception
                    
                except Exception, e:
                    
                    if (m == 0 and n == 0) or (m == 1 and n == 0):	# Correct username/email and correct pwd
                        self.lightbox_close()
            	    	L.log(BROWSERS[x], test, "FAIL, CANNOT LOG IN NYMAG", BASEURL, exception=str(e))
            	       
           	    else:
           	   	L.log(BROWSERS[x], test, "PASS, NYMAG LOGIN - INTENTIONAL FAIL - INCORRECT CREDENTIALS", BASEURL)
           	        
        	else:
        	    self.logout()
        	    if (m == 0 and n == 0) or (m == 1 and n == 0):
            	    	L.log(BROWSERS[x], test, "PASS, LOG IN NYMAG WORKS", BASEURL)
            	        
           	    else:
           	   	L.log(BROWSERS[x], test, "FAIL, NYMAG LOGIN - INCORRECT CREDENTIALS SHOULD NOT LOG USER IN", BASEURL)    	
           	
        	n += 1
        	
	    m += 1	
            
        ########################################################################    
        
    def c_nymag_register(self):
    	    
    	"""
    	The sign in function signs the user in to NY Mag/The Cut.
    	
    	PASSING CONDITIONS:  User can log in
    	FAILING CONDITIONS:  User can not log in
    	"""	
    
	m = n = 0
        driver = self.driver
        
        test = "Test B - NY Mag Log In"
        print test
        
        for each in NYM_CREDS:
        	
            usr = nym_usr[m]
            pwd_list = nym_pwd_list[m]
            #driver.refresh()
                
            for n in range(0,3):
            	  
		pwd = pwd_list[n]
                
                try:
                    driver.find_element_by_class_name("register-lightbox").click()
                    
                except Exception, e:
                    return False
                   
                n += 1
                    
        ########################################################################    
                
    def nymag_register_form_fill(self):
    	    
    	driver = self.driver
    	self.usr = usr
    	self.pwd = pwd
    	
    	try:
	    driver.find_element_by_id("id_membername").send_keys(self.usr)
	    driver.find_element_by_id("id_email_address").send_keys(self.pwd)
	    driver.find_element_by_id("id_password").send_keys()
	    driver.find_element_by_id("id_confirm_password").send_keys()
	    driver.find_element_by_id("id_zip").send_keys()
	    driver.find_element_by_id("id_gender_0").click()	
	    driver.find_element_by_id("id_gender_1").click()
	    driver.find_element_by_id("recaptcha_response_field").click()
	    #id_newsletter is checked
	    #toggle id_newsletter
	    #id_tos not checked
	    # toggle id_tos
	    #is present href="https://secure.nymag.com/newyork/terms/index.html">Terms of Service
	    # is present  href="https://secure.nymag.com/newyork/privacy/index.html">Privacy Policy</a>
	    #register = id submit1
		
	    """
	    Errors:
	    "membername_status"  status-wrp status-error
	    "email_address_status"
	    "password status"
	    "confirm_password_status"
	    "zip_code_status"
	    status_wrap status_ok
	    Membername already taken
	    "captcha_status"
	    "tos_status"
	    
	    """
	    
	except Exception, e:
	    print "FAILure with form fill NYMAG", str(e)
	    self.lightbox_close()    
    	    
        ########################################################################
	 
    def e_facebook_login(self):
    	    
        m = n = 0    
        driver = self.driver
        test = "Test B - Log In"
        print test
        
        for each in NYM_CREDS:
        	
            usr = nym_usr[m]
            pwd_list = nym_pwd_list[m]
            driver.refresh()
                
            for n in range(0,3):
            	  
		pwd = pwd_list[n]
		
		for r in range(0,2):	# Tests both the Facebook button next to log-in link and the fb button in the login popup window
        	
                    try:
                        if n == 0:
                            driver.find_element_by_class_name("fb_login").click()
            	    
                        else:
            	            driver.find_element_by_class_name("login-lightbox").click()
            	            driver.find_element_by_link_text("FACEBOOK LOGIN").click()
            	            print "I just clicked the FACEBOOK button!"
           
                    	self.fb_login_form_fill()
                    	driver.find_element_by_name("login").click()
                    	print "I just logged in!"
                    	time.sleep(5)
                    	driver.switch_to_window('f1-2')
                    	#driver.find_element_by_name("grant_clicked").click()
                    	time.sleep(5)
                   
                    except Exception, e:
                    	print "FAIL", str(e)
                    	L.log(BROWSERS[x], test, "FAIL, CANNOT LOG IN NYMAG", BASEURL, exception=str(e))
	        
	            else:
	            	driver.find_element_by_link_text("Log Out").click()
	            	L.log(BROWSERS[x], test, "PASS, LOG IN NYMAG WORKS", BASEURL)
	            	print "I logged out"
	    
	            time.sleep(1)
	            r += 1
	        
	        n += 1
	        
	    m += 1
		
	########################################################################
 	
    def is_element_present(self, how, what):
    	    
        try: 
            self.driver.find_element(by=how, value=what)
        
        except NoSuchElementException, e: 
            return False
        
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

#########################################################################
#########################################################################


URLS = open('../data/text/loginurls.txt', 'r').readlines()	# URLS to test login
y = 0

for each in URLS:

    BASEURL = URLS[y].strip('\n')
    print BASEURL, " is being opened"
    L = Logger.MainLogger(BASEURL, TEST)

    for x in range(0,2):

        suite = unittest.TestLoader().loadTestsFromTestCase(Login)
        unittest.TextTestRunner(verbosity=2).run(suite)
    
        x += 1
        
    y += 1
    
L.save()
