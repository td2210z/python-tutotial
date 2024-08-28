
from math import *

def nt(n):
    if n < 2: return False
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def cs(n):
    res = n % 10
    while n != 0:
        ans = n % 10
        if ans > res: return False
        n //= 10
    return True


if __name__ == '__main__':
    n = int(input())
    cnt = 0
    for i in range( n + 1):
        if cs(i) and nt(i):
            cnt += 1
            print(i , end = ' ')
    print()
    print(cnt)