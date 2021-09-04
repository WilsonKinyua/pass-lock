#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


def create_new_user(first_name, last_name, username, user_password):  # create a new user
    '''
    create a new user
    '''
    new_user = User(first_name, last_name, username, user_password)
    return new_user


def save_user(user):  # save user
    '''
    save user
    '''
    user.save_user()


def delete_user(username):  # delete user
    '''
    delete user
    '''
    User.delete_user(username)


def check_existing_user(username):  # check if the user exists
    '''
    check if user exists
    '''
    return User.user_exist(username)


def check_user_password(username, password):  # check if the password is correct
    '''
    funtion to check whether the user enter the correct username and password
    '''
    return User.check_user(username, password)


# create new credential
def create_new_credential(account_name, account_username, account_password):
    '''
    function to create a new credential
    '''
    new_credential = Credentials(
        account_name, account_username, account_password)
    return new_credential


def save_credentials(credentials):  # save credentials
    '''
    function to save credentials
    '''
    credentials.save_credentials()


def display_credentials():  # display credentials
    """
    funtion to display credentials
    """
    return Credentials.display_credentials()


def delete_credential(account_platform):  # delete credential
    '''
    function to delete credentials
    '''
    return Credentials.delete_credentials(account_platform)


def find_credential(account_name):  # find a credential
    '''
    find credentials eg to delete
    '''
    return Credentials.find_by_account_platform(account_name)


def generate_password(password_length):  # generate password
    """
    generate a random password for the user
    """
    return Credentials.generate_password(password_length)


def main():  # main function
    # ask user name
    print("Hello, Whats your name?")
    name = input()
    # greet the user
    print(f"Welcome to Password Locker {name} 😎. How can I help you")
    while True:
        print('*'*50)
        print("Use these short codes to use password locker:\n  cc - create a new user account,\n  lg - to login to your account,\n  da -display account,\n  ex -exit the application")
        print('*'*50)
        short_code = input().lower()
        if short_code == 'cc':
            print("Create New User Account")
            print('*'*50)
            print("Enter your first name .....")
            first_name = input()
            print("Enter your last name .....")
            last_name = input()
            print("Enter your username .....")
            username = input()
            print("Enter password .....")
            user_password = input()
            save_user(create_new_user(first_name, last_name,
                      username, user_password))
            print('*'*50)
            print(
                f"Hello {first_name}😃. Account created successfully. Proceed to login to access your account")
            print('*'*50)
        elif short_code == 'lg' or short_code == 'da':
            # login the user and check if the user exists
            print('*'*50)
            print("Enter your username ...")
            username = input()
            print("Enter your password ...")
            user_password = input()
            if check_existing_user(username):  # check if user exists
                # check if password is correct
                if check_user_password(username, user_password):
                    print("\n")
                    print(f"Welcome back {username} 😃")
                    print('*'*50)
                    while True:
                        print("Select an option below to continue: \n")
                        print(
                            "1. Create a new credential\n2. View saved credentials\n3. Delete credentials\n4. Logout")
                        print("\n")
                        log_choice = int(input())
                        if log_choice == 1:
                            print(
                                "Enter the account name you want to create eg twitter,instagram....")
                            account_name = input()
                            print("Enter the username of the account above")
                            account_username = input()
                            print('\n')
                            # allow user to select the option to generate a random password or enter password
                            print('*'*50)
                            print(
                                "Do you want to generate a random password or enter your own password?\n \n   Enter 1 to generate a random password\n   Enter 2 to enter your own password")
                            print('*'*10)
                            print("\n")
                            choice = int(input())
                            if choice == 1:  # generate a random password
                                print(
                                    "How long do you want your password to be?")
                                password_length = int(input())
                                account_password = generate_password(
                                    password_length)
                                print(
                                    f"Your password is {account_password}")
                            elif choice == 2:
                                print("Enter password of the account")
                                account_password = input()
                            else:
                                print("Invalid input")
                            # create and save credential
                            save_credentials(create_new_credential(
                                account_name, account_username, account_password))
                            print('\n')
                            print(
                                f"New Credential with account name '{account_name}' and password '{account_password}' has been created \n")
                            print('*'*10)
                        elif log_choice == 2:  # display credentials
                            print('\n')
                            print(
                                "Here is a list of all your credentials in the application")
                            print('*'*50)
                            if display_credentials():  # display credentials
                                for platform in display_credentials():
                                    print(
                                        f"{platform.account_platform} Account, username: {platform.user_account_username} and password: {platform.user_account_password} \n")
                            else:
                                print("No accounts saved!!")
                            print('*'*50)
                        elif log_choice == 3:  # delete credentials
                            print("Enter the account name you want to delete")
                            account_name_to_delete = input()
                            # delete credential
                            if find_credential(account_name_to_delete):
                                # delete_credential(account_name_to_delete)
                                print(
                                    f"Credential with account name '{account_name_to_delete}' has been deleted")
                                print('\n')
                            else:
                                print('*'*50)
                                print(
                                    f"Credential with account name '{account_name_to_delete}' do not exist")
                                print('*'*50)
                        elif log_choice == 4:  # logout
                            print("You have successfully logged out 🙂")
                            print('*'*50)
                            break
                        else:  # no account
                            print("No such account!!")

            else:
                print('Your entered wrong credentials')
        elif short_code == 'ex':  # exit
            print("Goodbye 😥 ........")
            break


# run main
if __name__ == '__main__':
    main()
