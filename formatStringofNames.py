#https://www.codewars.com/kata/format-a-string-of-names-like-bart-lisa-and-maggie/train/python

def namelist(names):
    resa = []
    if len(names) == 0:
        return ''    
    for d in names:
       resa.append(d["name"])    
    if len(resa) == 1:
        return resa[0]

    result = ' & '.join(resa)
    result = result.replace(' & ',', ', (result.count(' & ') -1))
    
    return result
