# https://www.codewars.com/kata/find-the-stray-number/train/python

def stray(arr):
    y = arr[:]
    x = arr[0]
    while x in y:
        y.remove(x)

    if len(y) == 1:
        return y[0]
    else:
        return x
