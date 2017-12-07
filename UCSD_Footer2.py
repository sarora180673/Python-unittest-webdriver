import unittest
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class FooterLinks2(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://extension.ucsd.edu")
        self.driver.set_window_size(1080,800)

    def test_CP2(self):
        time.sleep(20)
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Courses & Programs')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        driver.implicitly_wait(30)
        time.sleep(10)
        self.assertEqual("https://extension.ucsd.edu/courses-and-programs", driver.current_url)

    def test_SiteMap2(self):
        driver = self.driver
        element = driver.find_element_by_xpath("//a[contains(text(),'Site Map')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/map", driver.current_url)
        if sys.exc_info()[0]:
            self.driver.save_screenshot("failshot.png")

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
