# This program checks whether two words
# are anagrams.

def is_anagram(word1, word2):
    for i in word1:
        if i not in word2:
            break
        if i in word2 and i == word2[-1]:
            print(word1 + ' is an anagram of ' + word2 + '.')

is_anagram()
