
from math import *

def nt(n):
    if n < 2: return False
    for i in range(2 , isqrt(n)):
        if n % i == 0:
            return False
    return True

def tong(n):
    sum =0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

def tong_so_chan(n):
    sum1 = 0
    while n != 0:
        res = n % 10
        if res % 2 == 0: sum1 += res
        n //= 10
    return sum1

def tong_nt(n):
    sum2 =0
    while n != 0:
        sum2 += n % 10
        n //= 10
    return nt(sum2)

def lat_nguoc(n):
    dev = 0
    while n != 0:
        dev = dev * 10 + n % 10
        n //= 10
    return dev

def ham6(n):
    cnt =0
    for i in range(2 , isqrt(n) + 1):
        if (n % i == 0):
            cnt += 1
            while n % i == 0:
                n //= i
    if n > 1: cnt += 1
    return cnt

def ham7(n):
    ans = 0
    for i in range(2 , isqrt(n) + 1):
        if (n % i == 0):
            ans = i
            while n % i == 0:
                n //= i
    if n > 1: ans = n
    return ans


def ham8(n):
    ans = 0
    while n != 0:
        res = n % 10
        if (res == 6): ans += 1
        n //= 10
    return ans > 1


def ham9(n):
    ans = 0
    while n != 0:
        ans += n % 10
        n //= 10
    if (ans % 10 == 8): return True
    else: return False



def ham10(n):
    res = 0
    while n != 0:
        res += factorial(n % 10)
        n //= 10
    return res

def ham11(n):
    res = 0
    while n != 0:
        res += 1
        n //= 10
    if res > 1: return False
    else: return True

def ham12(n):
    res = n % 10
    while n != 0:
        ans = n % 10
        if ans > res: return False
        n //= 10
    return True

def demcs(n):
    cnt = 0
    while n != 0:
        cnt += 1
        n //= 10
    return cnt

def ham13(n):
    sum =0
    d = demcs(n)
    while n != 0:
        sum += pow(n % 10 , d)
        n //= 10
    return sum

if __name__ == '__main__':
    n = int(input())
    if nt(n):
        print('1')
    else:
        print('0')

    print(tong(n))
    print(tong_so_chan(n))
    print(tong_nt(n))
    print(lat_nguoc(n))
    print(ham6(n))
    print(ham7(n))
    

    if ham8(n):
        print('1')
    else:
        print('0')
    
    if ham9(n):
        print('1')
    else:
        print('0')

    print(ham10(n))

    if ham11(n):
        print('1')
    else:
        print('0')

    if ham12(n):
        print('1')
    else:
        print('0')
    
    print(ham13(n))