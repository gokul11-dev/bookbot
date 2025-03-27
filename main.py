from stats import get_text_words,  get_char_count, get_sorted_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    text = get_book_text(sys.argv[1])
    num_words = get_text_words(text)
    print(f"Found {num_words} total words")
    word_cout_dict = get_char_count(text)
    print("--------- Character Count -------")
    sorted_char_dict_list = get_sorted_count(word_cout_dict)
    for char_dict in sorted_char_dict_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["count"]}")
    print("============= END ===============")

main()