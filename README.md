# DuckDunk
Dead simple DuckDuckGo querying for webpages and images

----
## Installation

### TODO


## Usage
The module downloads as little as possible to reduce the request load. Searching web pages only takes a single line:

```
import duckdunk

results = duckdunk.search('cat facts')
print(results[0].url)
```

Searching images takes an extra step:

```
import duckdunk

results = duckdunk.image_search('cats')
img = results[0].download()
img.show()

```