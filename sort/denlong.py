from math import *
from functools import cmp_to_key




if __name__ == "__main__":
    n , x= map(int , input().split())
    a = list(map(int , input().split()))
    ans =0
    a.sort()
    ans = max(a[0] - 0 , x - a[-1])
    for i in range(1 , n):
        ans = max(ans , (a[i] - a[i-1]) // 2)
    print("%.10f" % ans)
    
