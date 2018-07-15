#This program takes in a word to produce
#a Caesar cypher.

def rotate_word(word, n):
    letters = word[0]
    newword = ""

    for letters in word:
        newletter = chr(ord(letters) + n)
        newword = newword + newletter
    print(newword)

rotate_word("test", 2)
