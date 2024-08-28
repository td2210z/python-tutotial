from math import *

def check(a , l , r , x):
    if l > r:
        return False
    m = (l + r) /2
    if a[m] == x:
        return True
    elif a[m] < x:
        return check(a , m + 1 , r , x)
    else:
        return check(a , l , m-1 , x)
    



if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    x = int(input())
    a.sort()
    if check(a , 0 , n-1 , x):
        print("1")
    else:
        print("0")