from urllib.request import Request, urlopen
from w3lib.url import canonicalize_url
from bs4 import BeautifulSoup
from PIL import Image
import io
import logging

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