from collections import defaultdict

def get_num_words(book):
    num_words = len(book.split())
    return f"Found {num_words} total words"

def get_num_characters(book):
    book = book.lower()
    book = book.split()
    char_counts  = defaultdict(int)
    for word in book:
        for c in word:
            char_counts[c] += 1
    return dict(char_counts)