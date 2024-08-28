from math import *

def nt(n):
    if n < 2:return False
    for i in range(2 , isqrt(n)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    res = len(a) // 2
    cnt1 , cnt2 =0 , 0
    for i in range(0 , len(a) //2):
        if nt(a[i]):
            cnt1 += 1
    
    for i in range(res , len(a)+1):
        if nt(a[i]):
            cnt2 += 1
    

    print(cnt1 + cnt2)


    

    