def count_words(file_contents):
    word_count = len(file_contents.split())
    return word_count


def count_characters(file_contents):
    char_dict = {}
    for char in list(file_contents):
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict
