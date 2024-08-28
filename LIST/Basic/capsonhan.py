a , b, c ,d = map(int , input().split())


if b % a == 0:
    p = b // a
    if b * p == c and c * p == d:
        print("YES")
    else:
        print("NO")
else:
    print("NO")