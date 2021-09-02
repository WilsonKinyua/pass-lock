class User():

    user_accounts = []

    def __init__(self, first_name, last_name, username, password):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = username
        self.password = password

    # save user to list
    def save_user(self):
        """Save user to list."""
        User.user_accounts.append(self)

    def delete_user(self):
        """ Delete user from the list"""
        User.user_accounts.remove(self)

    @classmethod
    def find_by_username(cls, username):
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
