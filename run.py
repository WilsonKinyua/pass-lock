#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


def create_user(fname, lname, username, password):
    '''
    create a new user
    '''
    new_user = User(fname, lname, username, password)
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
    print("Welcome to Password Locker 😎")
    print("\n")
    while True:
        print("Use these short codes : cc - create a new user account, dc - display user account, fc -find a user account, ex -exit the user list")
        short_code = input().lower()
        if short_code == 'cc':
            print("New User")
            print("-"*10)
            print("First name ....")
            fname = input()
            print("Last name ...")
            lname = input()
            print("Username ...")
            username = input()
            print("Password ...")
            password = input()
            save_user(create_user(fname, lname, username, password))
            print('\n')
            print(f"New User {fname} {lname} {username} {password} created")
            print('\n')
        elif short_code == 'dc':
            pass


if __name__ == '__main__':
    main()
