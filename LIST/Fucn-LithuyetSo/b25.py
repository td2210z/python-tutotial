
from math import *

def check(n):
    z = isqrt(n)
    if z * z == n:
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")