n = int(input())

dem =1
for i in range(1 , n +1):
    for j in range(1 , n +1):
        print(dem , end = ' ')
        dem += 1
    print()

print()

for i in range(1 , n +1):
    kt = i
    for j in range(1 , n +1):
        print(kt , end = ' ')
        kt += 1
    print()

print()

for i in range(1 , n +1):
    for j in range(1 , n+1):
        if j <= n -i:
            print("~" , end = '')
        else:
            print(i , end = '')
    print()

print()

for i in range(1 , n +1):
    kt = i
    kc = n-1
    for j in range(1 , i+1):
        print(kt , end = ' ')
        kt += kc
        kc -= 1
    print()

