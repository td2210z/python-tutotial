from math import *

fibo = [0] * 100

def kt():
    fibo[0] = 0
    fibo[1] =1
    for i in range(2 , 100):
        fibo[i] = fibo[i-1] + fibo[i-2]


if __name__ == '__main__':
    

    n = int(input())
    a = list(map(int , input().split()))
    kt()
    ok = False
    for x in a:
        if x in fibo:
            print(x , end = ' ')
            ok = True
    
    if not ok:
        print("NONE")
    

    