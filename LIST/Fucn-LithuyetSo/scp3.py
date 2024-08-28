
from math import *

if __name__ == '__main__':
    a , b = map(int , input().split())

    z1 = isqrt(a)
    z2 = isqrt(b)
    cnt =0
    for i in range(z1 , z2+1):
        tmp = i * i
        if tmp >= a and tmp <= b:
            cnt += 1
    print(cnt)