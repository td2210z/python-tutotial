from math import *



if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int , input().split()))
        a.append(b)
    x ,y = map(int , input().split())
    for i in range(n):
        tmp = a[i][x-1]
        a[i][x-1] = a[i][y-1]
        a[i][y-1] = tmp
    for i in range(n):
        for j in range(n):
            print(a[i][j] , end = ' ')
        print()    