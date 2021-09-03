import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
            Setup method for the test
        """
        self.new_credentials = Credentials(
            "Twitter", "developerTwitter", "myPass@1997")

    def test_init(self):
        """
            Test to check if the credentials object is created
        """
        self.assertEqual(self.new_credentials.account_platform, "Twitter")
        self.assertEqual(
            self.new_credentials.user_account_username, "developerTwitter")
        self.assertEqual(
            self.new_credentials.user_account_password, "myPass@1997")

    def test_save_credentials(self):
        """
        check whether the credentials object is saved to the user_credentials[]
        """
        self.assertEqual(len(Credentials.user_credentials), 0)
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_delete_credentials(self):
        """
        checks if a saved credential from the user_credentials[] is deleted
        """
        self.assertEqual(len(Credentials.user_credentials), 0)
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_credentials), 1)
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.user_credentials), 0)

    def test_find_credentials_by_platform(self):
        """
        test to check if we can find a credential by platform
        """
        self.found_credentials = Credentials.find_by_account_platform(
            "Twitter")


if __name__ == '__main__':
    unittest.main()
