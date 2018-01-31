import sys
import time
import unittest
from selenium import webdriver

class crossBrowser(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #print (browser_type)
        if (browser_type == "Chrome"):
            self.driver = webdriver.Chrome()
        elif (browser_type == "Firefox"):
            self.driver = webdriver.Firefox()
        else:
            print("Please enter valid Browser type")
            sys.exit()

        self.driver.get("http://www.google.com")
        self.driver.set_window_size(1080,800)

    def test_checkTitle(self):
        driver = self.driver
        elem = driver.find_element_by_name("q")
        elem.send_keys("Hello WebDriver!")
        elem.submit()
        time.sleep(20)
        driver.implicitly_wait(30)
        self.assertEqual("Hello WebDriver! - Google Search", driver.title)

    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("ERROR command-line parameter must be supplied for these tests")
    browser_type = sys.argv[1]
    del sys.argv[1:]
    unittest.main()