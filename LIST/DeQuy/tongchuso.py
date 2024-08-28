



def dem(n):
    if n < 10:
        return 1
    return n % 10 + dem(n //10 )


if __name__ == '__main__':
    n = int(input())
    print(dem(n))