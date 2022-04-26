#!/usr/bin/env python3.8
from user import User
from credentials import Credentials

#Function to create a new account
def create_account(username,password):

    new_account = Credentials(username,password)

    return new_account

    #function to save account
def save_account(account):
    account.save_account()

    #function to generate password
def generate_password(account):
    account.generate_password()

def create_credential(username,password):  #function that creates new credentials
    new_credential = User(username,password)
    return new_credential

def save_user(credential):  #function that saves credentials

    credential.save_user()

def save_multiple_users(account): #function that saves multiple credentials

    account.save_multiple_users()

def my_accounts():   #function that displays credentials
    return User.my_accounts()  

def delete_accounts(account):  #function that deletes credentials
    account.delete_accounts()


def main():
    print('Hello, welcome to PasswordLock')
    print('Choose the following short codes and key them in to get started: ')
    print('ca - to create an account')
    print('lg - to log in to your account')

    short_code = input().lower()
    if short_code == 'ca':
        print('username')
        username = input()
        print('\n')
        print('password')
        password = input()
        print('\n')
        save_account(create_account(username, password))    # create and save new account
        print('\n')
        print(f'Congratulations {username}, your account has been created successfully')
        print('\n')

    elif short_code == 'lg':
        print('\n')
        print('Choose the following short codes and key them in to get started: ')
        print('cn - to create new credentials')
        print('dc - to display credentials')
        print('dc -delete credentials')
        print('fc - to find credentials')
        my_short_code = input().lower()
        print('\n')

    if my_short_code == 'cn':
        print('New Credentials')
        print('\n')
        print('username')
        username = input()
        print('\n')
        print('password')
        password = input()
        print('\n')


        save_user(create_credential(username, password))
        print(f'Your account has been successfully created!')
        print(f'Your username is: {username}')
        print(f'Your password is: {password}')
        print('\n')

    elif my_short_code == 'dc':
        if my_accounts():
            print('Hi checkout your credentials')
            print('\n')

            for credential in my_accounts():
                print(f'{credential.username} {credential.password}')
                print('\n')

        else:
            print('Your Credentials list is empty')
            print('\n')

        print('key in the following short codes: ')
        print('cn - to create new credentials')
        print('dc - to display credentials')
        print('fc - to find credentials')
        print('ex -exit credential list')
        my_short_code = input().lower()
        print('\n')


if __name__ == '__main__':

    main()
