import tempfile
import unittest
from pathlib import Path

from spotifysynctool.playlists import read_playlist_urls, save_playlist_urls


class TestPlaylists(unittest.TestCase):
    def test_read_playlist_urls_invalid_path(self):
        self.assertRaises(Exception, read_playlist_urls, "wrong_path")

    def test_read_playlist_urls_valid_path(self):
        result = read_playlist_urls("playlist_urls")
        self.assertIsInstance(result, list)

    def test_save_playlist_urls(self):
        playlist_urls = ["http://example.com"]
        with tempfile.TemporaryDirectory() as tmp_dir:
            destination = Path(tmp_dir) / "urls.csv"
            save_playlist_urls(playlist_urls, destination)
            loaded = read_playlist_urls(destination)
        self.assertEqual(playlist_urls, loaded)


if __name__ == "__main__":
    unittest.main()
