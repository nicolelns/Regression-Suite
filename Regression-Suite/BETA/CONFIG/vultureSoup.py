import re
import os
import sys

"""
        This module contains HTML tags for elements on Vulture's home page.
        The HTML tags are only for objects that will NOT be used in a Selenium 
        Webdriver test.  Each class is for a page, each page object has functions 
        for components on each page.
        
        The HTML tags are used by BeautifulSoup inside of the test using these data.
        Most tests using this module will be for backend testing only.  Rarely will 
        a production test be using this code.
        
        In order to access these tags, import this module and create an 
        instance of this class as such:
        
        import vultureSoup
        
        HomePage = vultureSoup.HomePage()
        Soup = HomePage.(<your-function-here>)
        ..where <your-function-here> is a call to one of the below functions 
        in this class
        
        Example: the small_pictures_module contains several HTML tags assigned 
        to variables. 
        The function you call will return a tuple which can be accessed via 
        index in your test.

        Example use:
        
        Global = vultureSoup.Global()
        GlobalSoup = Global.footer()
        
        or
        
        HomePage = vultureSoup.HomePage()
        HomePageSoup = HomePage.news_feed()
    
        From there, you can assign variables to items in a tuple by index:
        
        vulture_logo = GlobalSoup[0]
        vulture_links = GlobalSoup[1]
        
        or
    
        entry_link = HomePageSoup[2]
        entry_headline = HomePageSoup[3]
        
        You can use more than one class' variables by assigning unique names to your
        class instances.  As above, you can use GlobalSoup for the Global() class, and
        HomePageSoup for the HomePage() class.  Use whatever names you like, the above
        was suggested as an organizational standard.
        
        Add variables to this module by assigning a well-named variable inside the correct 
        function to your HTML tag as a dictionary.  Then, append your new variable 
        to the END of the returned tuple.  FAILURE TO DO SO WILL CAUSE THE INDICES OF 
        THE VAIRIABLES TO BE WRONG INSIDE OF THE TESTS.
        
        Example:
        
        return the_latest_link, ... nth var, <your-new-variable>
        
        IF THE HTML TAG IS INCORRECT, YOUR TEST WILL
        NOT WORK.
    
        """
        
class Global():
	
    def __init__(self):
    	pass

    def vulture_nav(self):
    	pass


def HomePage(self):

    def __init__(self):
    	pass    
    	
    
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
