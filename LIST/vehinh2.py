n = int(input())

for i in range(1 , n +1):
    for j in range(i):
        print("*" , end = '')
    print()

print()
#hinh2 
for i in range(n , 0 , -1):
    for j in range(i):
        print("*" , end ='')
    print()

print()

for i in range(1 , n +1):
    for j in range(1 , n +1):
        if j <= n -i:
            print(" " , end = '')
        else: 
            print("*" , end = '')
    print()

print()
#hinh4

for i in range(1 , n +1):
    for j in range(1 , n +1):
        if j < i:
            print(" " , end = '')
        else:
            print("*" , end= '')
    print()
print()
# hinh 5

for i in range(1 , n +1):
    for j in range(1 , i +1):
        if i ==1 or j ==1 or i == n or j == i:
            print("*" , end = '')
        else:
            print(" " ,end = '')
    print()