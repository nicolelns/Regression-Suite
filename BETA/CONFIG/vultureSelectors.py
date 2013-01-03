import re
import os
import sys

"""
        This module contains CSS selectors for elements on Vulture's home page.
        The CSS selectors are only for objects that will be clicked on when
        used in a Selenium Webdriver test.  Each class is for a page, each page
        object has functions for components on each page.
        
        In order to access these selectors, import this module and create an 
        instance of this class as such:
        
        import vultureSelectors
        
        HomePage = vultureSelectors.HomePage()
        Selectors = HomePage.(<your-function-here>)
        ..where <your-function-here> is a call to one of the below functions 
        in this class
        
        Example: the small_pictures_module contains several css selectors assigned 
        to variables. 
        The function you call will return a tuple which can be accessed via 
        index in your test.

        Example use:
        
        Global = vultureSelectors.Global()
        GlobalSelectors = Global.footer()
        
        or
        
        HomePage = vultureSelectors.HomePage()
        HomePageSelectors = HomePage.news_feed()
    
        From there, you can assign variables to items in a tuple by index:
        
        vulture_logo = GlobalSelectors[0]
        vulture_links = GlobalSelectors[1]
        
        or
    
        entry_link = HomePageSelectors[2]
        entry_headline = HomePageSelectors[3]
        
        You can use more than one class' variables by assigning unique names to your
        class instances.  As above, you can use GlobalSelectors for the Global() class, and
        HomePageSelectors for the HomePage() class.  Use whatever names you like, the above
        was suggested as an organizational standard.
        
        Add variables to this module by assigning a well-named variable inside the correct 
        function to your CSS selector as a string.  Then, append your new variable 
        to the END of the returned tuple.  FAILURE TO DO SO WILL CAUSE THE INDICES OF 
        THE VAIRIABLES TO BE WRONG INSIDE OF THE SELENIUM TESTS.
        
        Example:
        
        return the_latest_link, ... nth var, <your-new-variable>
        
        IF THE SELECTOR IS INCORRECT, YOUR TEST WILL
        NOT WORK.
    
        """
        
class Global(self):
	
    def __init__(self):
    	pass  
        
    def universal_nav(self):
    	
    	"""
    	The below values are only for the production site.  The test environments
    	will have (some) urls like: http://stg.nymetro.com/daily/intelligencer/
    	
    	"""
    	
    	regex = re.compile('http:\/\/nymag.com\/nymag\/toc\/[0-9]{4}')
    	static_links = (('ul.global li.home a', 'http://nymag.com/'),
    		#('li[class*="top the-magazine"] a#nav-mag.top', str(regex)),
    		('ul.global > li:nth-child(3) > a','http://nymag.com/daily/intel/'),  #UPDATE TO INTELLIGENCER
    		('ul.global > li:nth-child(4) > a','http://www.vulture.com/'),
    		('ul.global > li:nth-child(5) > a','http://nymag.com/thecut/'),
    		('ul.global > li.last > a','http://newyork.grubstreet.com/'))
    	ul.global li.top div#sub_nav_mag ul li
    	hover_links = (('li[class*="top the-magazine"] a#nav-mag-hover', 'http://nymag.com/includes/tableofcontents.htm'),
    		('ul.global li.top div#sub_nav_mag ul li:nth-child(2) > a', 'http://nymag.com/redirects/circ_subscribe/utility-bar.html'),
    		('ul.global li.top div#sub_nav_mag ul li:nth-child(3) > a', 'http://nymag.com/redirects/circ_gifts/utility-bar.html'),
    		('ul.global li.top div#sub_nav_mag ul li:nth-child(4) > a', 'https://secure.palmcoastd.com/pcd/eServCart?iServ=MDM5MjEzODM0Mg=='),
    		('ul.global li.top div#sub_nav_mag ul li:nth-child(5) > a', 'http://nymag.com/includes/issuearchive.htm'),
    		('ul.global li.top div#sub_nav_mag ul li:nth-child(6) > a', 'https://secure.palmcoastd.com/pcd/eServ?iServ=MDM5MjEyNDE2Ng=='),
    		('ul.global li.top div#sub_nav_mag ul li.last > a', 'http://nymag.com/newyork/mediakit/'))  
    	
    	hover_image = 'div#sub-nav-mag > p > a > img'
    	mouseover_menu = 'a[id*="nav-mag"]'
    	
    	return static_links, hover_links, mouseover_menu, hover_image
    	
    def search(self):
    	    
    	search_bar = 'input.text'
    	radio_nymag = ''
    	radio_vulture = ''
    	search_button = 'button[id*="btn-ny-search"]'
    	
    	return search_bar, search_button
    
    def footer(self):
    	    
    	# Common to all pages
    	
    	vulture_links = (('section.vulture-promo h4 > header > a', 'http://www.vulture.com'),
    		('section.vulture-promo > ul:nth-child(1) > li > a', 'http://www.vulture.com/blog/'),
    		('section.vulture-promo > ul:nth-child(2) > li > a', 'http://www.vulture.com/movies/'),
    		('section.vulture-promo > ul:nth-child(3) > li > a', 'http://www.vulture.com/tv/'),
    		('section.vulture-promo > ul:nth-child(4) > li > a', 'http://www.vulture.com/music/'),
    		('section.vulture-promo > ul:nth-child(5) > li > a', 'http://www.vulture.com/books/'),
    		('section.vulture-promo > ul:nth-child(6) > li > a', 'http://www.vulture.com/art/'),
    		('section.vulture-promo > ul:nth-child(7) > li > a', 'http://www.vulture.com/theater/'),
    		('section.vulture-promo > ul:nth-child(8) > li > a', 'http://www.vulture.com/clickables/'),
    		('section.vulture-promo > ul > li.last > a', 'http://www.vulture.com/recommends/'))
    	
    	network_links = (('section.network-promo > div.content > div.also-wrap > div.item h6 > a.nym-head','http://nymag.com'),
    		)
    	
    	nymag_links = (('section.vulture-promo > ul:nth-child(1) > li > a', 'http://nymag.com/newyork/jobs/'),
    		('section.vulture-promo > ul:nth-child(2) > li > a','http://nymag.com/newyork/privacy/'),
    		('section.vulture-promo > ul:nth-child(3) > li > a','http://nymag.com/newyork/terms/'),
    		('section.vulture-promo > ul:nth-child(4) > li > a','http://nymag.com/newyork/aboutus/'),
    		('section.vulture-promo > ul:nth-child(5) > li > a','http://nymag.com/contactus/'),
    		('section.vulture-promo > ul:nth-child(6) > li > a','http://nymag.com/newyork/mediakit/'),
    		('section.vulture-promo > ul:nth-child(7) > li > a','http://nymag.com/newyork/rss/'),
    		('section.vulture-promo > ul:nth-child(8) > li > a','http://nymag.com/newsletters/#'),
    		('section.vulture-promo > ul:nth-child(9) > li > a','http://nymag.com/apps/'),
    		('section.vulture-promo > ul:nth-child(10) > li > a','http://nymag.com/sitemap/'),
    		('section.vulture-promo > ul:nth-child(11) > li.ad-choices > a','http://nymag.com/newyork/privacy/#ad-choices'),
    		('section.vulture-promo > ul:nth-child(12) > li.last > a','http://community.nymag.com/nymag'))
        
        return vulture_links, network_links, nymag_links
    
    def login_reg_links(self):
    	
    	login_link = 'a.login-lightbox'
    	register_link = 'a.register-lightbox'
    	
    	return login_link, register_link
    	
    def login_lightbox(self):
    	    
    	# Contains elements inside the lightbox after link to log in is clicked    
    	
    	lightbox = 'div#login-litebx.litebx-content[class*="login-box"]'
    	sign_in_text = 'div#login-litebx.litebx-content div.head h1'
    	existing_acct_text = 'div.frm-wrp-left h2'
    	fb_acct_text = 'div.frm-wrp-rt h2'         # fb = facebook
    	nymag_link = 'div#login-litebx.litebx-content div.lightbox-utilities ul li.first a.nymag'
    	vulture_link = 'div#login-litebx.litebx-content div.lightbox-utilities ul li a.vulture'
    	grubstreet_link = 'div#login-litebx.litebx-content div.lightbox-utilities ul li.last a.grubstreet'
    	info_hover = 'div.info-hover'
    	usr_label = 'li#membername-wrp.input-txt label'
    	usr_input_box = 'div.input-wrp input#id_login'
    	pwd_label = 'li#email_address-wrp.input-txt label'  #note, not password_addres-wrp
    	pwd_input_box = 'div.input-wrp input#id_password'
    	remember_me_box = 'input#id_remember' # remember me toggle 
    	forgot_pwd_link = 'li#member-wrp a.forgot'
    	login_button = 'input#submit1.submit'
    	register_link = 'div.form-wrp-left a.more'
    	fb_login = 'div.form-wrp-right div.fbbutton-wrp a'
    	fb_info = 'p.note'
    	tos_link = 'p.terms a'      # tos = terms of service
    	login_status = 'div#login_status.status-wrp[class*="status-wrp status-error"]'
    	close_lightbox = 'h5.closelightbox'
    	
    	return lightbox, sign_in_text, existing_acct_text, fb_acct_text, nymag_link,
    	        vulture_link, grubstreet_link, info_hover, usr_label, usr_input_box,
    	        remember_me_box, forgot_pwd_link, login_button, register_link, 
    	        forgot_pwd_link, login_button, register_link, fb_login, fb_info, 
    	        tos_link, login_status, close_lightbox
    	        
    def register_lightbox(self):
    	    
    	# Contains elements inside the lightbox after link to register is clicked
    	
    	lightbox = 'div#login-litebx.litebx-content[class*="reg-box"]'
        create_acct_text = 'div#registration-litebx.litebx-content div.head h1'
        fb_login_text = 'div.fbbutton-wrp span.fb-txt'        #fb = facebook
        fb_login_btn = 'span.fbbutton-wrp > a'
        nymag_link = 'div#login-litebx.litebx-content div.lightbox-utilities ul li.first a.nymag'
    	vulture_link = 'div#login-litebx.litebx-content div.lightbox-utilities ul li a.vulture'
    	grubstreet_link = 'div#login-litebx.litebx-content div.lightbox-utilities ul li.last a.grubstreet'
    	usr_label = 'form#reg-login-form > ul > li#membername-wrp.input-txt'
    	usr_input = 'input#id_membername'
    	email_label = 'form#reg-login-form > ul > li#email_address-wrp.input-txt'
    	email_input = 'input#id_email_address'
    	em_label = 'form#reg-login-form > ul > li#nymemployee-wrp-wrp.input-txt'   # em = employee
    	em_first_name_label = 'form#reg-login-form ul li#nymemployee-wrp-wrp ul li#nymfirst-wrp.input-txt label'
    	em_first_name_input = 'li#nymfirst-wrp.input-txt div.input-wrp input#id_first_name'
    	em_last_name_label = 'form#reg-login-form ul li#nymemployee-wrp-wrp ul li#nymlast-wrp.input-txt label'
    	em_last_name_input = 'li#nymlast-wrp.input-txt div.input-wrp input#id_last_name'
    	pwd_label = 'form#reg-login-form > ul > li#membername-wrp.input-txt'
    	pwd_input = 'input#id_password'
    	confirm_pwd_label = 'form#reg-login-form > ul > li#confirm_password-wrp.input-txt'
    	confirm_pwd_input = 'input#id_confirm_password'
    	zip_label = 'form#reg-login-form > ul > li#zip-wrp.input-txt'
    	zip_input = 'input#id_zip'
    	gender_label = 'form#reg-login-form > ul > li#gender-wrp.input-radio > label'
    	m_label = 'ul li#gender-wrp.input-radio div.input-wrp ul li:nth-child(1) > label'   # m = male
    	f_label = 'ul li#gender-wrp.input-radio div.input-wrp ul li:nth-child(2) > label'   # f = female
    	m_button = 'input#id_gender_0'
    	f_button = 'input#id_gender_1'
    	captcha_label = 'form#reg-login-form ul li#captcha-wrp.input-txt label'
    	captcha_input = 'tbody tr td div.recaptcha_input_area input#recaptcha_response_field'
    	nymag_email_toggle = 'input#id_newsletter'    # typo li id#newletter-wrp
    	nymag_email_label = 'form#reg-login-form ul li#newletter-wrp.input-checkbox label span'
    	tos_toggle = 'input#id_tos'  # tos = terms of service
    	tos_label = 'form#reg-login-form ul li#tos-wrp.input-checkbox label span'
    	tos_link = 'ul li#tos-wrp.input-checkbox label span:nth-child(1) > a'
    	privacy_link = 'ul li#tos-wrp.input-checkbox label span:nth-child(2) a'
    	register_btn = 'input#submit1.submit'
    	close_lightbox = 'h5.closelightbox'
    	
    	#  status-wrp status-ok is for OK fields.  Slice the string and add 'ok' to modify
    	usr_status = 'div#membername_status[class*="status-wrp status-error"]'
    	email_status = 'div#email_address_status[class*="status-wrp status-error"]'
    	nym_first_status = 'div#first_name_status[class*="status-wrp status-error"]'
    	nym_last_status = 'div#last_name_status[class*="status-wrp status-error"]'
    	pwd_status = 'div#password_status[class*="status-wrp status-error"]'
    	pwd_confirm_status = 'div#confirm_password_status[class*="status-wrp status-error"]'
    	zip_status = 'div#zip_code_status[class*="status-wrp status-error"]'
    	gender_status = 'div#gender_status[class*="status-wrp status-error"]'
    	captcha_status = 'div#captcha_status[class*="status-wrp status-error"]'
    	tos_status = 'div#tos_status[class*="status-wrp status-error"]'
    	
    	return lightbox, create_acct_text, fb_login_text, fb_login_btn, nymag_link,
    	        vulture_link, grubstreet_link, usr_label, usr_input, email_label, email_input,
    	        em_label, em_first_name_label, em_first_name_input, em_last_name_label,
    	        em_last_name_input, pwd_label, pwd_input, confirm_pwd_label, confirm_pwd_input,
    	        zip_label, zip_input, gender_label, m_label, f_label, m_button, f_button, 
    	        captcha_label, captcha_input, nymag_email_toggle, nymag_email_label, 
    	        tos_toggle, tos_label, tos_link, privacy_link, register_btn, close_lightbox,
    	        usr_status, email_status, nym_first_status, nym_last_status, pwd_status, 
    	        pwd_confirm_status, zip_status, gender_status, captcha_status, tos_status
    	
    def social(self):
    	    
    	facebook = 'form#u860xix2 div.pluginConnectButton div.pluginButton div button'
    	twitter = 'a#follow-button.btn span#l.label'

        return facebook, twitter
        
    def feedback_tab(self):
    	    
    	tab = 'div.gsfn-widget-tab'
    	feedback_close = 'gsfn-jqmClose'
        
        return tab


def HomePage(self):

    def __init__(self):
    	pass    
    	
    def vulture_nav(self):
    	    
    	static_links = (('li#navGlobalMovies.top a', "http://www.vulture.com/movies/"),
    		('li#navGlobalTv.top a', "http://www.vulture.com/tv/"),
                ('li#navGlobalMusic.top a', "http://www.vulture.com/music/"),
                #('li#navGlobalEtc.top a#etcBtn', 'http://www.vulture.com/wonderwall/'),
                ('li#navGlobalTv.top a', "http://www.vulture.com/tv/"),
                ('li#navGlobalTv.top a', "http://www.vulture.com/tv/"),
                ('li#navGlobalTv.top a', "http://www.vulture.com/tv/"),
                ('li#navGlobalTv.top a', "http://www.vulture.com/tv/"),
                ('li#navGlobalTv.top a', "http://www.vulture.com/tv/"),
                )
        
        mouseover_menu = 'a[class*="subNavDropdown"]'
        #mouseover_menu = 'li[class*="fashions cutSectionItem"] a.sectionLink'
        logo = 'h2#vultureLogo.brand > a'     
        
        return links, mouseover_menu, logo
    
def Movies(self):

    def __init__(self):
    	pass  


def Music(self):

    def __init__(self):
    	pass  


def TV(self):

    def __init__(self):
    	pass  


def Art(self):

    def __init__(self):
    	pass  


def Books(self):

    def __init__(self):
    	pass  


def Theater(self):

    def __init__(self):
    	pass  


def News(self):

    def __init__(self):
    	pass  


if __name__ == '__main__':

    main()
