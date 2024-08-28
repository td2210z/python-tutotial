

def loc_phat(n):
    while n != 0:
        res = n % 10
        if (not(res == 0 or res == 8 or res == 6)):return False
        n //= 10
    return True


if __name__ == '__main__':
    n = int(input())
    if loc_phat(n):
        print("1")
    else:
        print("0")
