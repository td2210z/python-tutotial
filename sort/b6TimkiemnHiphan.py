from math import *
from functools import cmp_to_key

def check(a , n , z):
    for i in range(n):
         if a[i] == z:
             return True
    return False
if __name__ == "__main__":
    n = int(input())
    a = list(map(int , input().split()))
    a.sort()
    t = int(input())
    for _ in range(t):
        z = int(input())
        if check(a , n , z):
            print("YES")
        else:
            print("NO")

