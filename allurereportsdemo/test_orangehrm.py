from selenium import webdriver
import pytest
import allure

class testhrm:
    def test_logo(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get("www.google.com")
        assert True
        self.driver.close()
