from math import *


if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    cnt = [0] * 1001
    for x in a:
        cnt[x] += 1
    cnt2= cnt.copy()
    l , r = min(a) , max(a)
    for x in a:
        if cnt[x] != 0:
            print(x , cnt[x])
            cnt[x] =0
    print()
    for i in range(l , r + 1):
        if cnt2[i] != 0:
            print(i , cnt2[i])
    s1 ,s2 , vt1 , vt2 = 0 , 0 , 0 , 10 **18 
    print()

    for i in range(l , r + 1):
        if cnt2[i] >= vt1:
            vt1 , s1 = cnt2[i] , i

    for i in range(l , r +1):
        if cnt2[i] != 0 and cnt2[i] < vt2:
            vt2 , s2 = cnt2[x] , i
    print()
    print(s1)
    print(s2)
