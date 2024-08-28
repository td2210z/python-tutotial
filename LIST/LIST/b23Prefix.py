from math import *



if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    pre = [0] * 10000
    for i in range(0 , len(a)):
        pre[i] = pre[i-1] + a[i]
        print(pre[i] , end = ' ')
    