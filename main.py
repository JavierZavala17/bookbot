from stats import get_num_words, get_num_characters, dict_to_sorted_list 

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def main():
    relative_path_to_frankenstein = "./books/frankenstein.txt"
    frankenstein = get_book_text(relative_path_to_frankenstein)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(get_num_words(frankenstein))
    print("--------- Character Count -------")
    dict_char_count = get_num_characters(frankenstein)
    sorted_list = dict_to_sorted_list(dict_char_count)
    for d in sorted_list:
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")


main()