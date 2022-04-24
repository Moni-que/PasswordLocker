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


    def delete_accounts(self):
        '''
        method that deletes an account
        '''
        User.user_credentials.remove(self)