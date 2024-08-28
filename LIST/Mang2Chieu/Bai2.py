from math import *




if __name__ == '__main__':
    n , m = map(int , input().split())
    a = []
    for i in range(n):
        b = list(map(int , input().split()))
        a.append(b)
    for i in range(n):
        print(sum(a[i]) , end = ' ')
    print()
    for j in range(m):
        tong = 0
        for i in range(n):
            tong += a[j][i]
        print(tong , end = ' ')
