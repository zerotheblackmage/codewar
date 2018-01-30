# https://www.codewars.com/kata/street-fighter-2-character-selection/train/python

def street_fighter_selection(fighters, initial_position, moves):
    result = []
    print(fighters[0][0])
    y = int(initial_position[0])
    x = int(initial_position[1])
    
    if moves == None:
        return result
    
    for m in moves:
        if m == "left":
            if x == 0:
                x = 5
            else:
                x -= 1
        if m == "right":
            if x == 5:
                x = 0
            else:
                x += 1
      
        if m == "up" and y == 1:
           y = 0
        if m == "down" and y == 0:
            y = 1 

        print(x, y)
        guy = fighters[int(y)][int(x)]
        result.append(guy)
  
    return result
