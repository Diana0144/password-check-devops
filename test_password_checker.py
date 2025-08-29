import unittest
from password_checker import is_valid_password
class TestPasswordChecker(unittest.TestCase):
    def test_valid_passwords(self):
        self.assertTrue(is_valid_password("Password1"))
        self.assertTrue(is_valid_password("Abcdefg9H"))
    def test_password_too_short(self):
        self.assertFalse(is_valid_password("P1a"))
        self.assertFalse(is_valid_password("Ab1C"))
    def test_password_missing_number(self):
        self.assertFalse(is_valid_password("Password"))
        self.assertFalse(is_valid_password("NoNumbersHere"))
    def test_password_missing_uppercase(self):
        self.assertFalse(is_valid_password("password1"))
        self.assertFalse(is_valid_password("lowercase9"))
    def test_password_missing_lowercase(self):
        self.assertFalse(is_valid_password("PASSWORD1"))
        self.assertFalse(is_valid_password("UPPERCASE9"))
    def test_empty_password(self):
        self.assertFalse(is_valid_password(""))
    def test_password_only_numbers(self):
        self.assertFalse(is_valid_password("12345678"))
    def test_password_only_letters(self):
        self.assertFalse(is_valid_password("abcdefgh"))
        self.assertFalse(is_valid_password("ABCDEFGH"))



if __name__ == "__main__":
    unittest.main()

