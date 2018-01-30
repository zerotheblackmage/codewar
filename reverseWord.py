# https://www.codewars.com/kata/reverse-words/train/python

import re
def reverse_words(str):
  stl = re.split(r'(\s+)', str)
  result = []
  for word in stl:
      word = word[::-1]
      result.append(word)
  return ''.join(result)
