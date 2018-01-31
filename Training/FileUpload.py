import os
import time
import unittest
from selenium import webdriver

class Upload(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_example_1(self):
        driver = self.driver
        filename = 'testFileUpload.txt'
        file = os.path.join(os.getcwd(), filename)
        driver.get('http://the-internet.herokuapp.com/upload')
        driver.find_element_by_id('file-upload').send_keys(file)
        driver.find_element_by_id('file-submit').click()
        time.sleep(10)

        uploaded_file = driver.find_element_by_id('uploaded-files').text
        print (uploaded_file)
        time.sleep(10)
        assert uploaded_file == filename, "uploaded file should be %s" % filename

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()