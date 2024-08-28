from math import *


if __name__ == '__main__':
    n , x = map(int , input().split())
    a = list(map(int , input().split()))
    if x in a:
        a.pop(a.index(x))
        for x in a:
            print(x , end = ' ')
    else:
        print("NOT FOUND")
