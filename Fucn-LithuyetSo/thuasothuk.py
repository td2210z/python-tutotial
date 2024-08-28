
from math import *

def pt(n , k):
    res = 0
    for i in range(2 , isqrt(n)):
        while n % i == 0:
            res += 1
            n //= i
            if res == k: return i
    if n > 1: res += 1
    if res == k: return n
    else: return -1

if __name__ == '__main__':
    n , k = map(int  , input().split())
    print(pt(n , k))
