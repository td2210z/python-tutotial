from math import *



if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int , input().split()))
        a.append(b)
    d = dict({})
    for i in range(n):
        d[a[0][i]] = 1
        
    for i in range(1 , n):
        for j in range(n):
            if d[a[i][j]] == i:
                d[a[i][j]] += 1
    for x ,y in d.items():
        if y == n:
            print(x , end = ' ')
