from math import *
from functools import cmp_to_key

def first(a , l , r , x):
    res = -1
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

def last(a , l , r , x):
    res = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            res= m
            l = m + 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m-1
    return res
            


if __name__ == "__main__":
    n , k = map(int , input().split())
    a = list(map(int , input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        p1 , p2 = first(a , i + 1, n -1 , k - a[i]) , last(a , i + 1, n -1 , k - a[i])
        if p1 != -1:
            ans += p2 - p1 + 1
    print(ans)
