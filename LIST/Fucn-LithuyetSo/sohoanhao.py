

from math import *

def shh(n):
    dev = 1
    tmp = n
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0:
            dev += i
            if i != n // i: dev += n // i
    return dev == tmp

if __name__ == '__main__':
    n = int(input())
    if shh(n):
        print("YES")
    else:
        print("NO")
