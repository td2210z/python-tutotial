
def tn(n):
    rev = 0
    tmp = n
    cnt =0
    sum =0
    ans =0
    while n != 0:
        r = n % 10
        rev = rev * 10 + r
        if (r == 6): ans += 1
        sum += r
        n //= 10
    return ans >= 1 and (sum % 10 == 8) and rev == tmp




if __name__ == '__main__':
    n , m = map(int , input().split())
    for i in range(n , m + 1):
        if tn(i):
            print(i , end = ' ')