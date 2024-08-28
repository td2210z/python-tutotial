from math import *



if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    cnt = [0] * 1000
    for x in a:
        cnt[x] += 1

    for x in a:
        if cnt[x] != 0:
            print(x , end= ' ')
        cnt[x] = 0
    
    

    