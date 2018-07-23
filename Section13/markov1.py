# This program generates a Markov Chain.

from collections import defaultdict
from random import choice

with open('meditations.txt') as fp:
    txt = fp.read().split()

txt_dict = defaultdict(list)

for word, nxt_word in list(zip(txt, txt[1:])):
    txt_dict[word].append(nxt_word)

def markov():
    word = 'The'
    for i in range(20):
        print(word, end=' ')
        word = choice(txt_dict[word])

markov()
