import codecs

GLOBAL_DOWNLOAD: bytes = b""
GLOBAL_RESPONSE: str = "empty"
DUMMY_IMG: str = 'BM:\x00\x00\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00Ä\x0e\x00\x00Ä\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ÿÿÿ\x00'
GLOBAL_DDG_RES = r'async="" src="/t.js?q=test&amp;kl=br-pt&amp;l=br-pt&amp;s=0&amp;dl=en&amp;ct=US&amp;bing_market=pt-BR&amp;p_ent=&amp;ex=-1&amp;dp=t0km_000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&amp;perf_id=0000000000000000&amp;parent_perf_id=0000000000000000&amp;perf_sampled=0&amp;host_region=usc&amp;dfrsp=1&amp;aps=0&amp;biaexp=b&amp;desktopadclickablecontentexp=b&amp;discussionsciexp=b&amp;litexp=b&amp;msvrtexp=b&amp;searchbarexp=b&amp;weatherexp=b&amp;you_news_verticalexp=b"></script><script type="text/javascript">var dc_enabled=1,dc_iu=false,baseLinkUrl="",baseLinkEnvName="prod",testTrafficType=0,rpl="1",fq=0,fd=1,it=0,iqa=0,iqbi=0,iqm=0,iqs=0,iqp=0,iqq=0,qw=2,dl="en",ct="US",server_detected_form_factor="desktop",iqd=0,r1hc=0,r1c=0,r2c,r3c=0,rq="test",rqd="test",rfq=0,rt="",ra="h_",rv="",rad="",rds=30,rs=0,spice_version="2000",spice_paths="{}",locale="en_US",settings_url_params={},rl="br-pt",shfl=1,shrl="us-en",rlo=0,df="",ds="",sfq="",iar="",vqd="4-000000000000000000000000000000000000000",safe_ddg=0,show_covid=0,perf_id="0000000000000000",parent_perf_id="0000000000000000",perf_sampled=0,ti,tig,y,y1,didNotLoadScripts=[],__DDG_BE_VERSION__="serp_00000000_000000_ET",__DDG_FE_CHAT_HASH__="hash";function handleScriptError(el)'
GLOBAL_DDG_WEB_RESULTS = """DDG.deep.pageLayoutSummary = "w3i1w7r1,e1";DDG.inject('DDG.Data.languages.adLanguages', {});if (DDG.pageLayout) DDG.pageLayout.load('d',[{"a":"","ae":null,"c":"","d":"","da":"","h":0,"i":"","m":0,"o":0,"p":0,"s":"bingv7aa","t":"test","u":"https://en.wikipedia.org"}]);DDG.duckbar.load(..."""
GLOBAL_DDG_HTML_RESULTS = '<div class="links_main etc"><a class="result__a" href="https://en.wikipedia.org">Test</a><a class="result__snippet">Testing</a></div>'
GLOBAL_DDG_IMAGE_RESULTS = '{"results": [{"encoding_format": "bmp", "width": 1, "height": 1, "thumbnail": "https://www.python.org/static/img/python-logo.png", "url": "https://www.python.org/", "title": "Test", "image": "https://www.python.org/static/img/python-logo.png"}]}'
GLOBAL_DDG_ERROR_WEB_RESULTS = """DDG.deep.pageLayoutSummary = "w3i1w7r1,e1";DDG.inject('DDG.Data.languages.adLanguages', {});if (DDG.pageLayout) DDG.pageLayout.load('d',[{"ae":null,"c":"","d":"","da":"","h":0,"i":"","m":0,"o":0,"p":0,"s":"bingv7aa","t":"test"}]);DDG.duckbar.load(..."""


def unescape(text: str) -> bytes:
    """Converts a string into bytes, including any escaped characters"""
    return codecs.escape_decode(text.encode('unicode_escape'))[0]

class FakeResponse:
    """Used in place of requests.Response"""
    def __init__(self, text: str, code: int = 200):
        self.text = text
        self.code = code

class FakeSession:
    """Used in place of requests.sessions.Session"""
    def __init__(self, return_vals: list = []) -> None:
        self.return_vals = return_vals

    def get(self, *_, **__) -> FakeResponse:
        return FakeResponse(self.return_vals.pop(0))

    def post(self, *_, **__) -> FakeResponse:
        return FakeResponse(self.return_vals.pop(0))

    def close(self, *_, **__):
        pass

class FakeReadableRequest:
    """Used as a return value for requests.urlopen"""
    def __init__(self, read_value: bytes):
        self.read_value = read_value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return self.read_value