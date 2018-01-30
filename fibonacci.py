# https://www.codewars.com/kata/fibonacci-tribonacci-and-friends/train/python/

def Xbonacci(signature,n):
    req = len(signature)
    result = signature[:]
    
    if n < len(result):
        result = signature[:n]
        return result
        
    if n == 0 :
        return []
    
    while len(result) < n:
        result.append(sum(result[-req:]))
    return result   
