
from math import *

def uoc(n):
    ans = -1
    for i in range(2 , isqrt(n)):
        if n % i == 0:
            ans = i
            while n % i == 0:
                n //= i
    if n > 1: ans = n
    return ans 



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(uoc(n))