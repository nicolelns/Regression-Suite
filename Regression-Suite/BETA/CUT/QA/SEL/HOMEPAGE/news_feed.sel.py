from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys
import cutSelectors


class HomePageNewsFeed(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
    
    def test_news_feed_links(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # Find the "Latest News" link and click on it
        # Assert that you land on the News page after clicking "The Latest"
        # Find the "Get More News" link and click on it
        # Assert that you land on the News page after clicking "Get More News"
        
        links = (the_latest_link, get_more_news_link)
        
        for each in links:
            driver.find_element_by_css_selector(each).click()
            self.assertEqual(driver.current_url, self.base_url + "news/")
            time.sleep(1)
            driver.back()
            
    def test_news_feed_entries(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # Assert that there are exactly 20 articles in the news feed
        # Assert that every article has a timestamp and headline
            
        self.assertEqual(len(driver.find_elements_by_css_selector(entry_link)), 20)
        num_of_timestamps = len(driver.find_elements_by_css_selector(entry_timestamp))
        num_of_headlines = len(driver.find_elements_by_css_selector(entry_headline))
        self.assertEqual(num_of_headlines, num_of_timestamps)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	
    # Grab selectors and assign to variables from homepageSelectors
    
    HomePage = cutSelectors.HomePage()
    Selectors = HomePage.news_feed()
    
    the_latest_link = Selectors[0]
    get_more_news_link = Selectors[1]
    entry_link = Selectors[2]
    entry_headline = Selectors[3]
    entry_timestamp = Selectors[4]
	
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageNewsFeed)
    unittest.TextTestRunner(verbosity=2).run(suite)
