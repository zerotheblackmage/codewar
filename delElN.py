# https://www.codewars.com/kata/delete-occurrences-of-an-element-if-it-occurs-more-than-n-times/train/python/

def delete_nth(order,max_e):
    results = []
    for i in order:
        if not results.count(i) == max_e:
            results.append(i)
            
    return(results) 
