


def fibo3(n):
    f1 , f2 = 1 , 0
    for i in range(2 , n):
        fn = f1 + f2
        if fn >= n: return fn
        f2 , f1 = f1 , fn
    return -1

if __name__ == '__main__':
    n = int(input())
    print(fibo3(n))