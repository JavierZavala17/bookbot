from collections import defaultdict

def get_num_words(book):
    num_words = len(book.split())
    return f"Found {num_words} total words"

def get_num_characters(book):
    book = book.lower()
    book = book.split()
    char_count  = defaultdict(int)
    for word in book:
        for c in word:
            char_count[c] += 1
    return dict(char_count)

def sort_on(items):
    return items["num"]


def dict_to_sorted_list(char_count):
    sorted_list_dict = []

    for char, count in char_count.items():
        if char.isalpha():
            sorted_list_dict += [{"char":char,"num":count}]
    
    sorted_list_dict.sort(reverse=True, key=sort_on)
    
    return sorted_list_dict