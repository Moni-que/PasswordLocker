import random #to generate random passwords
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
        uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lowercase_letters = uppercase_letters.lower()
        digits = '0123456789'
        symbols = '@#%^&*()":<>;.,!?/[]'

        upper,lower,nums,symbs = True, True, True,True

        password = []

        if upper:
            password += uppercase_letters
        if lower:
            password += lowercase_letters
        if nums:
            password += digits
        if symbs:
            password += symbols

        length = 10
        amount = 7

        for item in range(amount):
            password = ''.join(random.sample(password, length))  #generating random characters from the list
            print(password)

    @classmethod
    def check_account(cls, username,password):
        for account in cls.user_createAccount:
            if account.username == username and account.password == password:
                return True
        return False 
