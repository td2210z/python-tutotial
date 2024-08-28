from math import *
from functools import cmp_to_key

if __name__ == "__main__":
    n = int(input())
    a = list(map(int , input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        if a[i] - i >= 0:
            ans += a[i] - i
        else:
            break
    print(ans)
