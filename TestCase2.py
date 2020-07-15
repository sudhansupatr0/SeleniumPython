import unittest
from selenium import webdriver




class SearchEnginesTest(unittest.TestCase):

    def tearDown(self):
        print("this is after statement")


    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get("https://www.google.com")
        print(self.driver.title)
        title = self.driver.title
     #   self.assertEqual("Google", title, "page title emismatch")
        self.assertTrue(title == "Ggggle")
        self.driver.close()



    @unittest.skip("reason is yet not ready")
    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get("https://www.bing.com")
        print(self.driver.title)
        self.driver.close()

        if __name__ == "__main__" :
            unittest.main()

