# https://www.codewars.com/kata/mastermind/python 


import random
def mastermind(game):
    turns = 0
    colours = ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"]
    parsed = []
    for i in colours:
        attempt = [i]*4
        result = game.check(attempt)
        if result.count("Black") != 0:
            num = result.count("Black")
            print(num)
            print("There are {} {}s".format(num,i))
            for x in range(num):
                parsed.append(i)
    while True:
         result = game.check(parsed)
         if "White" in result:
             random.shuffle(parsed)
         else: 
              return parsed
