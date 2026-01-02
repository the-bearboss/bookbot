from stats import get_num_words, get_num_characters

def get_book_text(filename):
    with open(filename) as f:
        book_contents = f.read()
    
    return book_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    words = get_num_words(book)
    print(f"Found {words} total words")
    char_nums = get_num_characters(book)
    print(char_nums)
    

main()