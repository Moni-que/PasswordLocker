class User:
    '''
    class that generates new instances of users
    '''

    user_credentials = []  #an empty credential list


    def __init__(self,username,password): #creating a function
        self.username = username
        self.password = password

    # def save_user(self):
    #     '''
    #     save_user method saves user objects into user_credentials
    #     '''
    #     User.user_credentials.append(self)