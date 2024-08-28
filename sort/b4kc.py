from math import *
from functools import cmp_to_key




if __name__ == "__main__":
    n = int(input())
    a = list(map(int , input().split()))
    a.sort()
    ans = 10 ** 9 + 1
    for i in range(1 , n):
        ans = min(ans , a[i] - a[i+1])
    print(ans)
