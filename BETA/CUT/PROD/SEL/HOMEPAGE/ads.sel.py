#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys
import cutSelectors

reload(sys)
sys.setdefaultencoding("utf-8")


class HomePageAds(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
        
        ########################################################################
        
    def test_desktop_ads(self):    
        driver = self.driver
        driver.get(self.base_url)
        
        ads = (desktop_leaderboard_ad, desktop_right_col_ad, desktop_right_col_small_ad, desktop_footer_ad)
        
        for ad in ads:
            driver.find_element_by_css_selector(ad).click()
            time.sleep(1)
            
            try:
                driver.back()
                
            except Exception, e:
                self.verificationErrors.append("ad opens new window/tab")
         
        ########################################################################
    	
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
        ########################################################################
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        

#########################################################################
#########################################################################

if __name__ == "__main__":
    
    HomePage = cutSelectors.HomePage()
    Selectors = HomePage.ads()
    
    desktop_leaderboard_ad = Selectors[0]
    desktop_right_col_ad = Selectors[1]
    desktop_right_col_small_ad = Selectors[2]
    desktop_footer_ad = Selectors[3]
    
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageAds)
    unittest.TextTestRunner(verbosity=2).run(suite)
