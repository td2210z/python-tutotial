from math import *

a = []
#path = [[-1 , 0] ,[0 , -1] , [0 ,1] , [1 , 0]]
path = [[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 ,1]]

def check(i , j):
    for x , y in path:
        i1 = i + x
        j1 = j + y
        if i1 >= 0 and i1 <n and j1 >= 0 and j1 < m:
            if a[i1][j1] >= a[i][j]:
                return False
    return True

if __name__ == '__main__':
    n , m = map(int , input().split())
    a = []
    for i in range(n):
        b = list(map(int , input().split()))
        a.append(b)
    dem =0
    for i in range(n):
        for j in range(m):
            if check(i , j):
                dem += 1
    print(dem)