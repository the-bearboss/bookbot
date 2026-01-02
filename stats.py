def sort_on(item):
    return item["num"]

def get_num_words(book_contents):
    word_list = book_contents.split()

    return len(word_list)

def get_num_characters(book_contents):
    #create empty dictionary
    char_count = {}

    #count the letters
    for ch in book_contents.lower():
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

    return char_count

def sort_dicts(incoming):
    unsorted = []

    for ch,num in incoming.items():
        unsorted.append({"char": ch, "num": num})
    unsorted.sort(key=sort_on, reverse=True)

    return unsorted