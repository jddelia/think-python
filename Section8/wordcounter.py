#This program counts the amount of times a
#letter appears in a word.

def counter(word, letter, startpoint):
    letters = word[0]
    count = 0
    for letters in word[startpoint:]:
        if letters == letter:
            count += 1
            print(letter + ":", count)
    return count

counter("test", "t", 0)

def counter2(word, letter):
    print(word.count(letter))
    return word.count(letter)

counter2("test", "t")
