# This is practice using nested conditionals

def binomial_coeff(n, k):
    return 1 if k == 0
    return 0 if n == 0

    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    return res

binomial_coeff(0, 1)
