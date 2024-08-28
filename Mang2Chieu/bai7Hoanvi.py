from math import *



if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int , input().split()))
        a.append(b)
    x ,y = map(int , input().split())
    for i in range(n):
        tmp = a[x-1][i]
        a[x-1][i] = a[y-1][i]
        a[y-1][i] = tmp
    for i in range(n):
        for j in range(n):
            print(a[i][j] , end = ' ')
            