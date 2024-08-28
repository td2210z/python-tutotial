from math import *

a = []
dem = 0
path = [[-1 , 0] ,[0 , -1] , [0 ,1] , [1 , 0]]
#path = [[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 ,1]]
def oang(i , j):
    a[i][j] = 0
    global dem
    dem += 1
    for x , y in path:
        i1 = i + x
        j1 = j + y
        if i1 >= 0 and i1 < n and j1 >=0 and j1 < m and a[i1][j1] == 1:
            oang(i1 , j1)


if __name__ == '__main__':
    n , m = map(int , input().split())
    a = []
    for i in range(n):
        b = list(map(int , input().split()))
        a.append(b)
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                dem =0
                oang(i , j)
                ans = max(ans , dem)
    print(ans)