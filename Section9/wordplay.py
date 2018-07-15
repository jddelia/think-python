#This program will print words with 20+ characters.

fin = open("words.txt")
line = fin.readline()
word = line.strip()

def twenty():
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

#This program will print words without the letter "e".

total = 0
count = 0

def no_es():
    for line in fin:
        word = line.strip()
        total += 1
        if "e" not in word:
            print(word)
            count += 1
    print(count/total)
