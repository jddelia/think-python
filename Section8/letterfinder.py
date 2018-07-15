#This program traverses a sequence(word)
#for a letter in said word.

def find(word, letter, startpoint):
    int(startpoint)
    length = len(word)
    while startpoint < length:
        if word[startpoint] == letter:
            print(startpoint)
            return startpoint
        startpoint = startpoint + 1
    print("The letter isn't in the word")

find("test", "e", 0)
