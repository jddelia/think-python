# This program determines whether a word
# has duplicate letters.

def has_duplicates(word):
    '''This creates a loop within a loop.
        For each index, it will loop through the word again,
        to determine if any word occurs more than once.'''

    for i in word:
        count = 0
        for n in word:
            if i == n:
                count += 1
            if count == 2:
                print(word)
                break
        if count == 2:
            break
has_duplicates("committee")
