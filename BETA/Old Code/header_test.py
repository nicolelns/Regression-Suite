import sys
import os
import re
import urllib2
import httplib
import unittest

# get header

class Header(unittest.TestCase):

    def setUp(self):
        
        self.conn = httplib.HTTPConnection("www.vulture.com")
        self.verificationErrors = []
        
    def test_header(self):

        self.conn.request("HEAD", "http://www.vulture.com")  # Eventually, 2nd arg to conn.request will be an element in a list
        res = self.conn.getresponse()

        self.failIf(res.status == "404")
        self.failIf(res.status == "500")

    def tearDown(self):

        self.assertEqual(self.verificationErrors, [])
        self.conn.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)