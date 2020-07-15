import unittest

class SignUpTest(unittest.TestCase):
    def test_SignUpByGmail(self):
        print("This is Gmail SignUp")
        self.assertTrue(True)

    def test_SignUpByFacebook(self):
        print("This is facebook SignUp")
        self.assertTrue(True)

    def test_SignUpByTwitter(self):
        print("This is twitter SignUp")
        self.assertTrue(True)

        if __name__ == "__main__":
            unittest.main()