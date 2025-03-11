from stats import count_words, count_char, sorted_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(path):
    str = get_book_text(path)
    char_count = count_char(str)
    count_sorted_dict = sorted_dict(char_count)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    count_words(str)
    print(f"--------- Character Count -------")
    for item in count_sorted_dict:
        if item["character"].isalpha():
            print(f"{item["character"]}: {item["count"]}")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])
