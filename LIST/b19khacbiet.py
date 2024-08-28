from math import *


if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    ans = 10**9 + 7
    for i in range(0 , len(a)):
        for j in range(i + 1, len(a)):
            ans = min(ans , abs(a[i] - a[j]))
    print(ans)