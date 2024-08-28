from math import *
from functools import cmp_to_key


def check(a , l , r , x):
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return True
        elif a[m] < x:
            l = m + 1
        else:
            r = m-1
    return False

if __name__ == "__main__":
    n , x= map(int , input().split())
    a = list(map(int , input().split()))
    ans =0
    a.sort()
    for i in range(n):
        if check(a , 0 , n -1 , a[i] +x):
            print("1")
            exit()
    print("0")
    
