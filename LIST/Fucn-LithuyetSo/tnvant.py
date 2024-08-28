

from math import *

def tn(n):
    rev = 0
    tmp = n
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == tmp

def three_uoc(n):
    res = 0
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0:
            cnt =0
            while n % i == 0:
                n //= i
            res += 1
    if n > 1: res += 1
    return res >= 3


if __name__ == '__main__':
    a , b = map(int , input().split())
    ok = False
    for i in range(a , b + 1):
        if tn(i) and three_uoc(i):
            ok = True
            print(i , end= ' ')
    if ok == False: print("-1")

