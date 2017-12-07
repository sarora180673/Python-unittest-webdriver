import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class FooterLinks(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://extension.ucsd.edu")
        self.driver.set_window_size(1080,800)

    def test_CP(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Courses & Programs')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        driver.implicitly_wait(20)
        time.sleep(25)
        self.assertEqual("https://extension.ucsd.edu/courses-and-programs", driver.current_url)

    def test_DegreeCredit(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Degree Credit')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        driver.implicitly_wait(10)
        time.sleep(25)
        self.assertEqual("https://extension.ucsd.edu/courses-and-programs/degree-credit", driver.current_url)

    def test_InternationalPrograms(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'International Programs')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(25)
        self.assertEqual("https://extension.ucsd.edu/international-programs/home", driver.current_url)

    def test_PreCollege(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Pre-College')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        driver.implicitly_wait(10)
        time.sleep(25)
        self.assertEqual("https://extension.ucsd.edu/courses-and-programs/pre-college", driver.current_url)

    def test_NE(self):
        driver = self.driver
        element = driver.find_element_by_xpath("//footer/div/div/div/ul[2]/li/a")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(25)
        self.assertEqual("https://extension.ucsd.edu/news-and-events", driver.current_url)

    def test_EventCalendar(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Event Calendar')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        driver.implicitly_wait(10)
        time.sleep(25)
        self.assertEqual("https://extension.ucsd.edu/news-and-events/Event-Calendar", driver.current_url)

    def test_ExtensionBlog(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Extension Blog')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        driver.implicitly_wait(10)
        time.sleep(15)
        self.assertEqual("https://extension.ucsd.edu/news-and-events/extension-blog", driver.current_url)


    def test_InTheNews(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'In the News')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        driver.implicitly_wait(10)
        time.sleep(25)
        self.assertEqual("https://extension.ucsd.edu/news-and-events/media-room/in-the-news", driver.current_url)

    def test_SocialMediaDirectory(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Social Media Directory')])[3]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(25)
        self.assertEqual("https://extension.ucsd.edu/news-and-events/social-media-directory", driver.current_url)

    def test_MediaRoom(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Media Room')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(30)
        self.assertEqual("https://extension.ucsd.edu/news-and-events/media-room", driver.current_url)

    def test_CR(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Community & Research')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/community-and-research", driver.current_url)

    def test_UCTV(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'UCTV & UCSD-TV')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/community-and-research/uctv-and-ucsd-tv", driver.current_url)

    def test_TeachForUs(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Teach for Us')])[3]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/community-and-research/collaborate-with-us/teach-for-us", driver.current_url)

    def test_CustomTraining(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Custom Training Programs')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/community-and-research/collaborate-with-us/custom-training-programs", driver.current_url)

    def test_CenterForResearch(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Center for Research')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(15)
        self.assertEqual("https://extension.ucsd.edu/community-and-research/center-for-research", driver.current_url)

    def test_CollaborateWithUs(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Collaborate With Us')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/community-and-research/collaborate-with-us", driver.current_url)

    def test_SR(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Student Resources')])[3]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/student-resources", driver.current_url)

    def test_RegistrationPolicies(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Registration Policies and Procedures')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(30)
        self.assertEqual("https://extension.ucsd.edu/student-resources/registration-policies-and-procedures", driver.current_url)

    def test_Veterans(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Veterans Education Benefits')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/student-resources/veterans-education-benefits", driver.current_url)

    def test_Disabilities(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Services for Students with Disabilities')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/student-resources/Services-for-Students-with-Disabilities", driver.current_url)

    def test_TuitionFees(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Tuition and Fees')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/student-resources/Tuition-and-Fees", driver.current_url)

    def test_ExtensionCalendar(self):
        driver = self.driver
        element = driver.find_element_by_xpath("//a[contains(text(),'Extension Calendar')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/student-resources/Extension-Calendar", driver.current_url)

    def test_AboutExtension(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'About Extension')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/about-extension", driver.current_url)

    def test_ContactUs(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Contact Us')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/about-extension/Contact-Us", driver.current_url)

    def test_Instructors(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Instructors')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/about-extension/instructors", driver.current_url)

    def test_Locations(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(text(),'Locations, Maps & Transportation')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/about-extension/locations-maps-and-transportation", driver.current_url)

    def test_SanDiego(self):
        driver = self.driver
        element = driver.find_element_by_xpath("(//a[contains(@href, '/about-extension/san-diego')])[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/about-extension/san-diego", driver.current_url)

    def test_PrivacyPolicy(self):
        driver = self.driver
        element = driver.find_element_by_xpath("//a[contains(text(),'Privacy Policy')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/Privacy-Policy", driver.current_url)

    def test_SiteMap(self):
        driver = self.driver
        element = driver.find_element_by_xpath("//a[contains(text(),'Site Map')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element_with_offset(element, 0, 20).click().perform()
        element.click()
        time.sleep(20)
        self.assertEqual("https://extension.ucsd.edu/map", driver.current_url)

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
