from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys
import cutSelectors


class HomePagePartners(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = sys.argv[1]
        self.verificationErrors = []
    
    def test_homepagepartners(self):
        driver = self.driver
        driver.get(self.base_url)

        # Find the From our Partners section
        # Assert that the From our Partners text is in the section
        # Assert that there are exactly 4 partner links
        
        # Assert that there are the same number of article links and images

        driver.find_element_by_css_selector(partners_section)
        self.assertEqual(driver.find_element_by_css_selector(from_our_partners).text, "FROM OUR PARTNERS")
        
        self.assertEqual(len(driver.find_elements_by_css_selector(partner_link)), 4)

        num_of_links = len(driver.find_elements_by_css_selector(article_link))
        num_of_imgs = len(driver.find_elements_by_css_selector(article_img))
               
        self.assertEqual(num_of_links, num_of_imgs)
    
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
    Selectors = HomePage.partners_module()
    
    from_our_partners = Selectors[0]
    partners_section = Selectors[1]
    partner_link = Selectors[2]
    article_link = Selectors[3]
    article_img = Selectors[4]
    
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePagePartners)
    unittest.TextTestRunner(verbosity=2).run(suite)
