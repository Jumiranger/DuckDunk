from urllib.request import Request, urlopen
from w3lib.url import canonicalize_url
from bs4 import BeautifulSoup
from PIL import Image
import io
import logging

DEFAULT_HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'image/gif,image/apng,image/avif,image/webp,image/png,image/jpeg,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
"""Headers must be sent to most websites to say: "I'm not a bot."""

def download(url: str, headers=None) -> bytes:
    """
    Downloads bytes from the web.

    Args:
        url: The url to download data from.

    Returns:
        A bytes object.
    """
    url = canonicalize_url(url)
    logging.debug("Downloading " + url)

    if headers:
        req = Request(url, headers=headers)
    else:
        req = Request(url)

    with urlopen(req) as response:
        result = response.read()
    return result

def download_soup(url: str, headers=None) -> BeautifulSoup:
    """
    Downloads a BeautifulSoup object for HTML from the web.

    Args:
        url: The url to download the HTML from.

    Returns:
        A BeautifulSoup object for HTML parsing.
    """
    result = download(url, headers)
    decoded = result.decode("utf-8")
    return BeautifulSoup(decoded,  features="html.parser")

def download_image(url: str, headers=None) -> Image.Image:
    """
    Downloads an image from the web.

    Args:
        url: The url to download the image from.
    Returns:
        A Pillow Image object which can be saved.
    """
    result = download(url, headers)
    return Image.open(io.BytesIO(result))