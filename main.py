def main():
    get_word_count() 



def get_text():
    with open("books/frankenstein.txt") as f:
        return f.read()


def get_word_count():
    string = get_text()
    string = string.split()
    i = 0
    for s in string:
        i +=1
    print(i)

main()
