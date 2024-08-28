


from math import *


def check(n):
    if n < 2: return False
    for i in range(2 , isqrt(n) +1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    
    for i in range(n):
        l =0
        for j in range(0 , i):
            l += a[j]
        r = 0
        for j in range(i + 1, n):
            r += a[j]
        if check(l) and check(r):
            print(i , end = ' ')
    
    
    
    

    