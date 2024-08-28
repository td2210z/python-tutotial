from math import *
from functools import cmp_to_key




if __name__ == "__main__":
    n , x= map(int , input().split())
    a = list(map(int , input().split()))
    a.sort()
    i , j = 0 , n-1
    ans = 0
    while i <= j:
        if a[i] + a[j] <= x:
            ans += 1
            i += 1
            j -= 1
        else:
            ans += 1
            j -= 1
    print(ans)

   
    
