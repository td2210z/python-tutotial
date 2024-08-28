#in ra 10 so fibo dau tien 

def fibo(n):
    if n == 1: print(1)
    elif n == 2: print('1\n1')
    else:
        print('1\n1')
        f1 ,f2 = 1 , 1
        fn = 0
        for i in range(2 , n):
            fn = f1 + f2
            print(fn)
            f1 , f2 = f2 , fn

if __name__ == '__main__':
    n = int(input())
    fibo(n)