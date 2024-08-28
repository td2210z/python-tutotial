from math import *
from functools import cmp_to_key

def cmp(a , b):
    return abs(a) - abs(b)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int , input().split()))
    a.sort(key= cmp_to_key(cmp))
    for x in a:
        print(x , end= ' ')
