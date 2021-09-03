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


def check_user_password(username, password):
    '''
    funtion to check whether the user enter the correct username and password
    '''
    return User.check_user(username, password)


def create_new_credential(account_name, account_username, account_password):
    '''
    function to create a new credential
    '''
    new_credential = Credentials(
        account_name, account_username, account_password)
    return new_credential


def save_credentials(credentials):
    '''
    function to save credentials
    '''
    credentials.save_credentials()


def display_credentials():
    """
    funtion to display credentials
    """
    return Credentials.display_credentials()


def delete_credential(account_platform):
    '''
    function to delete credentials
    '''
    Credentials.delete_credentials(account_platform)


def find_credential(account_name):
    '''
    find credentials eg to delete
    '''
    return Credentials.find_by_account_platform(account_name)


def generate_password(password_length):
    """
    generate a random password for the user
    """
    return Credentials.generate_password(password_length)


def main():
    # ask user name
    print("Hello, Whats your name?")
    name = input()
    # greeting
    print(f"Welcome to Password Locker {name} 😎. How can I help you")
    print("\n")
    while True:
        print("Use these short codes to use password locker : cc - create a new user account, lg - to login to your account, dis -display account, ex -exit the user list")
        short_code = input().lower()
        if short_code == 'cc':
            print("Create New User Account")
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
            print('\n')
            print(
                f"Hello {first_name}😃. Account created successfully. Proceed to login to access your account")
            print('\n')
        elif short_code == 'lg':
            # login the user and check if the user exists
            print("Enter your username ...")
            username = input()
            print("Enter your password ...")
            user_password = input()
            if check_existing_user(username):
                if check_user_password(username, user_password):
                    print("\n")
                    print(f"Welcome back {username} 😃")
                    print("\n")
                    while True:
                        print("Select an option below to continue: \n")
                        print(
                            "1. Create a new credential \n2. View saved credentials \n3. Delete credentials\n 4. Logout")
                        print("\n")
                        log_choice = int(input())
                        if log_choice == 1:
                            print("Enter the account name you want to create")
                            account_name = input()
                            print("Enter the username of the account above")
                            account_username = input()
                            print('\n')
                            # allow user to select the option to generate a random password or enter password
                            print("Do you want to generate a random password or enter your own password?\n   Enter 1 to generate a random password or enter your own password\n   Enter 2 to enter your own password")
                            print("\n")
                            choice = int(input())
                            if choice == 1:
                                print(
                                    "How long do you want your password to be?")
                                password_length = int(input())
                                account_password = generate_password(
                                    password_length)
                                print(
                                    f"Your password is {account_password}")
                                print("\n")
                            elif choice == 2:
                                print("Enter password of the account")
                                account_password = input()
                            else:
                                print("Invalid input")

                            print("\n")
                            save_credentials(create_new_credential(
                                account_name, account_username, account_password))
                            print('\n')
                            print(
                                f"New Credential with account name '{account_name}' and password '{account_password}' has been created \n")
                        elif log_choice == 2:
                            print('\n')
                            print("Here is a list of all your credentials \n")
                            if display_credentials():
                                for platform in display_credentials():
                                    print(
                                        f"Account for {platform.account_platform} has username of {platform.user_account_username} and password is: {platform.user_account_password} \n")
                                # print("........" + display_credentials() + ".............")
                            else:
                                print("No accounts saved!!")
                        elif log_choice == 3:
                            print("Enter the account name you want to delete")
                            account_name_to_delete = input()
                            if find_credential(account_name_to_delete):
                                page_account_to_delete = account_name_to_delete
                                # delete_credential(page_account_to_delete)
                                # search for a single credential to delete
                                print(
                                    f"Credential with account name '{account_name_to_delete}' has been deleted")
                                print('\n')
                            else:
                                print("No such account!!")

            else:
                print('Your entered wrong credentials')
        elif short_code == 'ex':
            print("Goodbye 😥 ....")
            break


if __name__ == '__main__':
    main()
