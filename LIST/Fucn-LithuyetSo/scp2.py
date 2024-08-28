from math import *

#so chinh phuong trong doan 

if __name__ == '__main__':
    a , b = map(int , input().split())
    z1 = isqrt(a)
    z2 = isqrt(b)
    for i in range(z1 , z2+1):
        tmp = i *i
        if tmp >= a and tmp <= b:
            print(tmp , end= ' ')