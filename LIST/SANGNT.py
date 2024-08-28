from math import *

prime = [True] * (10 ** 6 + 1)

def sive():
    prime[0] , prime[1] = False , False
    for i in range(2 , isqrt(10 ** 6 +1)):
        if prime[i]:
            for j in range(i *i , 10**6 + 1, i):
                prime[j] = 0

if __name__ == '__main__':
    sive()
    n = int(input())
    if prime[n]:
        print("YES")
    else:
        print("NO")