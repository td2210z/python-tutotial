

import math

def lcm(a , b):
    return a * b // math.gcd(a , b)

if __name__ == '__main__':
    x , y , z , n = map(int , input().split())
    bc = lcm(lcm(x , y) , z)
    tmp = 10 ** (n-1)
    ans = (tmp + bc - 1) // bc * bc
    if ans < 10 ** n:
        print(ans)
    else:
        print('-1')
