# https://www.codewars.com/kata/take-a-ten-minute-walk/train/python

def isValidWalk(walk):
    if len(walk) < 10:
        return False

    elif ((walk.count('n') - walk.count('s') ) + ( walk.count('e') - walk.count('w'))) == 0:
        print(walk)
        return True
    else:
        return False
