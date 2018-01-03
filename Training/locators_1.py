import urllib
import urlparse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

site_path = '/home/opendatalabs/personal/Training/Automation/Web/site'
site_url = urlparse.urljoin('file://', urllib.pathname2url(site_path))
driver.get(site_url + "/locators.html")

time.sleep(5)
driver.find_element_by_id("cancel_link").click() # Link
time.sleep(5)
driver.find_element_by_id("submit_btn").click()  # Button
#driver.find_element_by_id("username").send_keys("agileway") # Textfield
#driver.find_element_by_id("alert_div").text    # HTML Div element

#driver.find_element_by_name("comment").send_keys("Selenium Cool")

#driver.find_element_by_link_text("Cancel").click()
#driver.find_element_by_partial_link_text("ance").click()

#driver.find_element_by_xpath("/html/body/div/div[3]/input").click()

#print (driver.find_element_by_tag_name("body").text)

#driver.find_element_by_class_name("btn").click()

#driver.find_element_by_css_selector("#div2 > input[type='checkbox']").click()

time.sleep(5)

driver.quit()
