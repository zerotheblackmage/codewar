# https://www.codewars.com/kata/disemvowel-trolls/train/python

import re
def disemvowel(string):
      string = re.sub("[aeiouAEIOU]", "", string)
      return string
