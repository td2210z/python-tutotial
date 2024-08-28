from math import *



if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    t_max1 , t_max2 = 0 , 0
    vlue = 0
    for i in range(0 , len(a)):
        if a[i] > t_max1:
            t_max2 = t_max1
            t_max1 = a[i]
        elif a[i] > t_max2:
            t_max2 = a[i]
    print(t_max1 , t_max2)

    