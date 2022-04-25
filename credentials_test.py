import unittest   #importing the unittest module
from credentials import Credentials  #importing Credentials class

class testCredentials(unittest.TestCase):
     '''
    Test class that defines test cases for the credentials class behaviours

    unittest.TestCase: TestCase class that helps in creating test class
    '''
     def setUp(self):
        self.new_account = Credentials('Bambi', '1234@')

     def tearDown(self):
           #code to be excecuted before each test case in order to clean up after each test case has run
         Credentials.user_createAccount = []

     def test_init(self):
         self.assertEqual(self.new_account.username, 'Bambi')
         self.assertEqual(self.new_account.password,'1234@')

     def test_save_account(self):
         self.new_account.save_account()
         self.assertEqual(len(Credentials.user_createAccount), 1)

     def test_log_in(self):
         self.new_account.save_account()
         log_in = Credentials('Bambi', '1234@')
         log_in.save_account()
         check_account = Credentials.check_account('Bambi','1234@')
         self.assertTrue(check_account)

     def test_generate_password(self):
         '''
         testing automatic password generation
         '''
         self.new_account.generate_password()
         self.assertEqual(self.new_account.password, '1234@')

if __name__ == '__main__':
    unittest.main()
