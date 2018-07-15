# This program interlocks words to form
# new words.

def interlock_word(word1, word2):
    interlock = ""
    n = 0
    for i in word1:
        interlock += (i + word2[n])
        n += 1
        print(interlock)

interlock_word("shoe", "cold")
