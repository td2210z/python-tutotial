'''
print("xin chao anh em")

'''

#a = 100 day la chu thich

# kieu du lieu
# s = '1234'

# a = int(s)
# print(type(s))
# print(a)



# toan tu gan = 
'''
s = 'thang123 ok1234'   ham in tiem kiem 
print('thang123'  in(s)) ''' 

# ham nhap xuat
'''
a = int(input('xin nhap so '))
print(type(a))
print('so vua nhap se la ' , a)'''

# nhap nhieu so 

# x , y , z = map(int , input().split())

# print(x + y + z)

# from math import *

# print('xin chao')



# if else 

# a = 10
# b = 20   shotif


# if a < b: print(a , 'nho hon ' , b)


# toán tử 3 ngôi 
# vảr = statement if conditon else statement



from math import *;

n = int(input())

if n % 2 ==0:
    print("YES")
else:
    print("NO")


if n % 3 == 0 and n % 5 == 0:
    print("YES")
else:
    print("NO")


if n % 3 ==0 and n % 7 != 0:
    print("YES")
else:
    print("NO")

if n % 3 == 0 or n % 7 == 0:
    print("YES")
else:
    print("NO")


if n > 30 and n < 50:
    print("YES")
else:
    print("NO")

if (n >= 30) and (n % 2 == 0 or n % 3 == 0 or n % 5 ==0):
    print("YES")
else:
    print("NO")

res = n % 10
if  (n >= 10) and  n <= 90 and (res == 2 or res == 5 or res == 3 or res == 7):
    print("YES")
else:
    print("NO")


if (n <= 100) and (n % 23 == 0):
    print("YES")
else:
    print("NO")

if  n < 10 or n > 20:
    print("YES")
else:
    print("NO")


if res % 3 == 0:
    print("YES")
else:
    print("NO")