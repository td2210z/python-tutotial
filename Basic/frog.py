

a , b , k = map(int , input().split())


l , r =0 , 0

if k % 2 == 0:
    l = k // 2
    r = k // 2
else:
    l = k // 2
    r = l + 1

print(r * a - l * b)