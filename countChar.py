# https://www.codewars.com/kata/count-characters-in-your-string/train/python

def count(string):
    # The function code should be here
    dict = {}
    for i in string:
        if i not in dict:
            dict[i] = string.count(i)
    return dict
