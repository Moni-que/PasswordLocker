import random #to generate random passwords
class User:
    '''
    class that generates new instances of users
    '''

    user_credentials = []  #an empty credential list


    def __init__(self,username,password): #creating a function
        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_credentials
        '''
        User.user_credentials.append(self)

    @classmethod
    def my_accounts(cls):
        '''
        method that returns the user_credentials
        '''
        return cls.user_credentials


    @classmethod
    def find_by_username(cls, username):
        '''
        Method that takes in a username and returns an account that matches that username.
        '''
        for account in cls.user_credentials:
            if account.username == username:
                return account 


    def delete_accounts(self):
        '''
        method that deletes an account
        '''
        User.user_credentials.remove(self)



class Credentials:
    '''
    class that helps user to create account 
    '''

    user_createAccount = [] #empty user account

    def __init__(self, username, password):

        '''
         __init__ method for defining properties for our objects.
        '''

        self.username = username
        self.password = password

    def save_account(self):
        '''
        save the account in the user object
        '''
        Credentials.user_createAccount.append(self) 


    def generate_password(self):
        '''
        generating a password
        '''
        password_characters = list(123456789 + '@!*&')  #characters to generate a password

        password_length = int(input('create a password'))  #password's length

        random.shuffle(password_characters) #to shuffle characters

        password = []
        for i in range(password_length):
            password.append(random.choice(password_characters))  #generating random characters from the list

            random.shuffle(password)

            print(password) #printing the password

    @classmethod
    def check_account(cls, username):
        for account in cls.user_createAccount:
            if account.username == username:
                return True
        return False 




