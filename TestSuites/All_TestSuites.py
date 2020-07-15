
import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignUpTest import SignUpTest

from Package2.TC_PaymentReturnTest import PaymentReturnsTest
from Package2.TC_PaymentTest import Paymenttest

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(Paymenttest)


SanityTestSuite = unittest.TestSuite([tc1,tc2])
#unittest.TextTestRunner().run(SanityTestSuite)

FunctionalTestSuite = unittest.TestSuite([tc3,tc4])
#unittest.TextTestRunner().run(FunctionalTestSuite)

MasterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner(verbosity=2).run(MasterTestSuite)

