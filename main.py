import sys
from stats import word_count
from stats import char_count
from stats import sort_dict


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    

def get_book_text(filepath):
    with open(filepath) as f:
       file_contents = f.read()
    return file_contents

def main():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = word_count(book_text)
    chars_counts = char_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_dict(chars_counts):
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")



main()



