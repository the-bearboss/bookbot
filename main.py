from stats import get_num_words, get_num_characters

def get_book_text(filename):
    with open(filename) as f:
        book_contents = f.read()
    
    return book_contents

def main():
   book_filename = "books/frankenstein.txt"
   book = get_book_text("books/frankenstein.txt")
   char_nums = get_num_characters(book)

   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {book_filename}...")
   print("----------- Word Count ----------")
   print(f"Found {get_num_words(book)} total words")
   print("--------- Character Count -------")
#print sorted list here
   print("============= END ===============")


main()