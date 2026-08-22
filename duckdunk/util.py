import re

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

def extract_dict(text: str, start: str, end: str, delimiter: str, sep: str = '=') -> dict[str, str]:
    """
    Converts a string within `start` and `end` to a dictionary.

    To summarize the usage, if you have the string:
        "x = {'a': 1, 'b': 2}"

    You could parse it as an actual dictionary with:
        extract_dict(my_string, "x = {", "}", ",", ":")

    And you would be given:
        {'a': '1', 'b': '2'}

    Values are always strings.
    
    Args:
        text: The string to search
        start: Where the search pattern starts. Everything before the start match is ignored.
        end: Where the search pattern ends. Everything after the end match is ignored.
        delimiter: The separator for each key-value pair, e.g. the ',' in x=1,y=2
        sep: The separator for the key and value, e.g. the '=' in x=1.

    Returns:
        Dictionary equivelant of expression result
    """
    # Search for the content within start...end
    searchkey = start + r'(.+?)' + end
    searchObj = re.search(searchkey, text)
    # The whole program would break in this case
    if not searchObj:
        raise Exception(f"Could not find content that fit the expression \"{searchkey}\". Did the page load incorrectly?")
    group = searchObj.group(1)

    # Splits the items, so that a=1,b=2 might become ('a=1', 'b=2')
    items = group.split(delimiter)
    # Cleans and converts every 'a="1"' into {'a': '1'}
    keyvalues = {}
    for item in items:
        keyvalues.update(safe_split_keyvar(item, sep))

    # The search results are returned as a cleaned dictionary
    return keyvalues