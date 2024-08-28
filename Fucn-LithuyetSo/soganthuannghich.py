
from math import *


def tn(n):
    rev = 0
    tmp = n
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return tmp == rev

def cd(n):
    res = n % 10
    n //= 10
    m = 0
    while n >= 10:
        m = m * 10 + n  % 10
        n //= 10
    if (res * 2== n or n * 2 == res) and tn(m): return True
    else: return False

if __name__ == '__main__':
    n = int(input())
    if cd(n):
        print("YES")
    else:
        print("NO")