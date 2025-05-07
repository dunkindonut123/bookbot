from stats import count_words, count_letters, list_of_dict
import sys
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    length = len(sys.argv)
    if length < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print('----------- Word Count ----------')
    count_words(text)
    print('----------- Character Count -----')
    print(list_of_dict(count_letters(text)))
    print('============ END ============')

main()

