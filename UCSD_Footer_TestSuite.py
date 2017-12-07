import unittest
import HTMLTestRunner
import os
from UCSD_Footer import FooterLinks
from UCSD_Footer2 import FooterLinks2

SUT = "https://extension.ucsd.edu"
dir = os.getcwd()
# get all tests from  and FooterLinks class
Footer_link_test = unittest.TestLoader().loadTestsFromTestCase(FooterLinks)
Footer_link_test2 = unittest.TestLoader().loadTestsFromTestCase(FooterLinks2)

# create a test suite Footer_link_test
#test_suite = unittest.TestSuite([Footer_link_test,Footer_link_test2])
test_suite = unittest.TestSuite([Footer_link_test2])

# run the suite
#unittest.TextTestRunner(verbosity=2).run(test_suite)
outfile = open(dir + "/SeleniumPythonTestSummary.html", "w")
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='UCSD Tests')
# run the suite using HTMLTestRunner
runner.run(test_suite)
