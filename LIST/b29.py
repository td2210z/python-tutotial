from math import *



if __name__ == '__main__':
    n = int(input())

    a = list(map(int , input().split()))
    
    cnt = [0] * 1000007
    for x in a:
        cnt[x] += 1
    l , r = min(a) , max(a)
    s1 , vt1 = 0 , 0
    for i in range(l , r + 1):
        if cnt[i] > vt1:
            vt1 = cnt[i]
            s1 = i
    print(s1 , vt1)
    