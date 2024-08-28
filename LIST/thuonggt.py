
import math
n = int(input())
res = 0

for i in range(n):
    res += 1 / math.factorial(i)

print('%.4f' % res)


