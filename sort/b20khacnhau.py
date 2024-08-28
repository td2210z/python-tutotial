from math import *
from functools import cmp_to_key

if __name__ == "__main__":
    n = int(input())
    a = list(map(int , input().split()))
    ans =0
    a.sort()
    for i in range(1 , n + 1):
        if a[i] != a[i-1]:
            ans += 1
    print(a[n-1] - a[0] - ans)
    
