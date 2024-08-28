from math import *
from collections import Counter
from functools import cmp_to_key


if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    b = list(dict(Counter(a)).items())
    c = sorted(b , key = lambda x : x[0])
    for x ,y in c:
        print(x , y , end = ' ')
    print()
    for x , y in b:
        print(x , y , end = ' ')
        
