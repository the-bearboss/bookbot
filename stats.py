def get_num_words(book_contents):
    word_list = book_contents.split()

    return(len(word_list))

def get_num_characters(book_contents):
    #create empty dictionary
    char_count = {}

    #count the letters
    for letters in book_contents.lower():
        if letters in char_count:
            char_count[letters] += 1
        else:
            char_count[letters] = 1

    return (char_count)