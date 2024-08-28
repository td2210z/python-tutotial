from math import *
from collections import Counter
from functools import cmp_to_key


if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    f = [0] * n
    ans = set({})
    for i in range(n -1 , -1 , -1):
        ans.add(a[i])
        f[i] = len(ans)
    q = int(input())
    for _ in range(q):
        t = int(input())
        print(f[t])
        
