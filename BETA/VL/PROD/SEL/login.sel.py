from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

class Login(unittest.TestCase):
    
    """
        Set up Webdriver with Firefox
        """
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.vulture.com"
        self.verificationErrors = []
        self.usr = "nicole.smith@nymag.com"
        self.pwd = "qatest1"
    
        """
        Open vulture.com
        """
    
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        
        """
        Make sure login link is loaded and click on it
        """
        
        login_button = driver.find_element_by_css_selector("a.login-lightbox")
        login_button.click()
        
        
        """
        Wait for the lightbox to appear before continuing
        """
        
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "id_login"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        
        """
        Click the username/email address field and enter username
        """
        
        login_box = driver.find_element_by_id("id_login")        
        login_box.click()
        login_box.clear()
        login_box.send_keys(self.usr)
        
        """
        Click the username/email address field and enter password
        """
        pwd_box = driver.find_element_by_id("id_password")
        pwd_box.click()
        pwd_box.clear()
        pwd_box.send_keys(self.pwd)
        
        """
        Click the submit button to log in
        """
        
        submit_btn = driver.find_element_by_id("submit1")
        submit_btn.click()
        
        """
        Close the lightbox after successfully logging in
            
        """
        
        close_lightbox = driver.find_element_by_css_selector("h5.closelightbox")
        close_lightbox.click()
        
        """
        Hover over the username after logging in
            
        """
                
        usr_name = driver.find_element_by_css_selector("cite#user_name")
        hover = ActionChains(driver).move_to_element(usr_name)
        hover.perform()
        
        """
        Click the Log Out link
            
        """
                
        logout = driver.find_element_by_id("utility_logout")
        logout.click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #results = open(path[:-4] + '.html', 'wb')
    #runner = HTMLTestRunner.HTMLTestRunner(stream=results, title="Vulture Login/Logout", description='Test Results for Vulture Home Page Login/Logout')
    #runner.run(suite)
    
    