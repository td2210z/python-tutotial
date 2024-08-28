



def in1(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n % 10 + in1(n//10)
    else: return in1(n//10)

def in2(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return n % 10 + in2(n // 10)
    else: return in2(n// 10)

if __name__ == '__main__':
    n = int(input())
    print(in1(n))
    print(in2(n))
    