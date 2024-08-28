

from math import *


def so_lon(n):
    if n < 10:
        return n
    return max(n % 10 , so_lon(n // 10))


def so_be(n):
    if n < 10:
        return n
    return min(n % 10 , so_be(n // 10))

if __name__ == '__main__':
    n = int(input())
    print(so_lon(n) , so_be(n))