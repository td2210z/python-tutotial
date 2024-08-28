


def gdc(a , b):
    if b == 0:
        return a
    return gdc(b , a % b)

def lcm(a , b):
    return a * b // gdc(a , b)
if __name__ == '__main__':
    a , b = map(int , input().split())
    print(gdc(a , b) , lcm(a , b))