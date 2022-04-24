from cgi import test
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


    def tearDown(self):
            
        User.user_credentials = []



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


    def test_save_many_users(self):
        self.new_user.save_user()
        test_user = User('username', 'password')
        test_user.save_user()

        self.assertEqual(len(User.user_credentials), 2)

    def test_display_accounts(self):
        '''
        test_view_accounts to test if i can view all my accounts
        '''

        self.assertEqual(User.my_accounts(), User.user_credentials)



    def test_find_accounts(self):
        self.new_user.save_user()
        test_user = User('Bambi', '1234')
        test_user.save_user()
        found_account = User.find_by_username('Bambi')
        self.assertEqual(found_account.password, test_user.password)

    def test_delete_account(self):
        '''
        test_delete_account to test if i can delete an account
        '''
        self.new_user.save_user()
        test_user = User('username', 'password')  #new user
        test_user.save_user()
        self.new_user.delete_accounts()  #deleteing a user object
        self.assertEqual(len(User.user_credentials), 1)




if __name__ == '__main__':
    unittest.main()
