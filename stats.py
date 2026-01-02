def get_num_words(book_contents):
    word_list = book_contents.split()

    return(len(word_list))

def get_num_characters(book_contents):
    #create dictionary of all lower case letters
    char_count = {
        'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,
        'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,
    }
    
    #change the book string into all lower case
    word_list = book_contents.lower()

    #count the letters
    for letter in char_count:
        char_count[letter] = word_list.count(letter)

    return (char_count)