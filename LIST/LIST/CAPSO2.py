


from math import *




if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    cnt = 1001
    for i in range(0 , len(a)):
        for j in range(i + 1, len(a)):
            cnt = min(cnt , abs(a[i] - a[j]))
    print(cnt)
    
    

    