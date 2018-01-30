# https://www.codewars.com/kata/highest-scoring-word/train/python

import string
def high(x):
    x = x.split()
    result = []
    for word in x:
        temp = []
        for c in word:
            cn = string.ascii_lowercase.index(c) + 1
            temp.append(cn)
        result.append(sum(temp))
    m = max(result)
    for num,i in enumerate(result):
        if i == m:
            return(x[num])
