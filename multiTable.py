#https://www.codewars.com/kata/multiplication-tables/train/python/

def multiplication_table(row,col):
    x = row
    y = col
    result = []
    
    while x is not 0:
        temp = []
        while y is not 0:
            temp.append(x *y)
            y -= 1
        temp.reverse()    
        result.append(temp)    
        y = col
        x -= 1
    result.reverse()    
    return result    
