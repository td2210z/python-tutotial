from math import *

def nt(n):
    if n < 2: return False
    for i in range(2 , isqrt(n)):
        if n % i == 0:
            return False
    return True

def cs(n):
    sum =0
    while n != 0:
        res = n % 10
        
        if (res != 2 or res != 3 or res != 5 or res != 7) :return False
        sum += res
        n //= 10
    return nt(sum)



if __name__ == '__main__':
    a , b = map(int , input().split())
    cnt =0
    for i in range(a , b +1):
        if cs(i) and nt(i):
            cnt += 1
    print(cnt)