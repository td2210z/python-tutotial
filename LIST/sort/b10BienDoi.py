from math import *
from functools import cmp_to_key

def dau_tien(a , n , x):
    res = -1
    l , r = 0 , n-1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            res = m
            r = m-1
        elif a[m] < x:
            l = m + 1
        else:
            r = m-1
    return res

def cuoi_cung(a , n , x):
    res = -1
    l , r = 0 , n-1
    
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            res = m
            l = m+1
        elif a[m] < x:
            l = m + 1
        else:
            r = m-1
    return res

def last1(a , n , x):
    res = -1
    l , r = 0 , n-1
    
    while l <= r:
        m = (l + r) // 2
        if a[m] >= x:
            res = m
            r = m-1
        else:
            l = m +1
    return res

def last2(a , n , x):
    res = -1
    l , r = 0 , n-1
    
    while l <= r:
        m = (l + r) // 2
        if a[m] > x:
            res = m
            r = m-1
        else:
            l = m +1
    return res


if __name__ == "__main__":
    n ,x = map(int , input().split())
    a = list(map(int , input().split())) 
    print(dau_tien(a , n ,x))
    print(cuoi_cung(a , n , x))
    print(last1(a , n , x))
    print(last2(a , n , x))

    if dau_tien(a , n , x) != -1:
        print(cuoi_cung( a, n , x) - dau_tien(a , n , x) + 1)
    else:
        print("0")

