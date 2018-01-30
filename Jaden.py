# https://www.codewars.com/kata/jaden-casing-strings/train/python

def toJadenCase(string):
    reality = []
    eyes = string.split()
    for i in eyes:
       x = i[:1].upper()
       reality.append(x + i[1:])
    mirror = ' '.join(reality)
    return mirror
