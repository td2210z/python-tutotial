from math import *



if __name__ == '__main__':
    f = [0] * 1000
    f[0] = 0
    f[1] = 1
    for i in range(2 , 100):
        f[i] = f[i-1] + f[i-2]
    n = int(input())
    a = [[0 for _ in range(n)] for _ in range(n)]
    dem = 0
    h1 , h2 , c1 , c2 = 0 , n -1 ,0 , n-1
    while dem < n * n:
        for i in range(c1 , c2 + 1):
            a[h1][i] = f[dem]
            dem += 1
        h1 += 1
        for i in range(h1 , h2 + 1):
            a[i][c2] = f[dem]
            dem += 1
        c2 -=1
        for i in range(c2 , c1 -1 , -1):
            a[h2][i] = f[dem]
            dem += 1
        h2 -= 1
        for i in range(h2 , h1 -1 , -1):
            a[i][c1] = f[dem]
            dem += 1
        c1 += 1
    for i in range(n):
        for j in range(n):
            print(a[i][j] , end = ' ')
        print()   
