from math import *
from collections import Counter
from functools import cmp_to_key


if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    d = dict({})
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] =1

    q = int(input())
    for _ in range(q):
        t1 , t2 = map(int , input().split())
        if t1 == 1:
            if t2 in d:
                d[t2] += 1
            else:
                d[t2] = 1
        elif t1 == 2:
            if t2 in d:
                d[t2] -= 1
                if d[t2] == 0:
                    d.pop(t2)
        else:
            if t2 in d:
                print("YES")
            else:
                print("NO")

