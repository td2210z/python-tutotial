

import math

def nt(n):
    if n < 2: return False
    for i in range(2 , math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        for i in range(2 , n // 2 + 1):
            if nt(i) and nt(n-i):
                print(i , n -i)