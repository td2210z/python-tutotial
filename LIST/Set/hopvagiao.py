from math import *
from collections import Counter
from functools import cmp_to_key


if __name__ == '__main__':
    n ,m = map(int , input().split())
    a = set(list(map(int , input().split())))
    b = set(list(map(int , input().split())))

    t1 = list(a.intersection(b)) # giao
    t2 = list(a.union(b))   # hop
    t1.sort()
    t2.sort()
    for x in t1:
        print(x , end = ' ')
    print()
    for x in t2:
        print(x , end =' ')
