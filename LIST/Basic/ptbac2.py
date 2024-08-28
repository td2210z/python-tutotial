from math import *

a , b , c = map(int , input().split())



if a == 0 and b == 0 and c == 0:
    print("VO SO NGHIEM")
elif b == 0 and c == 0:
    print("VO NGHIEM")
elif a == 0:
    print(-c/b)
else:
    delta = b*b - 4*a*c
    if(delta < 0) : print("VO NGHIEM")
    elif(delta == 0) : print((float) -b / 2 *a)
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print('%.2f' % x1 , '%.2f' % x2)
         