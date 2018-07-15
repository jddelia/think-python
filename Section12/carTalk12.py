''' This program finds the largest English word that
    can be reduced one letter at a time, while still
    being a word after each reduction. '''

fin = open('words2.txt')
d = {}
for letter in ["", "i", "a"]: # Base words.
    d[letter] = None

lst = [line.rstrip().lower() for line in fin] # Word list.
sorted(lst)

for word in lst:
    d[word] = None

memo = {}

def reducer(word):
    global memo
    end = word[:-1]
    frnt = word[1:]

    if end in lst:
        memo[end] = None
        return end
    elif frnt in lst:
        memo[frnt] = None
        return frnt

def reduced_word():
    global memo
    new_lst = []
    for word in d:
        rdce_word = reducer(word)
        while rdce_word in d:
            memo[rdce_word] = None
            new_lst.append(rdce_word)
            rdce_word = reducer(rdce_word)

    return new_lst

print(reduced_word())
