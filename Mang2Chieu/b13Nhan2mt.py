from math import *



if __name__ == '__main__':
    n , m ,p = map(int , input().split())
    a = []
    for i in range(n):
        bx = list(map(int , input().split()))
        a.append(bx)
    c = []
    for i in range(m):
        z = list(map(int , input().split()))
        c.append(z)

    ans = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                ans[i][j] *= a[i][k] + c[k][j]
    
    for i in range(n):
        for j in range(p):
            print(ans[i][j] , end = ' ')
        print()           
