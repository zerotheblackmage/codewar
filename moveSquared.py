# https://www.codewars.com/kata/moves-in-squared-strings-ii/train/python

def rot(strng):
    strng = strng[::-1]
    conv = strng.split("n\\")
    print(conv)
    strng2 = '\n'.join(conv)
    return(strng2)
    
        
    
def selfie_and_rot(strng):
    st2 = strng[::-1]
    res = []
    conv = st2.split()
    convo = strng.split()
    x = 0
    dots = "." * len(conv[0])
    for i in convo:
        res.append(i)
        res.append(dots +"\n")
    for i in conv:
        if not x == 0:
            res.append("\n" + dots)
        else:
            res.append(dots)
        res.append(i)
        x += 1
    print(res)    
    return ''.join(res)
        
def oper(fct, s):
    print(repr(s))
    return fct(s)
