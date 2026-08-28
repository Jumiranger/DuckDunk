import unittest
from unittest.mock import patch, Mock
import duckdunk.search
from PIL.BmpImagePlugin import BmpImageFile
from helper import *

class TestDuckImage(unittest.TestCase):
    def test_duckimage_general_methods(self):
        di = duckdunk.search.DuckImage('', 1, 1, '', '', '', '')
        self.assertEqual(type(di.__repr__()), str)

    @patch('duckdunk.download.download', Mock(return_value=unescape(DUMMY_IMG)))
    def test_download_from_duckimage(self):
        di = duckdunk.search.DuckImage('', 1, 1, '', '', '', '')
        thumbnail = di.download()
        self.assertEqual(type(thumbnail), BmpImageFile)
        original = di.download(original=True)
        self.assertEqual(type(original), BmpImageFile)

class TestDuckDetailedLink(unittest.TestCase):
    @patch('duckdunk.download.download', Mock(return_value=b'test'))
    def test_download_link(self):
        dd = duckdunk.search.DuckDetailedLink('', '', '', '', '', [], 0, '', 0, 0, 0, 0, '', '')
        text = dd.text()
        self.assertEqual(text, 'test')

class TestSessionAndSearchParameters(unittest.TestCase):
    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES,])))
    def test_get_session(self):
        session, text = duckdunk.search.get_duckduckgo_session('')
        self.assertEqual(type(session), FakeSession)
        self.assertEqual(text, GLOBAL_DDG_RES)

    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES,])))
    def test_get_tjs(self):
        _, text = duckdunk.search.get_duckduckgo_session('')
        payload = duckdunk.search._get_all_tjs(text)
        # Ensures the content loaded correctly
        self.assertEqual(type(payload), dict)
        # Test for first item
        self.assertTrue('q' in payload.keys())
        self.assertEqual(payload['q'], 'test')
        # Test for middle item
        self.assertTrue('l' in payload.keys())
        self.assertEqual(payload['l'], 'br-pt')

    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES,])))
    def test_get_js_Vars(self):
        _, text = duckdunk.search.get_duckduckgo_session('')
        payload = duckdunk.search._get_all_javascript_var(text)
        # Ensures the content loaded correctly
        self.assertEqual(type(payload), dict)
        # Test for first item
        self.assertTrue('dc_enabled' in payload.keys())
        self.assertEqual(payload['dc_enabled'], '1')
        # Test for middle item
        self.assertTrue('locale' in payload.keys())
        self.assertEqual(payload['locale'], 'en_US')

    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES,])))
    def test_get_djs_params(self):
         _, text = duckdunk.search.get_duckduckgo_session('')
         payload = duckdunk.search._get_djs_params(text)
         self.assertEqual(type(payload), dict)
         self.assertTrue('q' in payload.keys())
         self.assertEqual(payload['q'], 'test')

class TestWebSearch(unittest.TestCase):
    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES, GLOBAL_DDG_WEB_RESULTS])))
    def test_web_search(self):
        results = duckdunk.search.web_search('test', delay=0)
        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1)
        self.assertEqual(type(results[0]), duckdunk.DuckDetailedLink)
        self.assertEqual(results[0].title, 'test')

    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES, GLOBAL_DDG_WEB_RESULTS])))
    def test_advanced_web_search(self):
        results = duckdunk.search.web_search(
            'test', 
            delay=0, 
            time_frame='Day',
            locale='us-en',
            strict_search=True,
            safe_search=True,
            )

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1)
        self.assertEqual(type(results[0]), duckdunk.DuckDetailedLink)
        self.assertEqual(results[0].title, 'test')

    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES, GLOBAL_DDG_WEB_RESULTS])))
    def test_advanced_web_search_alt(self):
        results = duckdunk.search.web_search(
            'test', 
            delay=0, 
            time_frame='Day',
            locale='us-en',
            bing_market='en-US',
            country='US',
            auto_configure_locale=False,
            safe_search=False,
            )

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1)
        self.assertEqual(type(results[0]), duckdunk.DuckDetailedLink)
        self.assertEqual(results[0].title, 'test')

    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES, GLOBAL_DDG_WEB_RESULTS])))
    @patch('duckdunk.download.download', Mock(side_effect=[b'test']))
    def test_download_web_search(self):
        results = duckdunk.search.web_search('test', delay=0)
        text = results[0].text()
        self.assertEqual(text, 'test')

    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES, GLOBAL_DDG_ERROR_WEB_RESULTS])))
    def test_web_search_errored_response(self):
        results = duckdunk.search.web_search('test', delay=0)
        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 0)

    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES, GLOBAL_DDG_ERROR_WEB_RESULTS])))
    def test_web_search_invalid_flags(self):
        with self.assertRaises(ValueError):
            duckdunk.search.web_search('test', time_frame='Z', delay=0)

class TestHTMLSearch(unittest.TestCase):
    @patch('duckdunk.download.download', Mock(return_value=GLOBAL_DDG_HTML_RESULTS.encode('utf-8')))
    def test_html_web_search(self):
        results = duckdunk.html_web_search('test', delay=0)
        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1)
        self.assertEqual(type(results[0]), duckdunk.DuckHTMLLink)
        self.assertEqual(results[0].title, 'Test')
        self.assertEqual(results[0].snippet, 'Testing')
        self.assertEqual(results[0].url, 'https://en.wikipedia.org')

    @patch('duckdunk.download.download', Mock(side_effect=[GLOBAL_DDG_HTML_RESULTS.encode('utf-8'), b'test']))
    def test_download_html_web_search(self):
        results = duckdunk.html_web_search('test', delay=0)
        text = results[0].text()
        self.assertEqual(text, 'test')

    @patch('duckdunk.download.download', Mock(return_value=b''))
    def test_failure_html_web_search(self):
        with self.assertRaises(duckdunk.PageRefusalException):
            duckdunk.html_web_search('test', delay=0)
        
        
class TestImageSearch(unittest.TestCase):
    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES, GLOBAL_DDG_IMAGE_RESULTS])))
    def test_image_search(self):
        results = duckdunk.image_search('test', delay=0)
        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1)
        self.assertEqual(type(results[0]), duckdunk.DuckImage)
        self.assertEqual(results[0].title, 'Test')

    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES, GLOBAL_DDG_IMAGE_RESULTS])))
    def test_advanced_image_search(self):
        results = duckdunk.image_search(
            'test',
            hide_ai_images=False,
            time_range="Day",
            locale="pt-br",
            size="Small",
            layout="Square",
            delay=0,
            )
        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1)
        self.assertEqual(type(results[0]), duckdunk.DuckImage)
        self.assertEqual(results[0].title, 'Test')

    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_DDG_RES, GLOBAL_DDG_IMAGE_RESULTS])))
    @patch('duckdunk.download.download', Mock(return_value=unescape(DUMMY_IMG)))
    def test_download_image_search(self):
        results = duckdunk.image_search('test', delay=0)
        img = results[0].download()
        self.assertEqual(type(img), BmpImageFile)

class TestSearchMiscMethods(unittest.TestCase):
    def test_flag_validation_exceptions(self):
        with self.assertRaises(ValueError):
            duckdunk.search._validate_flag_enum('test', ('null',))

if __name__ == '__main__':
    unittest.main()