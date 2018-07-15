fin = open("words.txt")
line = fin.readline()
word = line.strip()


def letter_avoid():
    print('''Type all the letters you don't
want the word to have.''')
    n = input("Enter letters here: ")

    for line in fin:
        word = line.strip()
        for i in n:
            if i in word:
                break
            if i == n[-1]:
                print(word)

def uses_all():
    n = input("Enter letters here: ")
    length = len(n)
    for line in fin:
        word = line.strip()
        for i in n:
            if i not in word:
                break
            if i == n[-1]:
                print(word)

uses_all()
