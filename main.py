from stats import count_words, character_frequency, list_of_dict
import sys


def main(file_path):
    frankenstein = get_book_text(file_path)

    print("============= BOOKBOT =================")
    print(f"Analysing book found at {file_path}")
    print("-------Word Count------")
    print(f"Found {count_words(frankenstein)} total words")
    print("----Character Count----")

    array = list_of_dict(character_frequency(frankenstein))

    for dic in array:
        if dic["character"].isalpha():
            print(f"{dic["character"]}: {dic["num"]}")

    print("===========END===============")


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents


file = sys.argv[1]
main(file)
