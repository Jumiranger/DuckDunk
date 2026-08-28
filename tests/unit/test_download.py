import unittest
from unittest.mock import patch, Mock
import duckdunk
from bs4 import BeautifulSoup
from PIL.BmpImagePlugin import BmpImageFile
from helper import *

class TestDownload(unittest.TestCase):
    @patch('duckdunk.download.urlopen', Mock(return_value=FakeReadableRequest(b'test')))
    def test_download(self):
        result = duckdunk.download('https://en.wikipedia.org')
        self.assertEqual(result, b'test')

    @patch('duckdunk.download.urlopen', Mock(return_value=FakeReadableRequest(b'test')))
    def test_download_with_headers(self):
        result = duckdunk.download('https://en.wikipedia.org', duckdunk.headers.DEFAULT)
        self.assertEqual(result, b'test')
        
    @patch('duckdunk.download.urlopen', Mock(return_value=FakeReadableRequest(b'test')))
    def test_download_soup(self):
        result = duckdunk.download_soup('https://en.wikipedia.org')
        self.assertEqual(type(result), BeautifulSoup)

    @patch('duckdunk.download.urlopen', Mock(return_value=FakeReadableRequest(unescape(DUMMY_IMG))))
    def test_download_image(self):
        img = duckdunk.download_image('https://www.python.org/static/img/python-logo.png')
        self.assertEqual(type(img), BmpImageFile)
        self.assertTrue(hasattr(img, 'width'))

if __name__ == '__main__':
    unittest.main()