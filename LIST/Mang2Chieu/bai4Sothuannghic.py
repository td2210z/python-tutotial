from math import *


def tn(n):
    rev = 0
    tmp = n
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == tmp

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int , input().split()))
        a.append(b)
    cnt =0
    for i in range(n):
        for j in range(i + 1):
            if tn(a[i][j]):
                cnt += 1
    print(cnt)