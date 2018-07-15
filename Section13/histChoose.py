''' This function uses the random module to select random
    keys in a histogram, while taking into account
    frequency of of key and how it relates to probability. '''

import random

def choose_from_hist(hist):
    lst_hist = []

    for k, v hist.items():  # Converts hist to a list.
        for i in range(v):      # Loop in range of freq.
            lst_hist.append(k)  # Appends k each loop.

    random.choice(lst_hist)
