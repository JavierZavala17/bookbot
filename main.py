from stats import get_num_words, get_num_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def main():
    relative_path_to_frankenstein = "./books/frankenstein.txt"
    frankenstein = get_book_text(relative_path_to_frankenstein)
    print(get_num_words(frankenstein))
    print(get_num_characters(frankenstein))

main()