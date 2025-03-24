#!/usr/bin/python3
import sys

from stats import get_word_count, get_char_count, sort_char_count


def get_book_text(filepath: str) -> str:
    """Return content of the book specified by filepath."""
    with open(filepath, "rt", encoding="utf-8") as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 bookbot.py <path-to-book.txt>")
        sys.exit(1)
        return

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath} ...")
    content = get_book_text(filepath)

    print("---------- Word Count -----------")
    word_count = get_word_count(content)
    print(f"Found {word_count} total words.")
    print("-------- Character Count --------")

    char_count = get_char_count(content)
    # print(char_count)
    # print(sort_char_count(char_count))

    for item in sort_char_count(char_count):
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")

    print("============== END ===============")


main()
