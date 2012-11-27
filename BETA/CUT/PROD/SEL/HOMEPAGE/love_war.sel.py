from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys
import cutSelectors


class HomePageLove(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
    
    def test_love_war_link_heading(self):
        driver = self.driver
        driver.get(self.base_url)

        # Assert that the LOVE & WAR text is in the section
        # Find the "Read More Love&War link and click on it
        # Assert that you are on the love/ page after clicking the link

        self.assertEqual(driver.find_element_by_css_selector(love_war_heading).text, "LOVE & WAR")

        driver.find_element_by_css_selector(love_war_read_more).click()
        self.assertEqual(driver.current_url, self.base_url + 'love/')
        
    def test_love_war_articles(self):
        driver = self.driver
        driver.get(self.base_url)
        
        # Fail unless you can find the love and war section
        # Verify that there are three articles, links, feature rubrics,
        # bylines and excerpts in the section

        self.failUnless(driver.find_element_by_css_selector(love_war_section))

        num_links = len(driver.find_elements_by_css_selector(love_war_link))
        num_feature_rubrics = len(driver.find_elements_by_css_selector(love_war_rubric))
        num_bylines = len(driver.find_elements_by_css_selector(love_war_byline))
        num_excerpts = len(driver.find_elements_by_css_selector(love_war_excerpt))
            
        nums = (num_links, num_feature_rubrics, num_bylines, num_excerpts)
        
        for each in nums:  
            self.assertEqual(each, 3)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	
    HomePage = cutSelectors.HomePage()
    Selectors = HomePage.love_war()
    
    love_war_section = Selectors[0]
    love_war_heading = Selectors[1]
    love_war_link = Selectors[2]
    love_war_rubric = Selectors[3]
    love_war_byline = Selectors[4]
    love_war_excerpt = Selectors[5]
    love_war_read_more = Selectors[6]
    
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageLove)
    unittest.TextTestRunner(verbosity=2).run(suite)
