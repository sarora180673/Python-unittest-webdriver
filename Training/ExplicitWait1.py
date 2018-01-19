import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class FacebookTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.facebook.com")

    def test_EmailLogin(self):
        driver = self.driver
        loginemail = driver.find_element_by_xpath("//input[@id='email']")
        loginemail.send_keys("xxx@xxx.com")
        time.sleep(5)
        loginpassword = driver.find_element_by_xpath("//input[@id='pass']")
        loginpassword.send_keys("yyy")
        time.sleep(5)
        element = WebDriverWait(driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//label[@id='loginbutton']/input"))
        )
        element.click()
        #driver.find_element_by_xpath("//label[@id='loginbutton']/input").click()
        self.assertEqual("https://www.facebook.com/", driver.current_url)
    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()