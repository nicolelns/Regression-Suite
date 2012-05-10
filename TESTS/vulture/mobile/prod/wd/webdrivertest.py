import unittest
from selenium import webdriver


class Clickables(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://www.ubuntu.com/')
        
    def test_a(self):
        
        self.assertIn('Ubuntu', self.browser.title)
	print "Hello, WebDriver!"
        
    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
