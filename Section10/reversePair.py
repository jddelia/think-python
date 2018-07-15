# This program determines if two words are the reverse
# of each other.

fin = open('words.txt')
line = fin.readline()
word = line.strip()


t = []
for line in fin:
    word = line.strip()
    t.append(word)
t.sort()

fin = open('words.txt')

def reverse_pair():
    for i in fin:
        word = i.strip()
        if word[::-1] in t:
            print(word, word[::-1])

reverse_pair()
