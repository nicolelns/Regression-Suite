import re
import os
import sys


class HomePage():

    def __init__(self):
        
        """
        This class contains CSS selectors for elements on The Cut's home page.
        In order to access these selectors, import this module and create an 
        instance of this class as such:
        
        import cutSelectors
        
        HomePage = cutSelectors.HomePage()
        Selectors = HomePage.(<your-function-here>)
        ..where <your-function-here> is a call to one of the below functions 
        in this class
        
        Example: the small_pictures_module contains several css selectors assigned 
        to variables. 
        The function you call will return a tuple which can be accessed via 
        index in your test.

        Example use:
        
        HomePage = cutSelectors.HomePage()
        Selectors = HomePage.search()
    
        search_bar = Selectors[0]
        search_button = Selectors[1]
        
        Add variables to this module by assigning a well-named variable inside the correct 
        function to your CSS selector as a string.  Then, append your new variable 
        to the END of the returned tuple.
        
        Example:
        
        return the_latest_link, ... nth var, <your-new-variable>
        
        IF THE SELECTOR IS INCORRECT, YOUR TEST WILL
        NOT WORK.  THERE ARE NO UNIT TESTS FOR THIS MODULE.
    
        """
        
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
        
    def cut_nav(self):
    	    
    	links = (('li[class*="fashions cutSectionItem"] a.sectionLink', "fashion/"),
                #('li[class*="runway cutSectionItem"] a.sectionLink', "runway/"),
                #('li[class*="streetstyle cutSectionItem"] a.sectionLink', "street-style/"),
                ('li[class*="fame cutSectionItem"] a.sectionLink', "celebrities/"),
                ('li[class*="beauty cutSectionItem"] a.sectionLink', "beauty/"), 
                ('li[class*="goods cutSectionItem"] a.sectionLink', "shopping/"),
                ('li[class*="lovewar cutSectionItem"] a.sectionLink', "love/"))
        
        mouseover_menu = 'a[class*="subNavDropdown"]'
        #mouseover_menu = 'li[class*="fashions cutSectionItem"] a.sectionLink'
        
        return links, mouseover_menu
        
    def universal_nav(self):
    	
    	regex = re.compile('http:\/\/nymag.com\/nymag\/toc\/[0-9]{4}')
    	static_links = (('a.nymagLink', 'http://nymag.com/'),
    		#('li[class*="top the-magazine"] a.top', str(regex)),
    		('ul.childSites > li:nth-child(1) > a','http://nymag.com/daily/intel/'),
    		('ul.childSites > li:nth-child(2) > a','http://www.vulture.com/'),
    		('ul.childSites > li:nth-child(3) > a','http://nymag.com/thecut/'),
    		('ul.childSites > li:nth-child(4) > a','http://newyork.grubstreet.com/'))
    	
    	#hover_links = (())
    	
    	mouseover_menu = 'a[id*="nav-mag"]'
    	
    	return static_links, mouseover_menu
    	
    def ads(self):
    	    
    	desktop_leaderboard_ad = 'div[id*="nymTakeover"]'
    	desktop_right_col_ad = 'div[id*="homepage-300x600"]'
    	desktop_right_col_small_ad = 'div[id*="homepage-300x250"]'
    	desktop_footer_ad = 'div[id*="footer-desktop"]'
    	
    	return desktop_leaderboard_ad, desktop_right_col_ad, desktop_right_col_small_ad, desktop_footer_ad
    	
    def search(self):
    	    
    	search_bar = 'input.text'
    	search_button = 'button[id*="btn-ny-search"]'
    	
    	return search_bar, search_button
    	
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


class BeautySplash():
	
    def __init__(self):
    	pass


class LoveSplash():
	
    def __init__(self):
    	pass


class GoodsSplash():
	
    def __init__(self):
    	pass


class FameSplash():
	
    def __init__(self):
    	pass


class NewsSplash():
	
    def __init__(self):
    	pass


class RunwaySplash():
	
    def __init__(self):
    	pass


class StreetStyleSplash():
	
    def __init__(self):
    	pass


class FashionSplash():
	
    def __init__(self):
    	pass


class DesignersSplash():
	
    def __init__(self):
    	pass


class ModelsSplash():
	
    def __init__(self):
    	pass

class ArticleSplash():
	
    def __init__(self):
    	pass


class RunwayOpenerAndShow():
	
    def __init__(self):
    	pass


class SlideshowSplash():
	
    def __init__(self):
    	pass


if __name__ == '__main__':

    main()
        
