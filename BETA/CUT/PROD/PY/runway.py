#! /usr/bin/python                                                                                                                                                                                  
# -*- coding: utf-8 -*-

import sys
import os
import re
import httplib
import urllib
import urlparse
import unittest
import HTMLTestRunner
import string
import time
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")


"""
This test checks for features common to all splash pages, such as css sheets, facebook login,
the footer, global navigation, cut navigation, The Cut logo, etc.
Specific elements for splash pages are in the corresponding splash test: i.e., beautysplash.py
will test for things unique to the beauty splash page.

"""

class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


class RunwayOpenerSplash(unittest.TestCase):

    def setUp(self):

        self.BASEURL = show
        
        self.req = MyOpener()
        self.page = self.req.open(self.BASEURL)
        self.text = self.page.read()
        self.page.close()
        self.soup = BeautifulSoup(self.text)
        self.spam = self.soup.find_all
        self.verificationErrors = []
        
        ################################################################################
        
    def test_css_sheets(self):
    	    
    	self.assertNotEqual(self.soup.find('link', attrs={'rel':'stylesheet', \
    			'href':'http://cloud.webtype.com/css/b96bd528-3e1d-4b4a-b530-830f69cfca6c.css', \
    			'media':'all'}), None) 
    	
	self.assertNotEqual(self.soup.find('link', attrs={'rel':'stylesheet', \
    			'href':'http:'+ CACHE + 'css/screen/nym/nymCore.css', \
    			'media':'all'}), None)
    	
    	self.assertNotEqual(self.soup.find('link', attrs={'rel':'stylesheet', \
    			'href':'http:'+ CACHE + 'css/screen/thecut/css/thecut_screen.css', \
    			'media':'all'}), None)
    	
    	self.assertNotEqual(self.soup.find('link', attrs={'rel':'stylesheet', \
    			'href':'http:'+ CACHE + 'css/screen/echo.css', \
    			'media':'all'}), None)
    	
    	################################################################################
    	
    def test_facebook(self):
    	    
    	self.assertNotEqual(self.soup.find('meta', attrs={'property':'fb:app_id', 'content':'134556739904777'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'property':'og:title', 'content':True}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'property':'og:description', 'content':True}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'property':'og:site_name', 'content':'The Cut'}), None)
    	#self.assertNotEqual(self.soup.find('meta', attrs={'property':'og:image', 'content':'http://images.nymag.com/images/2/graphics/fb/thecut-fb-icon.jpg'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'property':'og:url', 'content':True}), None)
    	
    	################################################################################
    	
    def test_twitter(self):
    	 
        self.assertNotEqual(self.soup.find('meta', attrs={'name':'twitter:card', 'content':'summary'}), None)
    	self.assertNotEqual(self.soup.find('meta', attrs={'name':'twitter:site', 'content':'@TheCut'}), None)
	
	################################################################################
	
    def test_ads(self):
    	
    	self.assertNotEqual(self.soup.find('script', attrs={'src':CACHE + 'ads/config/thecut.js'}), None)
    	self.assertNotEqual(self.soup.find('script', attrs={'src':CACHE + 'scripts/nym/nymAds.js'}), None)
    	
    	self.assertNotEqual(self.soup.find('div', attrs={'class':'nym-ad', 'id':'leaderboard-desktop', 'data-ad-size':'980x60,980x30,970x90,728x90'}), None)
    	self.assertNotEqual(self.soup.find('div', attrs={'class':'nym-ad', 'id':'leaderboard-tablet', 'data-ad-size':'728x90,728x91'}), None)
    	self.assertNotEqual(self.soup.find('div', attrs={'class':'nym-ad', 'id':'leaderboard-tablet-mobile', 'data-ad-size':'480x60,480x61'}), None)
    	self.assertNotEqual(self.soup.find('div', attrs={'class':'nym-ad', 'id':'leaderboard-mobile', 'data-ad-size':'300x50,320x50'}), None)
    	
    	self.assertNotEqual(self.soup.find('div', attrs={'class':'nym-ad', 'data-id':'ad-skyscraper', 'data-ad-size':'300x250,300x600'}), None)
    	
    	self.assertNotEqual(self.soup.find('div', attrs={'class':'nym-ad', 'id':'footer-tablet-desktop', 'data-ad-size':'728x90,728x91'}), None)
    	self.assertNotEqual(self.soup.find('div', attrs={'class':'nym-ad', 'id':'footer-tablet-mobile', 'data-ad-size':'480x60,480x61'}), None)
    	self.assertNotEqual(self.soup.find('div', attrs={'class':'nym-ad', 'id':'footer-mobile', 'data-ad-size':'300x50,300x51,320x50,320x51'}), None)
    	self.assertNotEqual(self.soup.find('div', attrs={'class':'nym-ad', 'id':'footer-desktop', 'data-ad-size':'970x90,970x91,728x90,728x91'}), None)
    	
    
    	################################################################################
        	
    def test_tracking(self):
    	   
    	for tag in self.spam('div', attrs={'id':'analytics'}):
            
            tracking = tag
              
	    self.assertNotEqual(tracking.find('div', attrs={'id':'analytics-omniture'}).contents, [])
	    self.assertNotEqual(tracking.find('div', attrs={'id':'analytics-quantcast'}).contents, [])
	    self.assertNotEqual(tracking.find('div', attrs={'id':'analytics-buzzfeed'}).contents, [])
	    self.assertNotEqual(tracking.find('div', attrs={'id':'analytics-nielsen'}).contents, [])
	    self.assertNotEqual(tracking.find('div', attrs={'id':'analytics-google'}).contents, [])
	    self.assertNotEqual(tracking.find('div', attrs={'id':'analytics-chartbeat'}).contents, [])
	    self.assertNotEqual(tracking.find('div', attrs={'id':'analytics-optimizely'}).contents, [])
    
        ################################################################################
        
    def test_login(self):
    	
    	"""
    	NEW FEATURE FOR FUTURE
    	<script src="//stg.nymetro.com/scripts/loginRegister.js"></script>
    	<script src="//stg.nymetro.com/scripts/echo/core/v2.6.14/backplane.js"></script>

	"""
	
    	self.assertNotEqual(self.soup.find('li', attrs={'class':'facebook navSocial-list-item'}), None)
    	self.assertNotEqual(self.soup.find('fb:like', attrs={'href':'http://www.facebook.com/Cut'}), None)  
    	self.assertNotEqual(self.soup.find('li', attrs={'class':'twitter navSocial-list-item last'}), None)
    	self.assertNotEqual(self.soup.find('a', attrs={'class':'twitter-follow-button', 'href':'https://twitter.com/TheCut'}), None)
    	
    	self.assertNotEqual(self.soup.find('div', attrs={'id':'logged_in_bar', 'class':'membership'}), None)
    	self.assertNotEqual(self.soup.find('div', attrs={'id':'logged_out_bar', 'class':'membership'}), None) 
    	self.assertNotEqual(self.soup.find('a', attrs={'id':'nav-mynewyork', 'href':'http://my.nymag.com'}), None)
    	self.assertNotEqual(self.soup.find('a', attrs={'class':'login-lightbox', 'href':'/accountcenter/login.cgi'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'register-lightbox', 'href':'/registration/'}), None)

        ################################################################################
        
    def test_globalnav(self):
    	    
    	self.assertNotEqual(self.soup.find('ul', attrs={'class':'global'}), None)
    	self.assertNotEqual(self.soup.find('li', attrs={'class':'home'}), None)  
    	self.assertEqual(str(self.soup.find('a', attrs={'class':'nymagNetwork', 'href':'javascript:;'}).string), 'Our Sites')
    	self.assertEqual(str(self.soup.find('a', attrs={'class':'nymagLink', 'href':'/'}).string), 'nymag.com')
		
    	self.assertNotEqual(self.soup.find('ul', attrs={'class':'childSites'}), None)
    	self.assertEqual(str(self.soup.find('a', attrs={'href':'/daily/intel/'}).string), 'Daily Intel')
    	self.assertEqual(str(self.soup.find('a', attrs={'href':'http://www.vulture.com/'}).string), 'Vulture')
    	self.assertEqual(str(self.soup.find('a', attrs={'href':'/thecut/'}).string), 'The Cut')
    	self.assertEqual(str(self.soup.find('a', attrs={'href':'http://newyork.grubstreet.com/'}).string), 'Grub Street')
		
    	self.assertNotEqual(self.soup.find('li', attrs={'class':'top the-magazine'}), None)
    	self.assertEqual(str(self.soup.find('a', attrs={'id':'nav-mag', 'class':'top', 'href':'/includes/tableofcontents.htm'}).string), 'The Magazine')
    	self.assertNotEqual(self.soup.find('div', attrs={'id':'sub_nav_mag'}), None)
    	self.assertNotEqual(self.soup.find('a', attrs={'title':'See the current issue of New York', 'href':'/includes/tableofcontents.htm'}), None)
    	self.assertNotEqual(self.soup.find('img', attrs={'src':'http://images.nymag.com/current_issue.jpg'}), None)
    	
    	#self.assertEqual(str(self.soup.find('a', attrs={'href':'/includes/tableofcontents.htm', 'name':None}).string), 'Table of Contents')
    	self.assertEqual(str(self.soup.find('a', attrs={'href':'/redirects/circ_subscribe/utility-bar.html'}).string), 'Subscribe Now')
    	self.assertEqual(str(self.soup.find('a', attrs={'href':'/redirects/circ_gifts/utility-bar.html'}).string), 'Give a Gift Subscription')
    	self.assertEqual(str(self.soup.find('a',attrs={'href':'https://secure.palmcoastd.com/pcd/eServCart?iServ=MDM5MjEzODM0Mg=='}).string), 'Buy Back Issues')
    	self.assertEqual(str(self.soup.find('a', attrs={'href':'/includes/issuearchive.htm'}).string), 'Online Issue Archive')
    	self.assertEqual(str(self.soup.find('a', attrs={'href':'https://secure.palmcoastd.com/pcd/eServ?iServ=MDM5MjEyNDE2Ng=='}).string), 'Customer Service: Contact Us!')
    	self.assertEqual(str(self.soup.find('a', attrs={'href':'/newyork/mediakit/'}).string), 'Media Kit')
    	
        ################################################################################
        
    def test_footer(self):
    		
    	self.assertNotEqual(self.soup.find('ul', attrs={'class':'footerNav footerModuleNav'}), None)
    	self.assertNotEqual(self.soup.find('div', attrs={'class':'theCutLogo'}), None)  
        self.assertNotEqual(self.soup.find('ul', attrs={'class':'footerNav footerCompanyNav'}), None)
        self.assertNotEqual(self.soup.find('div', attrs={'class':'nyMagLogo'}), None)
        
        self.assertNotEqual(self.soup.find('li', attrs={'class':'listItem'}), None)
        self.assertNotEqual(self.soup.find('li', attrs={'class':'listItem footer-fame'}), None)
        self.assertNotEqual(self.soup.find('li', attrs={'class':'listItem footer-contact-us'}), None)
        self.assertNotEqual(self.soup.find('li', attrs={'class':'listItem footer-apps'}), None)
        
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/thecut/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/thecut/fashion/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/thecut/runway/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/thecut/street-style/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/thecut/celebrities/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/thecut/beauty/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/thecut/shopping/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/thecut/love/'}), None)
        
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/newyork/jobs/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/newyork/privacy/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/newyork/terms/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/newyork/aboutus/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/contactus/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/newyork/mediakit/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/newyork/rss/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/newsletters/#'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/apps/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/sitemap/'}), None)
        self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'/newyork/privacy/#ad-choices'}), None)
        #self.assertNotEqual(self.soup.find('a', attrs={'class':'listItemLink', 'href':'#'}), None)
        
        self.assertNotEqual(self.soup.find('p', attrs={'class':'paragraph desktop'}), None)
        self.assertNotEqual(self.soup.find('p', attrs={'class':'paragraph mobile'}), None)
        self.assertNotEqual(self.soup.find('p', attrs={'class':'paragraph tablet'}), None)
        self.assertNotEqual(self.soup.find('span', attrs={'class':'year'}), None)
        
        ################################################################################
        
    def test_cutlogo(self):
    	    
    	self.assertNotEqual(self.soup.find('a', attrs={'class':'cutLogo', 'href':'/thecut/'}), None)
    	self.assertNotEqual(self.soup.find('a', attrs={'class':'cutHomeLink', 'href':'/thecut/'}), None)
    	    
    	################################################################################
    	
    def test_cutnav(self):
    	
    	self.assertNotEqual(self.soup.find('a', attrs={'class':'sectionLink', 'href':'/thecut/fashion/'}), None)
    	self.assertNotEqual(self.soup.find('a', attrs={'class':'sectionLink', 'href':'/thecut/runway/'}), None)
    	self.assertNotEqual(self.soup.find('a', attrs={'class':'sectionLink', 'href':'/thecut/street-style/'}), None)
    	self.assertNotEqual(self.soup.find('a', attrs={'class':'sectionLink', 'href':'/thecut/celebrities/'}), None)
    	self.assertNotEqual(self.soup.find('a', attrs={'class':'sectionLink', 'href':'/thecut/beauty/'}), None)
    	self.assertNotEqual(self.soup.find('a', attrs={'class':'sectionLink', 'href':'/thecut/shopping/'}), None)
    	self.assertNotEqual(self.soup.find('a', attrs={'class':'sectionLink', 'href':'/thecut/love/'}), None)
    	
        ################################################################################
    	
    def test_search(self):
    	
    	self.assertNotEqual(self.soup.find('form', attrs={'id':'ny-search', 'method':'get', 'action':'http://nymag.com/search/search.cgi'}), None)
    	self.assertNotEqual(self.soup.find('fieldset', attrs={'class':'txt', 'id':'ny-search-fieldset'}), None)
    	self.assertNotEqual(self.soup.find('input', attrs={'type':'hidden', 'name':'fd'}), None)
    	self.assertNotEqual(self.soup.find('input', attrs={'type':'hidden', 'name':'Ns'}), None)
    	self.assertNotEqual(self.soup.find('input', attrs={'type':'hidden', 'name':'search_type'}), None)
    	self.assertNotEqual(self.soup.find('input', attrs={'type':'hidden', 'name':'N'}), None)
    	self.assertNotEqual(self.soup.find('input', attrs={'type':'text', 'id':'txt-ny-search'}), None)
    	self.assertNotEqual(self.soup.find('button', attrs={'type':'submit', 'id':'btn-ny-search'}), None)
    	
    	################################################################################
    	
    def tearDown(self):

        self.assertEqual([], self.verificationErrors)
        
        ################################################################################


"""   
FUTURE FEATURE:

def fail_writer(test):
	
    test = test	
    t = datetime.time
    print t
    f = open('../failures.txt')
    f.write(t + '\t' + BASEURL + '\n')
    print test

"""

for x in range(0,3):
	
    if x == 0:
    	ENV = 'stg'
    	CACHE = '//stg.nymetro.com/'
	SHOWS = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/stg.runway_shows.txt', 'r').readlines()	
    
    elif x == 1:
    	ENV = 'ec2'
    	CACHE = '//dev.nymag.biz/'
        SHOWS = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/ec2.runway_shows.txt', 'r').readlines()
        
    else:
    	ENV = 'prod'
    	CACHE = '//cache.nymag.com/'
    	SHOWS = open('/Users/nsmith/Desktop/BETA/CUT/DATA/TEXT/prod.runway_shows.txt', 'r').readlines()

    for s in range(len(SHOWS)):
    	show = SHOWS[s].strip('\n')
    	filename = show.split('/')
    
        results = open('../../DATA/HTML/RUNWAY/OPENER/' + filename[-1] + '.runway.html', 'wb')
        print "TESTING " + show
        suite = unittest.TestLoader().loadTestsFromTestCase(RunwayOpenerSplash)
        unittest.TextTestRunner(verbosity=2).run(suite)
        runner = HTMLTestRunner.HTMLTestRunner(stream=results, title=show, description='Results for Runway on ' + ENV)
        runner.run(suite)
        
        s += 1
        
    x += 1
