a , b , n = map(int , input().split())

check = False
for i in range(0 , n // a+ 1):
    tmp = n - a  * i
    if tmp % b == 0:
        check = True
        break

if check:
    print("YES")
else:
    print("NO")

