#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


def create_new_user(first_name, last_name, username, user_password):
    '''
    create a new user
    '''
    new_user = User(first_name, last_name, username, user_password)
    return new_user


def save_user(user):
    '''
    save user
    '''
    user.save_user()


def delete_user(username):
    '''
    delete user
    '''
    User.delete_user(username)


def find_user_account(username):
    '''
    find user
    '''
    return User.find_user(username)


def check_existing_user(username):
    '''
    check if user exists
    '''
    return User.user_exist(username)


def main():
    # ask user name
    print("Hello, Whats your name?")
    name = input()
    #greeting
    print(f"Welcome to Password Locker {name} 😎. How can I help you")
    print("\n")
    while True:
        print("Use these short codes to use password locker : cc - create a new user account, lg - to login to your account, dis -display account, ex -exit the user list")
        short_code = input().lower()
        if short_code == 'cc':
            print("New User")
            print("-"*10)
            print("Enter your first name ....")
            first_name = input()
            print("Enter your last name ...")
            last_name = input()
            print("Enter your username ...")
            username = input()
            print("Enter password ...")
            user_password = input()
            save_user(create_new_user(first_name, last_name,
                      username, user_password))
            full_name = first_name.upper() + " " + last_name.upper()
            print('\n')
            print(
                f"Hello {full_name}. Account with username as '{username}' and password: '{user_password}' has been created successfully")
            print('\n')
        elif short_code == 'dc':
            pass


if __name__ == '__main__':
    main()
