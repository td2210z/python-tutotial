


def check(a , b):
    if b == 0: return 1
    tmp = check( a, b // 2)
    if b % 2 == 1:
        return tmp * tmp * a % (10 ** 9 + 7)
    else:
        return tmp * tmp % (10 ** 9 + 7)

if __name__ == '__main__':
    a , b = map(int , input().split())
    print(check(a , b))
    