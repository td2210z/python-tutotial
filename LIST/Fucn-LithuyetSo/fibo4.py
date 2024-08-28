
from math import *


def nt(n):
    if n < 2: return False
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0:
            return False
    return True



def fibo(n):
    if  n == 1: return True
    f1 , f2 = 1 , 1
    for i in range(2 , 23):
        fn = f1 + f2
        if fn == n: return True
        f2 , f1 = f1 , fn
    return False

def tong(n):
    sum =0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        if nt(i) and fibo(tong(i)):
            print(i , end = ' ')
    