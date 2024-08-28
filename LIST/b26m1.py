from math import *



if __name__ == '__main__':
    n = int(input())

    a = list(map(int , input().split()))
    
    cnt = [0] * 1000001
    
    for x in a:
        cnt[x] += 1
    
    dem = 0
    for x in a:
        if cnt[x] != 0:
            dem += 1
            cnt[x] = 0
    print(dem)