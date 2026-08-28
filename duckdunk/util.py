import re
import json

def remove_quotes(text: str) -> str:
    """Removes quotes from a string."""
    if len(text) > 1:
        if text[0] == '"' and text[-1] == '"':
            text = text[1:-1]
    return text

def safe_split_keyvar(text: str, sep: str = '='):
    split = text.split(sep)
    key, value = '', ''
    if len(split) > 0:
        key = remove_quotes(str(split[0]))
        if len(split) == 2:
            value = remove_quotes(str(split[1]))
    return {key: value}

def search_between_strict(text: str, start: str, end: str) -> re.Match[str]:
    """Obtains a substring within a regular expression. Raises an exception on failure."""
    exp = start + r'(.+?)' + end
    search = re.search(exp, text)
    if not search:
        raise Exception(f"Could not find substring for expression \"{exp}\" in string of length {len(text)}. Did the page load incorrectly?")
    return search

def extract_json(text: str, start: str, end: str) -> dict:
    """Obtains a JSON object from the text that lies within start and end."""
    substring = search_between_strict(text, start, end)
    js = json.loads(substring.group(1))
    return js

def extract_dict(text: str, start: str, end: str, delimiters: list[str], sep: str = '=') -> dict[str, str]:
    """
    Converts a string within `start` and `end` to a dictionary.

    This function exists for parsing flat dictionaries which may
    or may not be valid JSON.

    To summarize the usage, if you have the string:
        "x = {'a': 1, 'b': 2}"

    You could parse it as an actual dictionary with:
        extract_dict(my_string, "x = {", "}", [","], ":")

    And you would be given:
        {'a': '1', 'b': '2'}

    Values are always strings.
    
    Args:
        text: The string to search
        start: Where the search pattern starts. Everything before the start match is ignored.
        end: Where the search pattern ends. Everything after the end match is ignored.
        delimiters: The separator for each key-value pair, e.g. the ',' in x=1,y=2
            If there are mutliple delimiters, the first separator found is used.
        sep: The separator for the key and value, e.g. the '=' in x=1.

    Returns:
        Dictionary equivelant of expression result
    """
    # Search for the content within start...end
    searchObj = search_between_strict(text, start, end)
    group = searchObj.group(1)

    # Uses the first delimiter found
    delimiter = delimiters[0]
    for d in delimiters:
        if d in group:
            delimiter = d
            break

    # Splits the items, so that a=1,b=2 might become ('a=1', 'b=2')
    items = group.split(delimiter)
    # Cleans and converts every 'a="1"' into {'a': '1'}
    keyvalues = {}
    for item in items:
        keyvalues.update(safe_split_keyvar(item, sep))

    # The search results are returned as a cleaned dictionary
    return keyvalues