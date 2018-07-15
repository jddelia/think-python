''' This program reads a file, breaks each line
    to words, strips punctuations and white spaces,
    and makes it lowercase. Refer to
    http://greenteapress.com/thinkpython2/html/thinkpython2014.html
    for more info. '''

import string
import re

def processor(file):
    fp = open(file)
    hist = {}
    for line in fp:
        formatter(line, hist)
    return hist

def formatter(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

meditations = processor('meditations.txt')

words3 = processor('words3.txt')

def most_freq(hist):
    freq_lst = []
    lst = []
    for k, v in hist.items():
        freq_lst.append([v, k])
    freq_lst = sorted(freq_lst, reverse=True)
    return freq_lst[:20]

freq_med = most_freq(meditations)

freq_words3 = most_freq(words3)

med_set = set(meditations)
word_set = set(words3)

print(med_set.difference(word_set))
