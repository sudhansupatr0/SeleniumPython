from selenium import webdriver
import unittest
import HtmlTestRunner

class OrangeHRMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Driver/chromedriver.exe")
        cls.driver.maximize_window()

    def test_HomepageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM",self.driver.title,"PAGE TITLE NOT MATHING")

    def test_Login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webPAGE TITLE NOT MATcHING")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("test completed")


    if __name__ == "__main__":
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\reports'))



