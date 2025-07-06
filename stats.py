def count_words(text):
    text_array = text.split()
    return len(text_array)


def sort_on(item):
    return item["num"]


def list_of_dict(dictionary):
    array = []
    for k, v in dictionary.items():
        array.append({"character": k, "num": v})

    array.sort(reverse=True, key=sort_on)
    return array


def character_frequency(text):
    text = text.lower()
    distinct_characters = set(text)

    char_dict = {key: 0 for key in distinct_characters}

    for i in text:
        char_dict[i] += 1

    return char_dict
