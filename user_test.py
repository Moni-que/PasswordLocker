import unittest   #importing the unittest module
from user import User  #importing the User class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test class
    '''


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('Bambi', '1234') # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Bambi")
        self.assertEqual(self.new_user.password,"1234")


    def test_save_user(self):
        '''
        test_save_user to test if user object is saved into the user_credentials
        '''

        self.new_user.save_user()  #saving the user
        self.assertEqual(len(User.user_credentials), 1)

if __name__ == '__main__':
    unittest.main()
