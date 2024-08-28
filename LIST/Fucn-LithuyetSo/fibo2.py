

def fibo2(n):
    if n == 0 or n == 1: return True
    f1 , f2 , fn= 1 , 0 , 0
    for i in range(2 , n):
        fn = f1 + f2
        if fn == n: return True
        f1 , f2 = f2 , fn
    return False

if __name__ == '__main__':
    n = int(input())
    if fibo2(n):
        print("YES")
    else:
        print("NO")