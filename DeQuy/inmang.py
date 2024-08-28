


def check(a , n):
    if n >= 1:
        print(a[n-1] , end= ' ')
        check(a ,n -1)

def check2(a , n):
    if n >= 1:
        check2(a , n -1)
        print(a[n-1] , end=' ')

if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    check(a , n)
    print()
    check2( a, n)