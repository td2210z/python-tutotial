from math import *



if __name__ == '__main__':
    n = int(input())

    a = list(map(int , input().split()))
    
    cnt = [0] * 1000007
    for x in a:
        cnt[x] += 1
    s1 , v1 = 0 , 0
    for x in a:
        if cnt[x] > v1:
            s1 , v1 = x , cnt[x]
    print(s1 , v1)
    