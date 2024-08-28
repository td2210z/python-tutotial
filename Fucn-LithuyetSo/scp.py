from math import *

def scp(n):
    z = isqrt(n)
    if z + z == n: return True
    else: return False


if __name__ == '__main__':
    n = int(input())
    if scp(n): print("YES")
    else:
        print("NO")