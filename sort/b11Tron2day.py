from math import *
from functools import cmp_to_key

if __name__ == "__main__":
    n , m = map(int , input().split())
    a = list(map(int , input().split()))
    b = list(map(int , input().split()))
    i , j =0 , 0
    
    a.sort()
    b.sort()
    cnt = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            i+= 1
        else:
            cnt+=1
            i += 1
            j += 1
    print(cnt)

