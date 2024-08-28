import math

def th(n , k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

if __name__ == '__main__':
    n , k = map(int , input().split())
    print(int(th(n , k)))