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


def sort_on(items):
    return items["num"]


def sort_char(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"char": char, "num": char_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
