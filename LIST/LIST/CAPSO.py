


from math import *




if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    k = int(input())
    cnt =0
    for i in range(0 , len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == k:
                cnt += 1
    print(cnt)
    
    

    