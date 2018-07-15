# This program finds the cumulative sum of
# a list by addin each consecutive digit to the previous
# from a given list.

t = [1, 2, 3, 4, 5]

def cum_sum(n):
    sum1 = [1]
    count1 = 0
    count2 = 1
    for i in t:
        sumcount1 = sum1[count1]
        sumcount2 = t[count2]
        sum1.append(sumcount1 + sumcount2)
        count1 += 1
        if i != t[-2]:
            count2 += 1
        else:
            break
    print(sum1)

cum_sum(t)
