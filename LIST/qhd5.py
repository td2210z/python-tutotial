from math import *

f = [True] * (10**6 + 7)

def init():
    f[0] , f[1] = False , False
    for i in range(2 , isqrt(10 ** 6) + 1):
        if f[i]:
            for j in range(i *i , 10 ** 6 + 1 , i):
                f[j] = False


if __name__ == '__main__':
    init()
    dem =0
    ans = [0] * (10 ** 6 + 1)
    ans[0] , ans[1] = 0 , 0
    ans[2] = 2
    for i in range(3 , 10 ** 6 + 1):
        if f[i]:
            ans[i] = ans[i-1] * i
        else:
            ans[i] = ans[i-1]
        ans[i] %= (10 ** 9 + 7)
    t = int(input())
    for i in range(t):
        n = int(input())
        print(ans[n])
