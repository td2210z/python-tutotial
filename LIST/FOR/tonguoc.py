from math import *

n = int(input())

sum =0
for i in range(1 , isqrt(n)):
    if n % i == 0:
        sum += i
        if i != n // i: sum += n // i

print(sum)