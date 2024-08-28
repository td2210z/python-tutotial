def fibo(n):
    if  n == 1: return True
    f1 , f2 = 1 , 1
    for i in range(2 , 23):
        fn = f1 + f2
        if fn == n: return True
        f2 , f1 = f1 , fn
    return False




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if fibo(n):
            print("YES")
        else:
            print("NO")
        
    