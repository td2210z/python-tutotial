n = int(input())

cnt =0
while n != 0:
    res = n % 10
    if (res == 2 or res == 3 or res == 5 or res == 7): cnt += 1
    n //= 10

print(cnt)