from stats import count_words, count_characters


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"Found {count_words(text)} total words")
    print(count_characters(text))


main()
