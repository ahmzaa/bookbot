from stats import (
    count_words,
    count_characters,
    sort_char,
)


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
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    char_sort = sort_char(char_count)

    print_report(book_path, word_count, char_sort)


main()
