DEFAULT = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 
    'Accept': '*/*;q=0.8', # image/gif,image/apng,image/avif,image/webp,image/png,image/jpeg,text/html,application/xhtml+xml,application/xml;q=0.9,
    # 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    }
"""Headers must be sent to most websites to say: "I'm not a bot."""

ALTERNATE = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:154.0) Gecko/20100101 Firefox/154.0', 
    'Accept': '*/*;q=0.8', # image/gif,image/apng,image/avif,image/webp,image/png,image/jpeg,text/html,application/xhtml+xml,application/xml;q=0.9,
    # 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    }

ALTERNATE2 = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'image/gif,image/apng,image/avif,image/webp,image/png,image/jpeg,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    }

DUCKDUCKGO_WEB_SEARCH = {
    'Host': 'links.duckduckgo.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 
    'Accept': '*/*;q=0.8', # image/gif,image/apng,image/avif,image/webp,image/png,image/jpeg,text/html,application/xhtml+xml,application/xml;q=0.9,
    'Accept-Language': 'en-US,en;q=0.8',
    'Accept-Encoding': 'none', # gzip, deflate, br, zstd
    'Referer': 'https://duckduckgo.com/',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Priority': 'u=5', # The actual priority usually seen is very high: 1
    'TE': 'trailers', # https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/TE
}

DUCKDUCKGO_IMAGE_SEARCH = {
    'Host': 'duckduckgo.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 
    'Accept': '*/*;q=0.8', # image/gif,image/apng,image/avif,image/webp,image/png,image/jpeg,text/html,application/xhtml+xml,application/xml;q=0.9,
    'Accept-Language': 'en-US,en;q=0.8',
    'Accept-Encoding': 'none',
    'Referer': 'https://duckduckgo.com/',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Cookie': 'experiment_homeheadline=optional',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=4',
    'TE': 'trailers', # https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/TE
}

BRAVE_CHUNK = {
    'Host': 'cdn.search.brave.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': '*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://search.brave.com/',
    'Origin': 'https://search.brave.com',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    }
"""This header is sent with every Brave search chunk"""

GOOGLE_SAME_SCRIPT = {
    'Sec-GPC': '1',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    }

GOOGLE_CROSS_SCRIPT = {
    'Sec-GPC': '1',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    }