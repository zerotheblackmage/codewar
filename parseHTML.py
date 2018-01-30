# https://www.codewars.com/kata/parse-html-slash-css-colors/train/python

import re
result = {'r': 0, 'g': 0, 'b': 0 }

def parse_html_color(color):
    if re.match('^\#', color) is None:
        color = PRESET_COLORS[color.lower()]

    if len(color) == 4:
        color = "#" + (color[1] *2) + (color[2] *2) + (color[3] * 2)    

    result['r'] = (int(color[1:3],16))
    result['g'] = (int(color[3:5],16))
    result['b'] = (int(color[5:7],16))  
    return result
