


from math import *




if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    b = []
    ok = False
    for i in range(n):
        if i % 2 == 0 and a[i] % 2 == 0:
            print(a[i] , end= ' ')
            ok = True
    
    if not ok:
        print("NONE")
    
    

    