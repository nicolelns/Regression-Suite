import re
import datetime
import time

""" 
This logging module writes test results to a main log file, primarily for QA's convenience
The module consists of several functions:
    spacer:	takes an int as the only argument; designates how many spacer lines to write to the file
    log:	logs the results, writes the time the test was run, the browser under test, the test type, the URL, the test results and any other exceptions to a file
    save:	self explanatory - saves and closes the text file
The log file is located at /Library/Python/2.6/site-packages/selenium/Selenium/Logs/NYMAG_MASTER_LOG.txt and is APPEND ONLY!!!!!
"""


class MainLogger():

    def __init__(self, baseurl, test):

        self.BASEURL = baseurl
	self.test = test
	self.now = time.strftime("%d-%m-%Y-%H:%M:%S")
	self.file = open("../Logs/NYMAG_MASTER_LOG.txt", 'a')

	self.file.write("NY MAG QA LOG FOR " + self.now + '\n')
	self.spacer(2)

    def spacer(self, iters):

	self.iters = iters

	for z in range(0, self.iters):
	
	    self.file.write("__________________________________________________________________________" + '\n')

    def log(self, browser, func, result, docstring, exception=None):

	self.browser = browser
	self.func = func 		# The specific test being run (i.e. "Latest News", "Feed")
	self.result = result		# The test result, pass/fail
	self.docstring = docstring	# Details
	self.exception = exception	# The exception thrown, if any

	f = self.file		# Convenience

	f.write("Time: " + self.now + '\t' + "Browser: " + self.browser + '\n')
	f.write("Test: " + self.func + '\t' + '\t' + "URL: " + self.BASEURL + '\n')
	self.spacer(1)
	f.write(self.func + '\t' + self.result + '\n')
	f.write(self.docstring + '\n')

	if self.exception is not None:

	    f.write("EXCEPTION: " + str(self.exception) + '\n')

	self.spacer(1)

    def save(self):

	self.file.close()

#########################################################################
#########################################################################

if __name__ == '__main__':
    Logger("TEST", "TEST", "TEST", "TEST", exception="TEST")
	
