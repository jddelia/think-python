#This program traverses a string in reverse.

def reversestring():
    word = input("Enter word here: ")
    index = len(word) - 1
    while index > -1:
        print(word[index])
        index -= 1

reversestring()
