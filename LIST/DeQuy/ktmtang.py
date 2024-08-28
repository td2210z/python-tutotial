


def check(a , n):
    if n == 1:
        return True
    else:
        if a[n-1] <= a[n-2]:
            return False
        else:
            return check(a , n-1)



if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    if check(a , n):
        print("YES")
    else:
        print("NO")