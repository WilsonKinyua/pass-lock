class User():

    user_accounts = []

    def __init__(self, first_name, last_name, username, password):
        """
        Initialize the user.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save_user(self):
        """
        Save user to list.
        """
        User.user_accounts.append(self)

    def delete_user(self):
        """ 
        Delete user from the list
        """
        User.user_accounts.remove(self)

    @classmethod
    def find_user(cls, username):
        """Find user by username"""
        for user in cls.user_accounts:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls, username):
        """Check if user exists"""
        for user in cls.user_accounts:
            if user.username == username:
                return True
        return False

    @classmethod
    def check_user(cls, username, password):
        """
        Check if user exists and if password is correct
        """
        user = cls.find_user(username)
        if user and user.password == password:
            return True
        return False

    # function to login user from username and password in the user_accounts[] and if incorrect password print "Incorrect Password"
    @classmethod
    def login_user(cls, username, password):
        """
        Login user from username and password
        """
        user = cls.find_user(username)
        if user and user.password == password:
            return True
        return False
    
    # @classmethod
    # def display_users(cls):
    #     """
    #     Display all users
    #     """
    #     return cls.user_accounts


