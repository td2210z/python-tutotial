from math import *
from functools import cmp_to_key


def tong(n):
    sum =0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum


def cmp(a , b):
    tong1 , tong2 = tong(a) , tong(b)
    if tong1 == tong2:
        return a - b
    return tong1 - tong2


if __name__ == "__main__":
    n = int(input())
    a = list(map(int , input().split()))
    a.sort(key= cmp_to_key(cmp))
    for x in a:
        print(x , end= ' ')
