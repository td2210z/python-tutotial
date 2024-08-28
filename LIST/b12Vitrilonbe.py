from math import *



if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    vt1 , vt2 = 0 , 0
    max_gt , min_gt = -10 ** 9 + 7 , 10 ** 9 + 7
    for i in range(0 , len(a)):
        if a[i] > max_gt:
            max_gt = a[i]
            vt1 = i
        if a[i] <= min_gt:
            min_gt = a[i]
            vt2 = i
    
    print(vt2 , vt1)

    