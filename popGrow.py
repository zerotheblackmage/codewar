# https://www.codewars.com/kata/growth-of-a-population/train/python

def nb_year(p0, percent, aug, p):
    year = 0
    percent = (percent/100)
    print(percent)

    while (p0 < p):
        p0 = (p0 * (1 + percent)) + aug
        year += 1
    return year
