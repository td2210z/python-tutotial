from math import *



if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int , input().split()))
        a.append(b)
    print("Pattern 1:")
    for i in range(n):
        for j in range(n):
            print(a[j][i] , end =' ')
        print()
    
    print("Pattern 2:")
    for i in range(n-1 , -1 ,-1):
        for j in range(n-1 , -1 ,-1):
            print(a[i][j] , end = ' ')
        print()
    print("Pattern 3:")
    for i in range(n-1 , - 1, -1):
        for j in range(n):
            print(a[j][i] , end = ' ')
        print()
    print("Pattern 4:")
    for i in range(n):
        for j in range(n-1 , -1 , -1):
            print(a[i][j] , end =' ')
        print()