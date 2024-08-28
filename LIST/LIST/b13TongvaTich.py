from math import *



if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    vt1 , vt2 = 0 , 0
    tong , tich = 0 , 1
    for x in a:
        tong += x
        tong %= (10 ** 9 + 7)
        tich *= x
        tich %= (10 ** 9 + 7)

    