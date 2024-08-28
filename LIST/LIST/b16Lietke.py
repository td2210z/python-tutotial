from math import *

def nt(n):
    if n < 2: return False
    for i in range(2 , isqrt(n)):
        if n % i == 0:
            return False
    return True

def tn(n):
    rev =0
    tmp = n
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == tmp

def cp(n):
    z = isqrt(n)
    if z * z == n: return True
    else: return False

def tong(n):
    sum =0
    while n != 0:
        sum += n % 10
        n //= 10
    return nt(sum)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    cnt =0
    cnt1 ,cnt2 , cnt3 = 0 , 0 , 0
    for x in a:
        if nt(x):
            cnt += 1
        if tn(x):
            cnt1 += 1
        if cp(x):
            cnt2 += 1
        if tong(x):
            cnt3 += 1
    
    print(cnt)
    print(cnt1)
    print(cnt2)
    print(cnt3)

    