# https://www.codewars.com/kata/iq-test/train/python

def iq_test(numbers):
    arr2 = []
    numbers = numbers.split()
    for i in numbers:
        if (int(i) %2 ) == 0:
            arr2.append(1)
        else:
            arr2.append(0)
    if arr2.count(1) == 1:
        for num,k in enumerate(arr2):
            if k == 1:
                return num +1 
    else:
        for num,k in enumerate(arr2):
            if k == 0:
                return num +1
