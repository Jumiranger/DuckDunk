import duckdunk
from bs4 import BeautifulSoup
from PIL import Image
import time

class TestDownloads():
    def test_bytes_no_header(self):
            data = duckdunk.download('https://www.python.org/static/img/python-logo.png')
            assert type(data) == bytes

    def test_bytes_wikipedia(self):
        data = duckdunk.download('https://en.wikipedia.org/', duckdunk.headers.DEFAULT)
        assert type(data) == bytes

    def test_soup_wikipedia(self):
        data = duckdunk.download_soup('https://en.wikipedia.org/', duckdunk.headers.DEFAULT)
        assert type(data) == BeautifulSoup

    def test_image_wikimedia(self):
        url = 'https://www.python.org/static/img/python-logo.png'
        img = duckdunk.download_image(url)
        assert img != None
        assert hasattr(img, 'width')

class TestMiscDuckDuckGo():
    def test_connect_no_headers(self):
        assert type(duckdunk.download('https://duckduckgo.com/')) == bytes

    def test_connect_with_headers(self):
        data = duckdunk.download('https://duckduckgo.com/', duckdunk.headers.DEFAULT)
        assert type(data) == bytes 

    # def test_get_vqd(self):
    #     assert type(duckdunk.get_vqd('cat')) == str

class TestWebSearch():
    def test_web_search(self):
        results = duckdunk.web_search('cat facts')
        assert len(results) > 0
        assert type(results[0]) == duckdunk.DuckHTMLLink

    def test_download_search_result_site(self):
         results = duckdunk.web_search('cat facts')
         assert len(results) > 0
         data = duckdunk.download(results[0].url, duckdunk.headers.DEFAULT)
         assert type(data) == bytes

class TestImageSearch():
    def test_image_search(self):
        results = duckdunk.image_search('cat')
        assert len(results) > 0
        assert type(results[0]) == duckdunk.DuckImage

    def test_download_image_search_result(self):
        results = duckdunk.image_search('cat')
        img = results[0].download()
        assert img != None
        assert hasattr(img, 'width')

        