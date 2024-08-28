


def check(a , n):
    if n >= 1:
        if a[n-1] % 2 == 1:
            return False
        else:
            return check(a , n-1)
    else:
        return True



if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    if check(a , n):
        print("YES")
    else:
        print("NO")