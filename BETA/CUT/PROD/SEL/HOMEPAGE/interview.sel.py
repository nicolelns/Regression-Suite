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


class HomePageInterview(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
        
    def test_interview_content(self):
    	driver = self.driver
    	driver.get(self.base_url)
    	
    	# Fail unless the interview section is on the page
    	self.failUnless(driver.find_element_by_css_selector(interview_section))
    	
    	# Assert that the section's title is INTERVIEW
    	self.assertEqual(driver.find_element_by_css_selector(interview_title).text, "INTERVIEW")
    	
    	
    def test_interview_function(self):
    	driver = self.driver
    	driver.get(self.base_url)
    	
    	interview = (interview_silo, interview_excerpt)
    	
    	# Click on the silo and the excerpt to verify page load
    	
        for each in interview:
            driver.find_element_by_css_selector(each).click()
    	    time.sleep(1)
    	    driver.back()
    	    
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
    Selectors = HomePage.interview_module()
    
    interview_section = Selectors[0]
    interview_title = Selectors[1]
    interview_silo = Selectors[2]
    interview_excerpt = Selectors[3]
    
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageInterview)
    unittest.TextTestRunner(verbosity=2).run(suite)
