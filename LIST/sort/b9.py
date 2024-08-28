from math import *
from functools import cmp_to_key

def tk(a , l , r , x):
    
    m = (l + r) // 2
    while l <= r:
        if a[m] == x:
            return True
        elif a[m] < x:
            l = m + 1
        else:
            r = m-1
    return False
        


if __name__ == "__main__":
    n = int(input())
    a = list(map(int , input().split()))
    a.sort()
    t = int(input())
    for _ in range(t):
        z = int(input())
        if tk(a , 0 , n-1 , z):
            print("YES")
        else:
            print("NO")

