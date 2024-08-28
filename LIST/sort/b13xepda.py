from math import *
from functools import cmp_to_key

if __name__ == "__main__":
    n = int(input())
    a = list(map(int , input().split()))
    a.sort(reverse=True)
    docung = a[0]
    ans = 1
    for i in range(1 , n):
        if docung >= 1:
            ans += 1
        else: break
        docung = min(docung -1 ,a[i])
    print(ans)