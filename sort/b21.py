from math import *
from functools import cmp_to_key




if __name__ == "__main__":
    n , k= map(int , input().split())
    a = []
    for _ in range(n):
        b = list(map(int , input().split()))
        a.append(b)
    a.sort(key= lambda x : x[0])
    for x , y in a:
        if x >= k:
            print("NO")
            exit()
        k += y
    print("YES")
    
