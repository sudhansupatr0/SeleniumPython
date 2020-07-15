import unittest

class LoginTest(unittest.TestCase):
    def test_LoginByGmail(self):
        print("This is Gmail login")
        self.assertTrue(True)

    def test_LoginByFacebook(self):
        print("This is facebook login")
        self.assertTrue(True)

    def test_LoginByTwitter(self):
        print("This is twitter login")
        self.assertTrue(True)

        if __name__ == "__main__":
            unittest.main()