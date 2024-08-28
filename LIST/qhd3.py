from math import *

f = [0] * (10 ** 6 + 1)

def init():
    f[0] = 0
    f[1] = 0
    f[2] = 1

    for i in range(3 , 10 ** 6 + 1):
        f[i] = f[i-1] + f[i-2] + f[i-3]
        f[i] %= (10 ** 9 + 7)


if __name__ == '__main__':
    init()
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print(f[n])
    