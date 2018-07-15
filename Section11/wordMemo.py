''' This program stores words from words.txt in a dictionary
     as a memo, and uses that dictionary in a function to
     search for a word in words.txt '''

fin = open('words.txt')
line = fin.readline()
word = line.strip()
wordDict = dict()

def word_build():
    for line in fin:
        word = line.strip()
        wordDict[word] = word
    return wordDict

wordDict = word_build()

def word_search(word):
    if word in wordDict:
        return wordDict[word]
    else:
        for line in fin:
            word2 = line.strip()
            if word == word2:
                return word

print(word_search("testing"))
