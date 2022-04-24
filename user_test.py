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

#     def test_init(self):
#         '''
#         test_init test case to test if the object is initialized properly
#         '''

#         self.assertEqual(self.new_user.username,"Bambi")
#         self.assertEqual(self.new_user.password,"1234")

# if __name__ == '__main__':
#     unittest.main()
