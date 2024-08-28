from math import *
from collections import Counter
from functools import cmp_to_key


if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))



    # a = set(a)   DUNG SET
    # z = int(input())
    # for _ in range(z):
    #     t = int(input())
    #     if t in a:
    #         print("YES")
    #     else:
    #         print("NO")
        
    # dung dict
    d = {}
    for x in a:
        d[x] = 1
    t = int(input())
    for _ in range(t):
        z = int(input())
        for z in d:
            print("YES")
        else:
            print("NO")
        