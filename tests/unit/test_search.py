import unittest
from unittest.mock import patch, Mock
import requests
import codecs
import duckdunk
from bs4 import BeautifulSoup
from PIL.BmpImagePlugin import BmpImageFile

GLOBAL_DOWNLOAD: bytes = b""
GLOBAL_RESPONSE: str = "empty"
GLOBAL_IMG: str = 'BM:\x00\x00\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00Ä\x0e\x00\x00Ä\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ÿÿÿ\x00'
GLOBAL_RES = r'async="" src="/t.js?q=cat%20facts&amp;kl=br-pt&amp;l=br-pt&amp;s=0&amp;dl=en&amp;ct=US&amp;bing_market=pt-BR&amp;p_ent=&amp;ex=-1&amp;dp=t0km_000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&amp;perf_id=0000000000000000&amp;parent_perf_id=0000000000000000&amp;perf_sampled=0&amp;host_region=usc&amp;dfrsp=1&amp;aps=0&amp;biaexp=b&amp;desktopadclickablecontentexp=b&amp;discussionsciexp=b&amp;litexp=b&amp;msvrtexp=b&amp;searchbarexp=b&amp;weatherexp=b&amp;you_news_verticalexp=b"></script><script type="text/javascript">var dc_enabled=1,dc_iu=false,baseLinkUrl="links.duckduckgo.com",baseLinkEnvName="prod",testTrafficType=0,rpl="1",fq=0,fd=1,it=0,iqa=0,iqbi=0,iqm=0,iqs=0,iqp=0,iqq=0,qw=2,dl="en",ct="US",server_detected_form_factor="desktop",iqd=0,r1hc=0,r1c=0,r2c,r3c=0,rq="cat%20facts",rqd="cat facts",rfq=0,rt="",ra="h_",rv="",rad="",rds=30,rs=0,spice_version="2000",spice_paths="{}",locale="en_US",settings_url_params={},rl="br-pt",shfl=1,shrl="us-en",rlo=0,df="",ds="",sfq="",iar="",vqd="4-268072618496410585329439251747045158338",safe_ddg=0,show_covid=0,perf_id="0000000000000000",parent_perf_id="0000000000000000",perf_sampled=0,ti,tig,y,y1,didNotLoadScripts=[],__DDG_BE_VERSION__="serp_20260822_035807_ET",__DDG_FE_CHAT_HASH__="hash";function handleScriptError(el)'

def unescape(text: str) -> bytes:
    """Converts a string into bytes, including any escaped characters"""
    return codecs.escape_decode(text.encode('unicode_escape'))[0]

class FakeResponse:
    def __init__(self, text: str, code: int = 200):
        self.text = text
        self.code = code

class FakeSession:
    def __init__(self, return_vals: list = []) -> None:
        self.return_vals = return_vals

    def get(self, *_, **__) -> FakeResponse:
        return FakeResponse(self.return_vals.pop(0))

    def post(self, *_, **__) -> FakeResponse:
        return FakeResponse(self.return_vals.pop(0))

class TestDownload(unittest.TestCase):
    @patch('duckdunk.download.download', Mock(return_value=b'test'))
    def test_download_soup(self):
        result = duckdunk.download_soup('')
        self.assertEqual(type(result), BeautifulSoup)

    @patch('duckdunk.download.download', Mock(return_value=unescape(GLOBAL_IMG)))
    def test_download_image(self):
        img = duckdunk.download_image('')
        self.assertEqual(type(img), BmpImageFile)
        self.assertTrue(hasattr(img, 'width'))

class TestDuckImage(unittest.TestCase):
    @patch('duckdunk.download.download', Mock(return_value=unescape(GLOBAL_IMG)))
    def test_download_from_duckimage(self):
        di = duckdunk.DuckImage('', 1, 1, '', '', '', '')
        thumbnail = di.download()
        self.assertEqual(type(thumbnail), BmpImageFile)

class TestDuckDetailedLink(unittest.TestCase):
    @patch('duckdunk.download.download', Mock(return_value=b'test'))
    def test_download_link(self):
        dd = duckdunk.DuckDetailedLink('', '', '', '', '', [], 0, '', 0, 0, 0, 0, '', '')
        text = dd.text()
        self.assertEqual(text, 'test')

class TestWebSearch(unittest.TestCase):
    @patch('duckdunk.search.Session', Mock(return_value=FakeSession([GLOBAL_RES,])))
    def test_get_session(self):
        session, text = duckdunk.get_duckduckgo_session('')
        self.assertEqual(type(session), FakeSession)
        self.assertEqual(text, GLOBAL_RES)


if __name__ == '__main__':
    unittest.main()