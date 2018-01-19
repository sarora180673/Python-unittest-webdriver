from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.google.com")
driver.implicitly_wait(30)
elem = driver.find_element_by_name("q")
elem.send_keys("Hello WebDriver!")
elem.submit()
print(driver.title)
driver.quit()