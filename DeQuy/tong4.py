
from math import *

def tong(n):
    if n == 1:
        return -1
    if n % 2 == 0: 
        return n + tong(n-1)
    else:
        return tong(n-1) - n

if __name__ == '__main__':
    n = int(input())
    print(tong(n))