# https://www.codewars.com/kata/title-case/train/python

import sys
def title_case(title, minor_words = ' '):

    if title == '':
        return title
        sys.exit()

    t = title.lower().split()
    opt = minor_words.lower().split()
    convert = []
    
    for i in t:
        if not i in opt:
            convert.append(i.capitalize())
        else:
            convert.append(i)
    convert[0] = convert[0].capitalize()    
    return ' '.join(convert)
