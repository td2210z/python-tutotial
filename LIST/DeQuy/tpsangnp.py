

def chuyen(n):
    if n != 0:
        chuyen(n // 2)
        print(n % 2 , end = '')

if __name__ == '__main__':
    
    n = int(input())
    chuyen(n)