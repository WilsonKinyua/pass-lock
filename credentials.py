import random
import string


class Credentials():

    user_credentials = []

    def __init__(self, account_platform, user_account_username, user_account_password):
        """
            account_platform: New credentials account name eg instagram account.
            user_account_password: New credentials account password.
        """
        self.account_platform = account_platform
        self.user_account_username = user_account_username
        self.user_account_password = user_account_password

    def save_credentials(self):
        """
            save credentials method that saves credentials into user_credentials[]
        """
        Credentials.user_credentials.append(self)

    def delete_credentials(self):
        """
            deletes saved credential from the user_credentials[]
        """
        Credentials.user_credentials.remove(self)

    @classmethod
    def find_by_account_platform(cls, account_platform):
        """
            Method that takes in a account_platform and returns a credentials that matches that account_platform.
        """
        for credentials in cls.user_credentials:
            if credentials.account_platform == account_platform:
                return credentials
        return False

    @classmethod
    def display_credentials(cls):
        """
            returns the credentials list(all credentials)
        """
        return cls.user_credentials

    @classmethod
    def generate_password(cls, password_length):
        """
            generate random password for a user creating a new account int the user_credentials[]
        """
        alpa = string.ascii_letters + string.digits
        password = ''.join(random.choice(alpa)
                           for i in range(password_length))
        return password
