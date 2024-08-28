
def uc(a , b):
    while b != 0:
        a , b = b , a % b
    return a

def lcm(a , b):
    return a * b // uc(a , b)


if __name__ == '__main__':
    a , b = map(int , input().split())

    print(uc(a , b) , lcm(a , b))