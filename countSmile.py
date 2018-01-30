# https://www.codewars.com/kata/count-the-smiley-faces/train/python

import re
def count_smileys(arr):
    x = 0
    for s in arr:
        if not (re.match('[:;][-~]?[)D]', s)) is None:
            x +=1
    return x  
