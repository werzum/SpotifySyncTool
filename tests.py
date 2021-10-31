import unittest
from unittest import TestCase, mock
from dotenv import load_dotenv

from playlist_management import *
from main import *
from utilities import *

class TestUtilities(TestCase):
	def test_check_valid_url(self):
		"""
		Test with a wrong and a correct URL
		"""
		wrong_url = "htttp://google.com"
		result = check_valid_url(wrong_url)
		self.assertFalse(result)
	
		wrong_url = "http://google.com"
		result = check_valid_url(wrong_url)
		self.assertTrue(result)

	@mock.patch.dict(os.environ, {"SPOTIPY_CLIENT_ID": "test", "SPOTIPY_CLIENT_SECRET": "test"})
	def test_spotify_environment_variables_present(self):
		"""
		Test with present environment variables
		"""
		self.assertTrue(spotify_environment_variables_present)

class TestPlaylistManagement(TestCase):
	def test_saving_urls_to_csv(self):
		"""
		Testing for reading an invalid and a valid CSV file to return a list
		"""
		self.assertRaises(Exception, read_playlist_urls, "wrong_path")

		returned_playlist = read_playlist_urls("playlist_urls")
		self.assertIs(type(returned_playlist), list)

if __name__ == '__main__':
    unittest.main()