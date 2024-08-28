


from math import *




if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    x = int(input())
    cnt1 , cnt2 = 0 , 0
    for i in a:
        if i < x:
            cnt2 += 1
        if i > x:
            cnt1 += 1
    print(cnt2)
    print(cnt1)
    

    