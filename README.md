# DuckDunk

[![Unit Tests](https://github.com/Jumiranger/DuckDunk/actions/workflows/python-unit-tests.yml/badge.svg)](https://github.com/Jumiranger/DuckDunk/actions/workflows/python-unit-tests.yml)
[![PyPI Version](https://img.shields.io/pypi/v/duckdunk)](https://pypi.org/project/duckdunk/)

Searching the web should be easy. DuckDunk provides dead simple DuckDuckGo 
querying for webpages and images.

## Installation

Easily install with pip through [PyPI](https://pypi.org/project/duckdunk/):
```
pip install duckdunk
```

Please refer to the README on the [PyPI](https://pypi.org/project/duckdunk/) 
page for instructions for the correct version.

## Usage

### Using site search results:
```python
import duckdunk

# Searches with DuckDuckGo and returns the result list
results = duckdunk.web_search('cat facts')
# Obtain information such as the URL, title, and snippet from each result:
print(results[0].title)
print(results[0].url)
# If you just want to downlaod the page text:
print(results[0].text())
```

### Advanced search

The old search has been replaced with `duckdunk.html_web_search` in the 
latest source files. In the latest version, the web search can be provided 
multiple parameters to customize the search, for example:

```python
latest_cat_pages = duckdunk.web_search(
    query='cats',
    time_frame='Day',
    locale='cn-zh',
    strict_search=True,
  )

```

### Using image search results:

```python
import duckdunk

# Obtain images with metadata (title, source, thumbnail, original image, etc)
results = duckdunk.image_search('cat')
# Quickly view one of the results
img = results[0].download()
img.show()
```
### Advanced image search

Image search parameters allow for very specific image queries:
```python
recent_cat_wallpapers = duckdunk.image_search(
    query='cat',
    time_range='Week',
    size='Wallpaper',
    layout='Wide',
    locale='us-en',
  )
```

## About

There are a LOT of DuckDuckGo search packages for Python. However, they 
either lack support for features, or focus on a specific use case. Moreover, 
most of these packages are very old and outdated.
The goal of this project is to bring a complete set of web search tools to Python, 
currently through the use of the DuckDuckGo search engine. Right now the aim
is to support most essential DuckDuckGo features through a human-friendly library.

The goals are:
- To be entirely free to use
- To be the most feature-complete web search tool for Python
- To encourage responsible use of any utilized search engine
- To remain simple

## Current functionality

* Integration tests for the `Main` branch on commit `6aeb670` passed at 8/28/2026 4:16 PM on a Windows 10 physical machine.

## A word of warning

Requests are purposely delayed. Sending many simultaneous requests 
to DuckDuckGo will almost always fail. Too many of these
problematic requests, and DuckDuckGo will temporarily block the client.

If you don't plan to make many requests, this delay can be removed: 
```duckdunk.web_search('cat facts', delay=0)```

If you need more speed when downloading images, the downloads for image 
previews from Bing could probably be threaded safely.
