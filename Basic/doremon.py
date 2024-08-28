a , b = map(int , input().split())


x , y = 0 , a

if a % 2 == 0:
    x = a // 2
else:
    x = a // 2 + 1


ans = (x + b - 1) // b * b
if ans <= y:
    print(ans)
else:
    print(-1)