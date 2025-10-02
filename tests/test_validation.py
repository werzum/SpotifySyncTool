import unittest

from spotifysynctool.validation import is_valid_url


class TestValidation(unittest.TestCase):
    def test_is_valid_url(self):
        self.assertFalse(is_valid_url("htttp://google.com"))
        self.assertTrue(is_valid_url("http://google.com"))


if __name__ == "__main__":
    unittest.main()
