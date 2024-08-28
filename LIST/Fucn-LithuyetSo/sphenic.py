from math import *

def sp(n):
    res = 0
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0:
            cnt =0
            while n % i == 0:
                cnt += 1
                n //= i
            if cnt > 1: return False
            else: res+=1
    if n > 1: res += 1
    return res == 3

if __name__ == '__main__':
    n = int(input())
    if sp(n):
        print("1")
    else:
        print("0")
    