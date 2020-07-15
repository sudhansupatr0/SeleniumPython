from selenium import webdriver
import pytest


class TestHRM:
    def test_Logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        status=self.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
        if status==True:
            assert True
        else:
            assert False
        self.driver.close()


    def test_ListEmployees(self):
        pytest.skip("this test is skipped by me")

    def test_Login(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

        act_title = self.driver.title
        if act_title=="OrangeHRM":
            assert True
        else:
            assert False



