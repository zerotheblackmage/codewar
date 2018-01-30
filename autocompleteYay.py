# https://www.codewars.com/kata/autocomplete-yay/train/python/

import re
def autocomplete(input_, dictionary):
    auto = "^" + str(re.sub('[^A-Za-z]+', '', input_))
    result = []
    for ch in dictionary:
        if re.match(auto, ch, re.IGNORECASE) is not None :
            result.append(ch)
    return result[:5]
