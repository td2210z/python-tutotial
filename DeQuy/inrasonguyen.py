


from math import *

def in1(n):
    if n < 10:
        print(n , end = ' ')
        return 
    in1(n // 10)
    print(n % 10 , end = ' ')


def in2(n):
    if n < 10:
        print(n , end = ' ')
        return 
    print(n % 10 , end = ' ')
    in2(n//10)


if __name__ == '__main__':
    n = int(input())
    in1(n)
    