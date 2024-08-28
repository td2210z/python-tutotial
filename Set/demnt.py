from math import *
from collections import Counter
from functools import cmp_to_key
from sys import stdin


def kg(n):
    res = n % 10
    n //= 10
    while n != 0:
        if res < n % 10:
            return False
        res = n % 10
        n //= 10
    return True

    
if __name__ == '__main__':
    
    d = dict({})
    for line in stdin:
        a = list(map(int , line.split()))
        for x in a:
            if kg(x):
                if x in d:
                    d[x] += 1
                else:
                    d[x] = 1
    d = list(d.items())
    d.sort(key= lambda x : (-x[1] , x[0]))
    for x ,y in d:
        print( x , y)
