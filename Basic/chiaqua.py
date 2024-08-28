a,b,c, n = map(int , input().split())

if (n + a + b + c) % 3 == 0:
    tm = (n + a + b + c) // 3
    if tm >= a and tm >= b and tm >= c:
        print("YES")
    else:
        print("NO")
else:
    print("NO")