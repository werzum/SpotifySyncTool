import os
import unittest
from unittest import mock

from spotifysynctool.config import spotify_environment_variables_present


class TestConfig(unittest.TestCase):
    @mock.patch.dict(os.environ, {"SPOTIPY_CLIENT_ID": "test", "SPOTIPY_CLIENT_SECRET": "test"}, clear=True)
    def test_spotify_environment_variables_present(self):
        self.assertTrue(spotify_environment_variables_present())


if __name__ == "__main__":
    unittest.main()
