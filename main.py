from stats import (
    count_words,
    count_characters,
    sort_char,
)

import sys
import os


def check_args():
    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            return sys.argv[1]
        else:
            print("Invalid Path")
            sys.exit(1)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def print_report(book_path, word_count, char_sort):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_sort:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


def main():
    book_path = check_args()
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    char_sort = sort_char(char_count)

    print_report(book_path, word_count, char_sort)


main()
