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

    def delete_accounts(self):
        '''
        method that deletes an account
        '''
        User.user_credentials.remove(self)
        
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




