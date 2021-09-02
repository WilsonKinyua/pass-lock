import random
import string


class Credentials():

    user_credentials = []

    def __init__(self, account_name_page, user_account_password):
        """
            account_name_page: New credentials account name eg instagram account.
            user_account_password: New credentials account password.
        """
        self.account_name_page = account_name_page
        self.user_account_password = user_account_password

    def save_credentials(self):
        """
            save credentials method that saves credentials into user_credentials[]
        """
        Credentials.user_credentials.append(self)

    def delete_credentials(self):
        """
            deletes a saved credential from the user_credentials[]
        """
        Credentials.user_credentials.remove(self)

    @classmethod
    def display_credentials(cls):
        """
            returns the credentials list
        """
        return cls.user_credentials

    @classmethod
    def generate_password(cls, password_length):
        """
            generate random password for a user creating a new account
        """
        alphabet = string.ascii_letters + string.digits
        password = ''.join(random.choice(alphabet)
                           for i in range(password_length))
        return password
