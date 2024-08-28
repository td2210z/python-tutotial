from math import *

f = [0] * (10 ** 6 + 1)

def init():
    f[0] =1
    for i in range(1 , 10 ** 6 + 1):
        f[i] = f[i-1] * i
        f[i] %= (10 ** 9 + 7)

if __name__ == '__main__':
    init()
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print(f[n])
    