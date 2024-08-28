

def chuyen(n):
    if n != 0:
        chuyen(n // 16)
        r = n % 16
        if r < 10:
            print(r , end= '')
        else:
            print(chr(r + 55) , end= '')
if __name__ == '__main__':
    
    n = int(input())
    if n == 0: print(")")
    else:
        chuyen(n)