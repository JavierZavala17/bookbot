from stats import get_num_words, get_num_characters, dict_to_sorted_list 
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:   
        book = get_book_text(sys.argv[1])
        
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(get_num_words(book))
        print("--------- Character Count -------")
        dict_char_count = get_num_characters(book)
        sorted_list = dict_to_sorted_list(dict_char_count)
        for d in sorted_list:
            print(f"{d['char']}: {d['num']}")
        print("============= END ===============")


main()