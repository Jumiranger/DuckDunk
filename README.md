# DuckDunk
Searching the web should be easy. DuckDunk provides dead simple DuckDuckGo querying for webpages and images.

## Installation

Easily install with pip through [PyPI](https://pypi.org/project/duckdunk/):
```
pip install duckdunk
```

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

### Using image search results:

```python
import duckdunk

# Obtain images with metadata (title, source, thumbnail, original image, etc)
results = duckdunk.image_search('cat')
# Quickly view one of the results
img = results[0].download()
img.show()
```

## About

There are a LOT of DuckDuckGo search packages for Python. However, they 
either lack support for features, or focus on a specific use case. Moreover, 
most of these packages are very old and outdated.
The goal of this project is to bring a complete set of web search tools to Python, 
currently through the use of the DuckDuckGo search engine. Right now the aim
is to support most essential DuckDuckGo features through a human-friendly library.

## A word of warning

Requests are purposely delayed. Sending many simultaneous requests 
to DuckDuckGo will almost always fail. Too many of these
problematic requests, and DuckDuckGo will temporarily block the client.

If you don't plan to make many requests, this delay can be removed: 
```duckdunk.web_search('cat facts', delay=0)```

The downloads for image previews from Bing could probably be threaded safely,
but for the time being they are downloaded one at a time.
