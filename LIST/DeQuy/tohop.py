


def th(n , k):
    if n == k or k == 0:
        return 1
    return th(n-1 , k-1) + th(n-1 , k)


if __name__ == '__main__':
    n ,k = map(int , input().split())
    print(th(n ,k))