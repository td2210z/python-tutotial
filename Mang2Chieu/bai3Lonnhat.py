from math import *




if __name__ == '__main__':
    n , m = map(int , input().split())
    a = []
    for i in range(n):
        b = list(map(int , input().split()))
        a.append(b)
    min_vl , max_vl = 10 ** 9 + 7, -10 ** 9 + 7
    for i in range(n):
        for j in range(m):
            if a[i][j] < min_vl:
                min_vl = a[i][j]
    print(min_vl)
    for i in range(n):
        for j in range(m):
            if a[i][j] == min_vl:
                print(i +1 , j +1)
    
    for i in range(n):
        for j in range(m):
            if a[i][j] > max_vl:
                max_vl = a[i][j]
    print(max_vl)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_vl:
                print(i + 1, j + 1)
        