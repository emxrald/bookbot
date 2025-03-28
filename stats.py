from pprint import pprint


def get_word_count(content: str) -> int:
    """Return word count in the string."""
    # split by whitespace
    return len(content.split())


def get_char_count(content: str) -> dict[str, int]:
    """Return dictionary with characters and its count found in the content."""
    char_count = {}  # output dict

    for c in content:
        c = c.lower()
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count


def sort_key(dict):
    """Function used for sorting char count list returned by 'sort_char_count'."""
    return dict["count"]


def sort_char_count(char_count: dict[str, int]) -> list[dict]:
    """Return list of character count dictionaries osrted by count desc."""
    output_list = [] # output list
    for item in char_count:
        ch = item
        count = char_count[item]
        output_dict = {"character": ch, "count": count}
        output_list.append(output_dict)

    # sort()  does sorting in place, it does not return sorted object.
    output_list.sort(key=sort_key, reverse=True)

    return output_list
