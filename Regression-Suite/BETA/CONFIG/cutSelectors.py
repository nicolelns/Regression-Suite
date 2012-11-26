import re
import os
import sys

        """
        This module contains CSS selectors for elements on The Cut's site.
        The CSS selectors are only for objects that will be clicked on (or otherwise
        require a browser) when used in a Selenium Webdriver test.  Each class is for a page, 
        each page object has functions for components on each page.
        
        In order to access these selectors, import this module and create an 
        instance of this class as such:
        
        import cutSelectors
        
        HomePage = cutSelectors.HomePage()
        Selectors = HomePage.(<your-function-here>)
        ..where <your-function-here> is a call to one of the below functions 
        in this class
        
        Example: the small_pictures_module contains several CSS selectors assigned 
        to variables. 
        The function you call will return a tuple which can be accessed via 
        index in your test.

        Example use:
        
        Global = cutSelectors.Global()
        GlobalSelectors = Global.footer()
        
        or
        
        HomePage = cutSelectors.HomePage()
        HomePageSelectors = HomePage.news_feed()
    
        From there, you can assign variables to items in a tuple by index:
        
        cut_logo = GlobalSelectors[0]
        cut_links = GlobalSelectors[1]
        
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

    def cut_nav(self):
    	    
    	links = (('li[class*="fashions cutSectionItem"] a.sectionLink', "http://nymag.com/thecut/fashion/"),
                #('li[class*="runway cutSectionItem"] a.sectionLink', "http://nymag.com/thecut/runway/"),
                #('li[class*="streetstyle cutSectionItem"] a.sectionLink', "http://nymag.com/thecut/street-style/"),
                ('li[class*="fame cutSectionItem"] a.sectionLink', "http://nymag.com/thecut/celebrities/"),
                ('li[class*="beauty cutSectionItem"] a.sectionLink', "http://nymag.com/thecut/beauty/"), 
                ('li[class*="goods cutSectionItem"] a.sectionLink', "http://nymag.com/thecut/shopping/"),
                ('li[class*="lovewar cutSectionItem"] a.sectionLink', "http://nymag.com/thecut/love/"))
        
        mouseover_menu = 'a[class*="subNavDropdown"]'
        #mouseover_menu = 'li[class*="fashions cutSectionItem"] a.sectionLink'
        logo = 'a.cutLogo'
        
        return links, mouseover_menu, logo
        
    def universal_nav(self):
    	
    	"""
    	The below values are only for the production site.  The test environments
    	will have (some) urls like: http://stg.nymetro.com/daily/intelligencer/
    	
    	"""
    	
    	regex = re.compile('http:\/\/nymag.com\/nymag\/toc\/[0-9]{4}')
    	static_links = (('a.nymagLink', 'http://nymag.com/'),
    		#('li[class*="top the-magazine"] a.top', str(regex)),
    		('ul.childSites > li:nth-child(1) > a','http://nymag.com/daily/intel/'),  #UPDATE TO INTELLIGENCER
    		('ul.childSites > li:nth-child(2) > a','http://www.vulture.com/'),
    		('ul.childSites > li:nth-child(3) > a','http://nymag.com/thecut/'),
    		('ul.childSites > li:nth-child(4) > a','http://newyork.grubstreet.com/'))
    	
    	hover_links = (('ul.global li.top div#sub_nav_mag ul li:nth-child(1) > a', 'http://nymag.com/includes/tableofcontents.htm'),
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
    	search_button = 'button[id*="btn-ny-search"]'
    	
    	return search_bar, search_button

    def footer(self):
    	    
    	# Common to all pages
    	
    	cut_logo = 'div.theCutLogo'
    	cut_links = (('ul[class*="footerNav footerModuleNav"]:nth-child(1) > li.listItem > a.listItemLink', 'http://nymag.com/thecut/'),
    		('ul[class*="footerNav footerModuleNav"]:nth-child(2) > li.listItem > a.listItemLink','http://nymag.com/thecut/fashion/'),
    		('ul[class*="footerNav footerModuleNav"]:nth-child(3) > li.listItem > a.listItemLink','http://nymag.com/thecut/runway/'),
    		('ul[class*="footerNav footerModuleNav"]:nth-child(4) > li.listItem > a.listItemLink','http://nymag.com/thecut/street-style/'),
    		('ul[class*="footerNav footerModuleNav"]:nth-child(5) > li.listItem > a.listItemLink','http://nymag.com/thecut/celebrities/'),
    		('ul[class*="footerNav footerModuleNav"]:nth-child(6) > li.listItem > a.listItemLink','http://nymag.com/thecut/beauty/'),
    		('ul[class*="footerNav footerModuleNav"]:nth-child(7) > li.listItem > a.listItemLink','http://nymag.com/thecut/shopping/'),
    		('ul[class*="footerNav footerModuleNav"]:nth-child(8) > li.listItem > a.listItemLink','http://nymag.com/thecut/love/'))
    	
    	nymag_links = (('ul[class*="footerNav footerCompanyNav"]:nth-child(1) li.listItem a.listItemLink', 'http://nymag.com/newyork/jobs/'),
    		('ul[class*="footerNav footerCompanyNav"]:nth-child(2) li.listItem a.listItemLink','http://nymag.com/newyork/privacy/'),
    		('ul[class*="footerNav footerCompanyNav"]:nth-child(3) li.listItem a.listItemLink','http://nymag.com/newyork/terms/'),
    		('ul[class*="footerNav footerCompanyNav"]:nth-child(4) li.listItem a.listItemLink','http://nymag.com/newyork/aboutus/'),
    		('ul[class*="footerNav footerCompanyNav"]:nth-child(5) li.listItem a.listItemLink','http://nymag.com/contactus/'),
    		('ul[class*="footerNav footerCompanyNav"]:nth-child(6) li.listItem a.listItemLink','http://nymag.com/newyork/mediakit/'),
    		('ul[class*="footerNav footerCompanyNav"]:nth-child(7) li.listItem a.listItemLink','http://nymag.com/newyork/rss/'),
    		('ul[class*="footerNav footerCompanyNav"]:nth-child(8) li.listItem a.listItemLink','http://nymag.com/newsletters/#'),
    		('ul[class*="footerNav footerCompanyNav"]:nth-child(9) li.listItem a.listItemLink','http://nymag.com/apps/'),
    		('ul[class*="footerNav footerCompanyNav"]:nth-child(10) li.listItem a.listItemLink','http://nymag.com/sitemap/'),
    		('ul[class*="footerNav footerCompanyNav"]:nth-child(11) li.listItem a.listItemLink','http://nymag.com/newyork/privacy/#ad-choices'),
    		('ul[class*="footerNav footerCompanyNav"]:nth-child(12) li.listItem a.listItemLink','http://community.nymag.com/nymag/products/nymag_thecut'))
        
        footer_search_input = 'input.txt-ny-search-bottom'
        footer_search_btn = 'button#btn-ny-search'    # btn = button
        footer_search_nym_btn = 'ul li label input#sc-all-bottom.radio'
        footer_search_vulture_btn = 'ul li label input#sc-vulture-bottom.radio'
        
        return cut_logo, cut_links, nymag_links, footer_search_input, footer_search_btn,
                footer_search_nym_btn, footer_search_vulture_btn

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
    	    
    	tab = 'a.feedbackLink i.shortHeadline', 'http://www.surveygizmo.com/s3/1024147/Share-your-feedback-with-The-Cut'
        
        return tab
        

class HomePage():

    def __init__(self):
        pass        
        
    def small_pictures_module(self):
    	    
        small_pictures_section = 'section[class*="module clearfix featuredSlideshowWrap"]'
        small_pictures_heading = 'section[class*="module clearfix featuredSlideshowWrap"] h1'
        small_pictures_link = 'section[class*="module clearfix featuredSlideshowWrap"] > a'
        small_pictures_image = 'section[class*="module clearfix featuredSlideshowWrap"] > a > div[data-picture*="true"]'
        small_pictures_description = 'section[class*="module clearfix featuredSlideshowWrap"] > a > p.contentDescription'
        
        return small_pictures_section, small_pictures_heading, small_pictures_link, small_pictures_image, small_pictures_description
        
    def partners_module(self):
    	    
    	from_our_partners = 'article[class*="module clearfix partners"] h1'
        partners_section = 'div[class*="partnerHeadlines"]'
        partner_link = 'a.partnerLink'
        article_link = 'a > p.sectionDetailsText'
        article_img = 'article[class*="module clearfix partners"] section a img'    
        
        return from_our_partners, partners_section, partner_link, article_link, article_img
        
    def news_feed(self):
    	    
    	the_latest_link = 'h1[class*="feedTitle"] a'
        get_more_news_link = 'a[class*="readMore raquo"]'
        entry_link = 'article.entry a'
        entry_headline = 'h1.entryHeadline'
        entry_timestamp = 'time.timestamp'
        
        return the_latest_link, get_more_news_link, entry_link, entry_headline, entry_timestamp
        
    def most_popular(self):
    	    
    	most_popular_section = 'article[class*="module mostPopular"]'
        most_popular_heading = 'article[class*="module mostPopular"] h1'
        most_popular_link = 'article > ol > li > a'
        
        return most_popular_section, most_popular_heading, most_popular_link
        
    def love_war(self):
    	    
    	love_war_section = 'div[class*="parbase loveAndWar section"]'
        love_war_heading = 'article[class*="module clearfix loveWrap"] h1'
        love_war_link = 'a > header > h2'
        love_war_rubric = 'a > header > p.rubric'
        love_war_byline = 'a > p.authors'
        love_war_excerpt = 'a > p.excerpt'
        love_war_read_more = 'article[class*="module clearfix loveWrap"] a.more'
        
        return love_war_section, love_war_heading, love_war_link, love_war_rubric, love_war_byline, love_war_excerpt, love_war_read_more
    
    def lookbook(self):
    	
    	look_book_section = 'article[class*="clearfix lookbooksWrap"]'
        look_book_heading = 'article[class*="clearfix lookbooksWrap"] > header > h1'
        look_book_image = 'article[class*="clearfix lookbooksWrap"] div[data-picture*="true"]'
        look_book_link = 'article[class*="clearfix lookbooksWrap"] > div > a[href*="-look-book.html"]'
        look_book_next_arrow = 'article[class*="clearfix lookbooksWrap"] > nav > a.next'
        look_book_prev_arrow = 'article[class*="clearfix lookbooksWrap"] > nav > a.prev'
        
        return look_book_section, look_book_heading, look_book_image, look_book_link, look_book_next_arrow, look_book_prev_arrow
        
    def lede(self):
    	    
        lede_article = 'li.ledeArticle'
        lede_img = 'div.ledeImage'
        lede_link = 'a.ledeHeadlineLink'
        next_arrow = 'a[class*="ledeNext"]'
        prev_arrow = 'a[class*="ledePrev"]'	
        
        return lede_article, lede_img, lede_link, next_arrow, prev_arrow
        
    def goods(self):
    	    
    	goods_promo_section = 'section[class*="goodsWrap"]'
        goods_promo_big_img = "div.homepage_goods_promo a div img.image"
        goods_promo_thumb = "a.boxThumbnail img.image"
        goods_read_more = "p.readMore a.readMoreLink"
        
        return goods_promo_section, goods_promo_big_img, goods_promo_thumb, goods_read_more
        
    def ads(self):
    	    
    	desktop_leaderboard_ad = 'div[id*="nymTakeover"]'
    	desktop_right_col_ad = 'div[id*="homepage-300x600"]'
    	desktop_right_col_small_ad = 'div[id*="homepage-300x250"]'
    	desktop_footer_ad = 'div[id*="footer-desktop"]'
    	
    	return desktop_leaderboard_ad, desktop_right_col_ad, desktop_right_col_small_ad, desktop_footer_ad
    	
    def video_module(self):
    	    
    	video_section = 'article[class*="module clearfix videoModule"]'
    	video_url = 'a.vidBox'
    	video_headline = 'p.title'
    
        return video_section, video_url, video_headline
        
    def interview_module(self):
    	    
    	interview_section = 'div[class*="parbase interview section"]'
    	interview_title = 'h3.hed'
    	interview_silo = 'img.interviewImage'
    	interview_excerpt = 'p.contentHeader'
    	
    	return interview_section, interview_title, interview_silo, interview_excerpt
    	
    def giant_image(self):
    	    
    	giant_img_section = 'div[class*="largeImageSlideshow parbase section"]'
    	giant_img_image = 'div[class*="largeImageSlideshow parbase section"] a.moduleLink div.content div img'
    	giant_img_headline = 'div.contentDescription p.contentDescriptionMain'
    	giant_img_excerpt = 'div.contentDescription p.contentDescriptionSub'
        giant_img_pics_button = 'section a header.header h3.hed'
        
        return giant_img_section, giant_img_image, giant_img_headline, giant_img_excerpt, giant_img_pics_button
        
    def find_collection(self):
    	    
    	collection_section = 'section[class*="module collectionFinderWrap"]'
    	collection_header = 'section[class*="module collectionFinderWrap"] header.header' #FIND A COLLECTION
    	collection_season_dropdown = 'dl.select-dropdown > dt.select-header' # Select a Season.text
    	specific_season = 'dl.select-dropdown > dd.select-content > ul.option-list > li.option' # FINDALL = 8, click one to get designer dropdown
    	collection_designer_dropdown = 'dl.dropdown > dt.select-header' # = Select a Designer.text
    	specific_designer = 'dl.dropdown > dd.select-content > ul.option-list >li.option' # > 10, click random one
    	
    	return collection_section, collection_header, collection_season_dropdown, specific_season, collection_designer_dropdown, specific_designer
    	
    def giant_ad_component(self):
    	    
    	ad_section = 'div.adGalleryLarge'
    	ad_image = 'div.adGalleryLarge section.module a.moduleLink div.content div.content-img-wrap img'
    	ad_headline = 'div.adGalleryLarge section.module a.moduleLink div.contentDescription p.contentDescriptionMain'
    	
    	return ad_section, ad_image, ad_headline
    	
    def twitter(self):
    	
    	twitter_headline = 'section[class*="module clearfix twitter socialModule"] > header.header > h3.hed'
    	twitter_link = 'section[class*="module clearfix twitter socialModule"] > div.content > p.contentText > a'
    	twitter_button = 'iframe.twitter-follow-button'
    	
    	return twitter_headline, twitter_link, twitter_button
    	
    def facebook(self):
    	    
    	fb_headline = 'section[class*="module clearfix facebook socialModule"] > header.header > h3.hed'
    	fb_link = 'section[class*="module clearfix facebook socialModule"] > div.content > p.contentText > a'
    	fb_button = 'a.follow-facebook-url'
    	
    	return fb_headline, fb_link, fb_button
    	
    def instagram(self):
    	    
    	inst_headline = 'section[class*="module clearfix instagram socialModule"] > header.header > h3.hed'
    	inst_link = 'a.follow-instagram-img-url > img.follow-instagram-img'
    	inst_button = 'a.follow-instagram-url'
    	
    	return inst_headline, inst_link, inst_button
    	
    def pinterest(self):
    	    
    	pinterest_section_headline = 'section[class*="module clearfix pins"] > header.header > h3.hed'
    	pinterest_img = 'section[class*="module clearfix pins"] > div.content > section.imageFrame div.imageWrap a img.image'
    	pinterest_title = 'section[class*="module clearfix pins"] > div.content > section.imageFrame div.paragraphWrap a p.paragraph'
    	pinterest_button = 'section[class*="module clearfix pins"] footer > div.logoWrap > a > img'
    	
    	return pinterest_section_headline, pinterest_img, pinterest_title, pinterest_button
    	
    def newsletter(self):
    	    
    	newsletter_section_headline = 'section#fashion-alert-newsletter-promo[class*="module clearfix newsletter"] > header.header > h3.hed'
    	newsletter_email_input = 'input#txt-newsletters-single-email'
    	newsletter_button = 'form#sub-newsletters.form fieldset.required a.submit'
    	    
    	return newsletter_section_headline, newsletter_email_input, newsletter_button
    	
    def apps(self):
    	    
    	apps_section_headline = 'section[class*="module clearfix appsModule"] > header.header h3.hed'
    	apps_image = 'section.sectionImage a.img', 'http://itunes.apple.com/us/app/the-cut-on-the-runway/id414306304'
    	apps_button = 'section.sectionText a.submit', 'http://itunes.apple.com/us/app/the-cut-on-the-runway/id414306304'
    	
    	
    	return apps_section_headline, apps_image, apps_button
    	

class BeautySplash():
	
    def __init__(self):
    	pass

    def partner_feed(self):
    	    
    	# Common to all splash pages except goods
    	    
    	partner_feed = 'div#partner-feeds.partner-feeds'
    	partner_logo = 'div[class*="content feed"] > div.header > h5 > a.logo'
    	partner_link = 'div[class*="content feed"] > ul > li > a'
    	
    	return partner_feed, partner_logo, partner_link

    def lede(self):

        # Common to all splash pages except runway and news, goods is different

        lede_headline = 'a.ledeHeadlineLink'
        lede_image = 'div.ledeImage'
        lede_right_arrow = 'a.ledeNext'
        lede_left_arrow = 'a.ledePrev'
        lede_feature_rubric = 'a.ledeFeatureRubricLink'
        lede_byline = 'div.ledeByline > b > a'
        lede_markers = 'ol.ledeMarkers'
        
        return lede_headline, lede_imag, lede_right_arrow, lede_left_arrow,
                lede_feature_rubric, lede_byline, lede_markers

    def article(self):
    	    
    	# Common to all splash pages, goods and news are different

        newsfeed_headline = 'div.filters h3'
        article_headline = 'article#entry.feedEntry header h2 a'
        article_image = 'div.featureImage'
        article_timestamp = 'li.metaTime'
        article_feature_rubric = 'ul.meta:nth-child(2)'
        article_text = 'p.excerpt'
        load_more = 'a#loadMoreEntries.galleryOpen'
        
        return newsfeed_headline, article_headline, article_image, article_timestamp, 
                article_feature_rubric, article_text, load_more

    def ads(self):

        """
        For desktop only
        
        """
        
        # Common to all splash pages, goods is different

        lb_above_nav = ''  # lb = leaderboard
        lb_below_nav = 'div#leaderboard-desktop.nym-ad-active'
        blogvertorial = 'div.blogvertorial'
        feed_interstitial = ''
        feed_sponsored = 'div.blogvertorial h3.moduleHed'
        rc_top = 'div#secondary-flex.nym-ad-active'       # rc = right column
        rc_bottom = 'div#secondary-scroll.nym-ad-active'
        footer = 'div#footer-desktop.nym-ad-active'

        return lb_above_nav, lb_below_nav, blogvertorial, feed_interstitial, 
                feed_sponsored, rc_top, rc_bottom, footer
        

class LoveSplash():
	
    def __init__(self):
    	pass

    def partner_feed(self):
    	    
    	# Common to all splash pages except goods
    	    
    	partner_feed = 'div#partner-feeds.partner-feeds'
    	partner_logo = 'div[class*="content feed"] > div.header > h5 > a.logo'
    	partner_link = 'div[class*="content feed"] > ul > li > a'
    	
    	return partner_feed, partner_logo, partner_link

    def lede(self):

        # Common to all splash pages except runway and news, goods is different

        lede_headline = 'a.ledeHeadlineLink'
        lede_image = 'div.ledeImage'
        lede_right_arrow = 'a.ledeNext'
        lede_left_arrow = 'a.ledePrev'
        lede_feature_rubric = 'a.ledeFeatureRubricLink'
        lede_byline = 'div.ledeByline > b > a'
        lede_markers = 'ol.ledeMarkers'
        
        return lede_headline, lede_imag, lede_right_arrow, lede_left_arrow,
                lede_feature_rubric, lede_byline, lede_markers

    def article(self):
    	    
        # Common to all splash pages, goods and news are different

        newsfeed_headline = 'div.filters h3'
        article_headline = 'article#entry.feedEntry header h2 a'
        article_image = 'div.featureImage'
        article_timestamp = 'li.metaTime'
        article_feature_rubric = 'ul.meta:nth-child(2)'
        article_text = 'p.excerpt'
        load_more = 'a#loadMoreEntries.galleryOpen'
        
        return newsfeed_headline, article_headline, article_image, article_timestamp, 
                article_feature_rubric, article_text, load_more

    def ads(self):

        """
        For desktop only
        
        """
        
        # Common to all splash pages, goods is different

        lb_above_nav = ''  # lb = leaderboard
        lb_below_nav = 'div#leaderboard-desktop.nym-ad-active'
        blogvertorial = 'div.blogvertorial'
        feed_interstitial = ''
        feed_sponsored = 'div.blogvertorial h3.moduleHed'
        rc_top = 'div#secondary-flex.nym-ad-active'       # rc = right column
        rc_bottom = 'div#secondary-scroll.nym-ad-active'
        footer = 'div#footer-desktop.nym-ad-active'

        return lb_above_nav, lb_below_nav, blogvertorial, feed_interstitial, 
                feed_sponsored, rc_top, rc_bottom, footer


class GoodsSplash():
	
    def __init__(self):
    	pass

    def lede(self):

        # Common to all splash pages except runway and news, goods is different

        lede_headline = 'a.ledeHeadlineLink'
        lede_image = 'div.ledeImage'
        lede_excerpt = 'div.excerpt p'
        lede_feature_rubric = 'a.ledeFeatureRubricLink'
        lede_right_arrow = 'a.ledeNext'
        lede_left_arrow = 'a.ledePrev'
        
        return lede_headline, lede_image, lede_excerpt, lede_feature_rubric, 
                lede_right_arrow, lede_left_arrow

    def article(self):
    	    
    	# Common to all splash pages, goods and news are different

        article_headline = 'article#entry.goodsEntry header h3 a'
        article_image = 'article#entry.goodsEntry div.primaryImage a div img'
        load_more = 'a#loadMoreEntries.galleryOpen'
        
        return article_headline, article_image, load_more

    def ads(self):

        """
        For desktop only
        """
        
        # Common to all splash pages, goods is different

        lb_above_nav = ''  # lb = leaderboard
        lb_below_nav = 'div#leaderboard-desktop.nym-ad-active'
        feed_interstitial = 'div.nym-ad'
        footer = 'div#footer-desktop.nym-ad-active'

        return lb_above_nav, lb_below_nav, feed_interstitial, footer 


class FameSplash():
	
    def __init__(self):
    	pass

    def partner_feed(self):
    	    
    	# Common to all splash pages except goods
    	    
    	partner_feed = 'div#partner-feeds.partner-feeds'
    	partner_logo = 'div[class*="content feed"] > div.header > h5 > a.logo'
    	partner_link = 'div[class*="content feed"] > ul > li > a'
    	
    	return partner_feed, partner_logo, partner_link

    def lede(self):

        # Common to all splash pages except runway and news, goods is different

        lede_headline = 'a.ledeHeadlineLink'
        lede_image = 'div.ledeImage'
        lede_right_arrow = 'a.ledeNext'
        lede_left_arrow = 'a.ledePrev'
        lede_feature_rubric = 'a.ledeFeatureRubricLink'
        lede_byline = 'div.ledeByline > b > a'
        lede_markers = 'ol.ledeMarkers'
        
        return lede_headline, lede_imag, lede_right_arrow, lede_left_arrow,
                lede_feature_rubric, lede_byline, lede_markers

    def article(self):
    	    
    	# Common to all splash pages, goods and news are different

        newsfeed_headline = 'div.filters h3'
        article_headline = 'article#entry.feedEntry header h2 a'
        article_image = 'div.featureImage'
        article_timestamp = 'li.metaTime'
        article_feature_rubric = 'ul.meta:nth-child(2)'
        article_text = 'p.excerpt'
        load_more = 'a#loadMoreEntries.galleryOpen'
        
        return newsfeed_headline, article_headline, article_image, article_timestamp, 
                article_feature_rubric, article_text, load_more

    def ads(self):

        """
        For desktop only
        
        """
        
        # Common to all splash pages, goods is different

        lb_above_nav = ''  # lb = leaderboard
        lb_below_nav = 'div#leaderboard-desktop.nym-ad-active'
        blogvertorial = 'div.blogvertorial'
        feed_interstitial = ''
        feed_sponsored = 'div.blogvertorial h3.moduleHed'
        rc_top = 'div#secondary-flex.nym-ad-active'       # rc = right column
        rc_bottom = 'div#secondary-scroll.nym-ad-active'
        footer = 'div#footer-desktop.nym-ad-active'

        return lb_above_nav, lb_below_nav, blogvertorial, feed_interstitial, 
                feed_sponsored, rc_top, rc_bottom, footer

    def look_book(self):
    	    
    	# Only on fame page
    	
    	lookbook_section = 'div[class*="parbase lookbooks"]'
    	lookbook_headline = 'div[class*="parbase lookbooks"] header > h1'
    	lookbook = 'div.scrollDiv > a'
    	img = 'div.scrollDiv > a div.cropDiv'
    	title = 'div.scrollDiv > a > h2'
    	prev_arrow = 'nav > a.prev'
    	next_arrow = 'nav > a.next'
    	
    	return lookbook_section, lookbook_headline, lookbook, img, title, prev_arrow, next_arrow

    def gallery_html_module(self):
    	    
    	# Only on fame page
    	    
    	gallery_section = 'div.htmlComponent section[class*="module lookbookMag"]'
        text = 'div.htmlComponent section[class*="module lookbookMag"] a div.content p.contentText'
        image = 'div.htmlComponent section[class*="module lookbookMag"] a div.content img.image'
        quote = 'div.htmlComponent section[class*="module lookbookMag"] a footer blockquote.quote span.quoteText'

        return gallery_section, text, image, quote


class NewsSplash():
	
    def __init__(self):
    	pass

    def partner_feed(self):
    	    
    	# Common to all splash pages except goods
    	    
    	partner_feed = 'div#partner-feeds.partner-feeds'
    	partner_logo = 'div[class*="content feed"] > div.header > h5 > a.logo'
    	partner_link = 'div[class*="content feed"] > ul > li > a'
    	
    	return partner_feed, partner_logo, partner_link

    def article(self):
    	    
    	# DIFFERS FROM OTHER SPLASH PAGES

        article_headline = 'article#entry[class*="feedEntry"] header.primaryHeader h2 a'
        article_image = 'div[class*="featureImage"] a'
        article_timestamp = 'li.metaTime'
        article_text = 'div.articleText p'
        article_excerpt = 'div.excerpt'
        article_byline = 'li > cite > a'
        article_rubric = 'li[class*="featureRubric"] a'
        article_read_more = 'div.articleText span.more a'
        load_more = 'a#loadMoreEntries.galleryOpen'
        
        return article_headline, article_image, article_timestamp, article_text, 
                article_excerpt, article_byline, article_rubric, article_read_more, load_more

    def ads(self):
        
        """
        For desktop only
        
        """
        
        # Common to all splash pages, goods is different

        lb_above_nav = ''  # lb = leaderboard
        lb_below_nav = 'div#leaderboard-desktop.nym-ad-active'
        blogvertorial = 'div.blogvertorial'
        feed_interstitial = ''
        feed_sponsored = 'div.blogvertorial h3.moduleHed'
        rc_top = 'div#secondary-flex.nym-ad-active'       # rc = right column
        rc_bottom = 'div#secondary-scroll.nym-ad-active'
        footer = 'div#footer-desktop.nym-ad-active'

        return lb_above_nav, lb_below_nav, blogvertorial, feed_interstitial, 
                feed_sponsored, rc_top, rc_bottom, footer
        
        
class RunwaySplash():
	
    def __init__(self):
    	pass

    def partner_feed(self):
    	    
    	# Common to all splash pages except goods
    	    
    	partner_feed = 'div#partner-feeds.partner-feeds'
    	partner_logo = 'div[class*="content feed"] > div.header > h5 > a.logo'
    	partner_link = 'div[class*="content feed"] > ul > li > a'
    	
    	return partner_feed, partner_logo, partner_link

    def runway_panel(self):

        # Only on runway splash page

        panel_section = 'div[class*="lede splashlede parbase"]'
        window = 'div.ledeWindow'
        designer_list = 'ul.designerList'
        season_title = 'h3.seasonTitle'
        top_show_tab = 'div.titleTab a'
        az_show_tab = 'div.titleTab a secret' # Hidden until clicked
        top_designer = 'li.designer'
        top_designer_title = 'div.designerName > a'
        top_designer_silo = 'div.designSilo > div > img'
        top_designer_label = 'div.designerLabel'
        az_list = 'ol.alphaFinder'
        az_designer_title = 'a.designerLink'
        
        return panel_section, window, designer_list, season_title, top_show_tab, az_show_tab,
                top_designer, top_designer_title, top_designer_silo, top_designer_label, az_list, az_designer_title
                
    def find_collection(self):
    	    
    	collection_section = 'section[class*="module collectionFinderWrap"]'
    	collection_header = 'section[class*="module collectionFinderWrap"] header.header' #FIND A COLLECTION
    	collection_season_dropdown = 'dl.select-dropdown > dt.select-header' # Select a Season.text
    	specific_season = 'dl.select-dropdown > dd.select-content > ul.option-list > li.option' # FINDALL = 8, click one to get designer dropdown
    	collection_designer_dropdown = 'dl.dropdown > dt.select-header' # = Select a Designer.text
    	specific_designer = 'dl.dropdown > dd.select-content > ul.option-list >li.option' # > 10, click random one
    	
    	return collection_section, collection_header, collection_season_dropdown, specific_season, collection_designer_dropdown, specific_designer
                
    def bridal_html(self):
    	    
    	# Only on runway and fashion
    	
    	bridal_section = 'div[class*="htmlComponent section"]'
    	bridal_title = 'header.header > h3.hed > a' # Links to first show and list, so does image
    	bridal_image = 'img.imagePath' # Links to first show in list, so does title
    	bridal_list = 'ul.trendsList > a'
    	
    	return bridal_section, bridal_title, bridal_image, bridal_list

    def article(self):
    	    
    	# Common to all splash pages, goods and news are different

        newsfeed_headline = 'div.filters h3'
        article_headline = 'article#entry.feedEntry header h2 a'
        article_image = 'div.featureImage'
        article_timestamp = 'li.metaTime'
        article_feature_rubric = 'ul.meta:nth-child(2)'
        article_text = 'p.excerpt'
        load_more = 'a#loadMoreEntries.galleryOpen'
        
        return newsfeed_headline, article_headline, article_image, article_timestamp, 
                article_feature_rubric, article_text, load_more

    def videos(self):
    	    
    	# Only on runway
    	
    	video_section = 'div[class*=runwayVideo section'
    	video_header = 'header.header h3.hed'
    	video_img = 'ul.runwayVideoList > li.runwayVideoListItem > div.image'
    	video_title = 'ul.runwayVideoList > li.runwayVideoListItem > p.label'
    	
    	return video_section, video_header, video_img, video_title

    def ads(self):

        """
        For desktop only
        
        """
        
        # Common to all splash pages, goods is different

        lb_above_nav = ''  # lb = leaderboard
        lb_below_nav = 'div#leaderboard-desktop.nym-ad-active'
        blogvertorial = 'div.blogvertorial'
        feed_interstitial = ''
        feed_sponsored = 'div.blogvertorial h3.moduleHed'
        rc_top = 'div#secondary-flex.nym-ad-active'       # rc = right column
        rc_bottom = 'div#secondary-scroll.nym-ad-active'
        footer = 'div#footer-desktop.nym-ad-active'

        return lb_above_nav, lb_below_nav, blogvertorial, feed_interstitial, 
                feed_sponsored, rc_top, rc_bottom, footer


class StreetStyleSplash():
	
    def __init__(self):
    	pass

    # Common to all splash pages except goods
    	    
    	partner_feed = 'div#partner-feeds.partner-feeds'
    	partner_logo = 'div[class*="content feed"] > div.header > h5 > a.logo'
    	partner_link = 'div[class*="content feed"] > ul > li > a'
    	
    	return partner_feed, partner_logo, partner_link

    def lede(self):

        # Common to all splash pages except runway and news, goods is different

        lede_headline = 'a.ledeHeadlineLink'
        lede_image = 'div.ledeImage'
        lede_right_arrow = 'a.ledeNext'
        lede_left_arrow = 'a.ledePrev'
        lede_feature_rubric = 'a.ledeFeatureRubricLink'
        lede_byline = 'div.ledeByline > b > a'
        lede_markers = 'ol.ledeMarkers'
        
        return lede_headline, lede_imag, lede_right_arrow, lede_left_arrow,
                lede_feature_rubric, lede_byline, lede_markers

    def article(self):
    	    
    	# Common to all splash pages, goods and news are different

        newsfeed_headline = 'div.filters h3'
        article_headline = 'article#entry.feedEntry header h2 a'
        article_image = 'div.featureImage'
        article_timestamp = 'li.metaTime'
        article_feature_rubric = 'ul.meta:nth-child(2)'
        article_text = 'p.excerpt'
        load_more = 'a#loadMoreEntries.galleryOpen'
        
        return newsfeed_headline, article_headline, article_image, article_timestamp, 
                article_feature_rubric, article_text, load_more

    def ads(self):

        """
        For desktop only
        
        """
        
        # Common to all splash pages, goods is different

        lb_above_nav = ''  # lb = leaderboard
        lb_below_nav = 'div#leaderboard-desktop.nym-ad-active'
        blogvertorial = 'div.blogvertorial'
        feed_interstitial = ''
        feed_sponsored = 'div.blogvertorial h3.moduleHed'
        rc_top = 'div#secondary-flex.nym-ad-active'       # rc = right column
        rc_bottom = 'div#secondary-scroll.nym-ad-active'
        footer = 'div#footer-desktop.nym-ad-active'

        return lb_above_nav, lb_below_nav, blogvertorial, feed_interstitial, 
                feed_sponsored, rc_top, rc_bottom, footer


class FashionSplash():
	
    def __init__(self):
    	pass

    def partner_feed(self):
    	    
    	# Common to all splash pages except goods
    	    
    	partner_feed = 'div#partner-feeds.partner-feeds'
    	partner_logo = 'div[class*="content feed"] > div.header > h5 > a.logo'
    	partner_link = 'div[class*="content feed"] > ul > li > a'
    	
    	return partner_feed, partner_logo, partner_link

    def lede(self):

        # Common to all splash pages except runway and news, goods is different

        lede_headline = 'a.ledeHeadlineLink'
        lede_image = 'div.ledeImage'
        lede_right_arrow = 'a.ledeNext'
        lede_left_arrow = 'a.ledePrev'
        lede_feature_rubric = 'a.ledeFeatureRubricLink'
        lede_byline = 'div.ledeByline > b > a'
        lede_markers = 'ol.ledeMarkers'
        
        return lede_headline, lede_imag, lede_right_arrow, lede_left_arrow,
                lede_feature_rubric, lede_byline, lede_markers

    def article(self):
    	    
    	# Common to all splash pages, goods and news are different

        newsfeed_headline = 'div.filters h3'
        article_headline = 'article#entry.feedEntry header h2 a'
        article_image = 'div.featureImage'
        article_timestamp = 'li.metaTime'
        article_feature_rubric = 'ul.meta:nth-child(2)'
        article_text = 'p.excerpt'
        load_more = 'a#loadMoreEntries.galleryOpen'
        
        return newsfeed_headline, article_headline, article_image, article_timestamp, 
                article_feature_rubric, article_text, load_more

    def ads(self):

        """
        For desktop only
        
        """
        
        # Common to all splash pages, goods is different

        lb_above_nav = ''  # lb = leaderboard
        lb_below_nav = 'div#leaderboard-desktop.nym-ad-active'
        blogvertorial = 'div.blogvertorial'
        feed_interstitial = ''
        feed_sponsored = 'div.blogvertorial h3.moduleHed'
        rc_top = 'div#secondary-flex.nym-ad-active'       # rc = right column
        rc_bottom = 'div#secondary-scroll.nym-ad-active'
        footer = 'div#footer-desktop.nym-ad-active'

        return lb_above_nav, lb_below_nav, blogvertorial, feed_interstitial, 
                feed_sponsored, rc_top, rc_bottom, footer
        
    def bridal_html(self):
    	    
    	# Only on runway and fashion
    	
    	bridal_section = 'div[class*="htmlComponent section"]'
    	bridal_title = 'header.header > h3.hed > a' # Links to first show and list, so does image
    	bridal_image = 'img.imagePath' # Links to first show in list, so does title
    	bridal_list = 'ul.trendsList > a'
    	
    	return bridal_section, bridal_title, bridal_image, bridal_list
    	
    def find_collection(self):
    	    
    	collection_section = 'section[class*="module collectionFinderWrap"]'
    	collection_header = 'section[class*="module collectionFinderWrap"] header.header' #FIND A COLLECTION
    	collection_season_dropdown = 'dl.select-dropdown > dt.select-header' # Select a Season.text
    	specific_season = 'dl.select-dropdown > dd.select-content > ul.option-list > li.option' # FINDALL = 8, click one to get designer dropdown
    	collection_designer_dropdown = 'dl.dropdown > dt.select-header' # = Select a Designer.text
    	specific_designer = 'dl.dropdown > dd.select-content > ul.option-list >li.option' # > 10, click random one
    	
    	return collection_section, collection_header, collection_season_dropdown, specific_season, collection_designer_dropdown, specific_designer
    	
    def fashion_show_module(self):
    	    
    	# Only on fashion splash
    	
    	fashion_section = 'div[class*="lede runwayshows parbase section"]'
    	fashion_title = 'h4.bgTitle'
    	fashion_season = 'div.angledBackground'
    	fashion_silo = 'ul.runwayShowsContainer li.designer div.child a.designSilo'
    	fashion_designer = 'ul.runwayShowsContainer li.designer div.child a.designerName'
    	all_shows = 'a.moreCoverage'
    	right_arrow = 'nav.moduleNav a.next'
    	left_arrow = 'nav.moduleNav a.prev'
    	
    	return fashion_section, fashion_title, fashion_season, fashion_silo, fashion_designer, all_shows,
    	        right_arrow, left_arrow


class DesignersSplash():
	
    def __init__(self):
    	pass


class ModelsSplash():
	
    def __init__(self):
    	pass


class LabelsSplash():
    
    def __init__(self):
    	pass


class Article():
	
    def __init__(self):
    	pass

    def image(self):
    	    
    	zoom = 'a.zoomIcon'
    	enlargeable_img = 'div.image a div img.enlargeable'
    	img = ''
    	close_zoom = 'div.lightboxCloseIcon'
    	zoom_in = 'div.enlargeZoomInIcon'
    	zoom_out = 'div.enlargeZoomOutIcon'
    	
    	return zoom
    	
    def social(self):
    	    
    	facebook_button = 'button i.pluginButtonIcon'
    	twitter_button = 'div.btn-o a#b.btn span#l.label'
    	pin_it = 'li.shareItem a.PIN_1353901900378_pin_it_button'
    	tumblr = 'span.tumblr_button_abc123 a'
    	stumble_upon = 'iframe#iframe-stmblpn-widget-1'
    	email = 'a.addthis_button_email'
    	more = 'ul.shareTools li.shareItem'
    	
    	return facebook_button, twitter_button, pin_it, tumblr, stumble_upon, email, more

    def content(self):
    	    
    	timestamp = 'ul.meta li.first'
    	comments = 'span.comment-num'
    	byline = ''
    	headline = 'header.primaryHeader h1'
    	body = 'div.entryTextContent div.par div.parbase p'
    	tags = 'nav.entryTags a'
        related_stories = ''
        show_more = 'a.showMore b.downArrow'
        show_less = 'a.showMore b.upArrow'
        
        return timestamp, comments, byline, headline, body, tags, related_stories, show_more
                show_less
        
    def comments(self):
    	    
    	comment_section = 'div.comments'
    	comment_header = 'span#echo-counter.echo-ui'
    	comment_button = 'button.echo-submit-postButton'
    	comment_textbox = 'textarea.echo-submit-text'
    	lightbox = ''
    	comments = 'div.echo-stream-body'
    	
    	return comment_section, comment_header, comment_button, comment_textbox, lightbox, comments
        
    def latest_headlines(self):
    	    
    	section = 'section[class*="module latestHeadlines"]'
    	headline = 'section.module header h3 b'
    	headline_img = 'ul.topStories li span.topStoryHeadline a p'
    	headline_text = 'ul.topStories li span.topStoryThumb a img'
    	
    	return section, headline, headline_img, headline_text
    	
    def news_feed(self):
    	    
    	news_section = 'div.content h4'
    	article_headline = 'ul.newsFeed li a'
    	show_more = 'p.maxlist-more a.showMore'
    	
    	return news_section, article_headline, show_more
    	
    def article_nav(self):
    	    
    	prev_arrow = 'a.leftArticleArrow'
    	next_arrow = 'a.rightArticleArrow'
    	footer_prev = 'nav.entryPrev span.prevNextDetails'
    	footer_next = 'nav.entryNext span.prevNextDetails'
    	all_news = 'nav.newsLinkWrap a.newsLink'
    	
    	return prev_arrow, next_arrow, footer_prev, footer_next, all_news
    	
    def slideshow(self):
    	    
    	slideshow_button = 'a.galleryOpen span.slideshowZoom'
    	
    	return slideshow_button

class RunwayOpenerAndShow():
	
    def __init__(self):
    	pass

    def runway_nav(self):
    	    
    	nav = 'div.openerShowChooser'    
    	fashion_link = 'span.breadCrumbs:nth-child(1) a.breadCrumbsLink'
    	runway_link = 'span.breadCrumbs:nth-child(2) a.breadCrumbsLink'
    	season_link = 'span.breadCrumbs:nth-child(3) a.breadCrumbsLink'
    	showfinder_link = 'span.openerShowChooserLink'
    	
    	return nav, fashion_link, runway_link, season_link, showfinder_link
    	
    def prev_next_nav(self):
    	    
    	prev_arrow = 'a.leftArticleArrow'
    	next_arrow = 'a.rightArticleArrow'
    	
    	return prev_arrow, next_arrow
    	
    def showfinder(self):
    	    
    	lightbox = 'section.showFinder'
    	showfinder_header = 'div.showfinderHeader > h1.runwayHeader'
    	season_list = 'div[class*="showFinderListBox showFinderSeasonListBox"] > h3[class*="runwayHeader runwayHeaderSubdued runwayHeaderLowercase"]'
    	season = 'ol#showfinder_seasons.showFinderList li.showFinderListItem'
    	city_list = 'div[class*="showFinderListBox showFinderCityListBox"] > h3[class*="runwayHeader runwayHeaderSubdued runwayHeaderLowercase"]'
    	city = 'ol#showfinder_cities.showFinderList li.showFinderListItem'
    	designer_list = 'div[class*="showFinderListBox showFinderLabelListBox"] > h3[class*="runwayHeader runwayHeaderSubdued runwayHeaderLowercase"]'
    	designer = 'ol#showfiner_labels.showfinderList li.showFinderListItem'
    	close = 'span.x'
    	
    	return lightbox, showfinder_header, season_list, season, city_list, city,
    	        designer_list, designer, close
    	        
    def designer_opener(self):
    	    
    	designer = 'h1.contentOpenerShowTitle'
    	season = 'h2.contentOpenerSeasonYearType'
    	opener_links = 'section.contentOpenerSlideshowLinks'
    	view_collection = 'a[class*="contentOpenerSlideshowLink contentOpenerCollectionLink"]'
        video = 'a[class*="contentOpenerSlideshowLink contentOpenerVideoLink"]'
    	details = 'a[class*="contentOpenerSlideshowLink contentOpenerDetailsLink"]'
    	beauty = 'a[class*="contentOpenerSlideshowLink contentOpenerBeautyLink"]'
    	backstage = 'a[class*="contentOpenerSlideshowLink contentOpenerBackstageLink"]'
    	share_text = 'span.shareLinksTitle'
    	facebook = 'i.iconFacebook'
    	twitter = 'i.iconTwitter'
    	pinterest = 'i.iconPinterest'
    	email = 'i.iconEmail'
    	palette = 'img.palette'
    	show_hide_toggle = 'a#opener-show-notes-toggle.contentOpenerShowNotesShowMore span'
    	image = 'div.contentOpener'
    	
    	return designer, season, opener_links, view_collection, video, details, beauty, backstage, 
    	        share_text, facebook, twitter, pinterest, email, palette, show_hide_toggle, image
    	
    def most_popular_shows(self):
    	
    	popular_show_section = 'section[class*="mostPopularShows clearfix"]'
    	title = 'h1.runwayHeader'
    	prev_arrow = 'nav.prevCarousel'
    	next_arrow = 'nav.nextCarousel'
    	popular_show = 'li.mostPopularShowsListitem a.mostPopularShowLink'
    	show_silo = 'img.silo'
    	show_designer = 'h3.runwayHeader'
    	season = 'h4.runwaySeasonHeader'

        return popular_show_section, title, prev_arrow, next_arrow, popular_show,
                show_silo, show_designer, season

    def runway_show(self):
    	    
    	# Inside runway show (will work for details, beauty, etc)
    	
    	main_img = 'img[class*="ssPhotoMainView"]'
    	detail_img = 'img[class*="ssPhotoDetailView"]'
    	back_img = 'img[class*="ssPhotoBackView"]'
    	zoom = 'span.zoomIcon'
    	zoom_close = 'div.lightboxCloseIcon'
    	zoom_in = 'div.enlargeZoomInIcon'
    	zoom_out = 'div.enlargeZoomOutIcon'
    	thumbnail_link = 'a.ssViewThumbs'
    	thumbnail_imgs = 'li.ssThumbsListitem img.ssPhoto'
    	next_img = 'a.ssNext'
    	prev_img = 'a.ssPrev'
    	close = 'a.ssClose'
    	hit = 'a.hit'
    	miss = 'a.miss'
    	designer_show_link = 'h1.ssSlideshowTitle'
    	showfinder_link = 'a[class*="ssFashionSeasonLink miniCaps"]'
    	photo_credits = 'dl.ssDictionary'
    	video = 'ss.runwayVideo'
    	
    	return main_img, detail_img, back_img, zoom, zoom_close, zoom_in, zoom_out,
    	        thumbnail_link, thumbnail_imgs, next_img, prev_img, close, hit, miss, 
    	        designer_show_link, showfinder_link, photo_credits, video

    def video(self):
        
        video = 'div#lightbox.fullScreen div.videoWrap div.vidPlayer a.lightboxClose'
        
        return video
        
    def ads(self):
    	    
    	rc_ad = 'section.ssAd'  # rc = right column
        ad_text = 'span.headerText'
        close_interstitial = 'span.closeInterstitial'
        
        return rc_ad, ad_text, close_interstitial
        
        
class PremiumSlideshow(self):
	
    def __init__(self):
    	pass

    def inside_slideshow(self):
    	    
    	# Inside premium slideshow (NOT runway or lookbook)    
    	    
    	main_img = 'li[class*="ssPhotoList Item"]'  # zoomable if zoom
    	img = 'ss.Photo'
    	zoom = 'span.zoomIcon'
    	zoom_close = 'div.lightboxCloseIcon'
    	zoom_in = 'div.enlargeZoomInIcon'
    	zoom_out = 'div.enlargeZoomOutIcon'
    	slideshow_title = 'h2.ssPhotoTitle'
    	photo_caption = 'div.ssPhotoCaption'
    	thumbnail_link = 'a.ssViewThumbs'
    	thumbnail_imgs = 'li.ssThumbsListitem img.ssPhoto'
    	next_img = 'a.ssNext'
    	prev_img = 'a.ssPrev'
    	close = 'a.ssClose'
    	hit = 'a.hit'
    	miss = 'a.miss'
    	
    	return main_img, img, zoom, zoom_close, zoom_in, zoom_out, slideshow_title,
    	        photo_caption, thumbnail_link, thumbnail_imgs, next_img, prev_img,
    	        close, hit, miss
    	        
    def ads(self):
    	    
    	rc_ad = 'section.ssAd'  # rc = right column
        ad_text = 'span.headerText'
        close_interstitial = 'span.closeInterstitial'
        
        return rc_ad, ad_text, close_interstitial
    	    
class LookBookSlideshow(self):
	
    def __init__(self):
    	pass

    def inside_lookbook(self):
    	    
    	# Inside the lookbook slideshow
    	    
    	main_img = 'li[class*="ssPhotoList Item"]'  # zoomable if zoom
    	zoom = 'span.zoomIcon'
    	zoom_close = 'div.lightboxCloseIcon'
    	zoom_in = 'div.enlargeZoomInIcon'
    	zoom_out = 'div.enlargeZoomOutIcon'
    	lookbook_title = 'h1.ssSlideshowTitle > img'
    	photo_caption = 'div.ssPhotoCaption'
    	thumbnail_link = 'a.ssViewThumbs'
    	thumbnail_imgs = 'li.ssThumbsListitem img.ssPhoto'
    	next_img = 'a.ssNext'
    	prev_img = 'a.ssPrev'
    	close = 'a.ssClose'
    	hit = 'a.hit'
    	miss = 'a.miss'
        lookbook_footer = 'footer.ssPanel b.ssLogo'
        lb_footer_box = 'img.lookBookCarouselBox'     # lb = lookbook
        lb_footer_img = 'img.lookBookCarouselImage'                      
        lb_footer_headline = 'h5.lookBookCarouselTitleName'
        lb_footer_prev_arrow = 'div.lookBookArrowLeft'
        lb_footer_next_arrow = 'div.lookBookArrowRight'

    	return main_img, zoom, zoom_close, zoom_in, zoom_out, lookbook_title, photo_caption,
    	        thumbnail_link, thumbnail_imgs, next_img, prev_img, close, hit, miss, 
    	        lookbook_footer, lb_footer_box, lb_footer_img, lb_footer_headline, 
    	        lb_footer_prev_arrow, lb_footer_next_arrow

    def ads(self):
    	    
    	rc_ad = 'section.ssAd'  # rc = right column
        ad_text = 'span.headerText'
        close_interstitial = 'span.closeInterstitial'
        
        return rc_ad, ad_text, close_interstitial

class RegularSlideshow():
	
    def __init__(self):
    	pass

    def inside_slideshow(self):
    	    
    	# Inside regular editorial slideshow (white background)

        main_img = ''
        
        return main_img
        
        
if __name__ == '__main__':

    main()
        
