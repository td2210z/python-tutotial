from math import *


def check(a):
    l , r = 0 , len(a) -1

    while l <= r:
        if a[l] != a[r]:
            return False
        l +=1
        r -= 1
    return True


if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    # b = a.copy()
    # b[::]
    # if check(a , b , n -1):
    #     print("YES")
    # else:
    #     print("NO")
    b = a[:]
    a.reverse()
    if a == b:
        print("YES")
    else:
        print("NO")
    
    

    