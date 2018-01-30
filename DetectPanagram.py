# https://www.codewars.com/kata/detect-pangram/train/python

def is_pangram(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    for c in alpha:
        if c not in s:
            return False
    return True
