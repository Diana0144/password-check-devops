import unittest
from password_checker import is_valid_password


class TestPasswordChecker(unittest.TestCase):

    # White-Box-Test
    def test_all_passwords(self):
        self.assertFalse(is_valid_password("A1B2C3"))  # short
        self.assertFalse(is_valid_password("Abcdefgh"))
        self.assertFalse(is_valid_password("abcdefg2"))
        self.assertFalse(is_valid_password("ABCDEFG2"))
        self.assertTrue(is_valid_password("AbcdEfg23"))

    # Black-Box-Test
    def test_blackbox_passwords(self):
        self.assertFalse(is_valid_password("shortA1"))
        self.assertFalse(is_valid_password("JustLetters"))
        self.assertFalse(is_valid_password("nouppercase2"))
        self.assertFalse(is_valid_password("NOLOWERCASE2"))
        self.assertTrue(is_valid_password("ValidPassword23"))


if __name__ == "__main__":
    unittest.main()
