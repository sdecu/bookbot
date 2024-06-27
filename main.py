import string
def main():
    book = get_text()
    get_word_count(book) 
    get_char_count(book) 


def get_text():
    with open("books/frankenstein.txt") as f:
        return f.read()


def get_word_count(string):
    string = string.split()
    i = 0
    for s in string:
        i +=1
    return i


def get_char_count(book):
    arr = list(book)
    alphabet = string.ascii_lowercase
    dict = {}
    for c in alphabet:
        i = 0
        for letter in arr:
            if c == letter.lower():
                i += 1
        dict[c] = i
    return dict
main()
