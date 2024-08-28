from math import *
from sys import stdin


if __name__ == '__main__':
    a = []
    for s in stdin:
        a += list(map(int , s.split()))
    c , l =0 , 0
    for x in a:
        if x % 2 == 0:
            c += 1
        else:
            l += 1
    if c == l: print('CHANLE')
    elif c > l: print('CHAN')
    else: print('LE')