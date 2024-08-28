
#nnhapkhi nao gap so duong thi dung 

# while True:
#     n = int(input('nhap so'))
#     if n ==2200 : break


n = int(input())
sum =0
while n != 0:
    sum += n % 10
    n //= 10

print(sum)