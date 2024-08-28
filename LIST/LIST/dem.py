




if __name__ == '__main__':
    n = int(input())
    cnt1 =0
    cnt2 =0
    tong1 =0
    tong2 =0
    a = list(map(int , input().split()))
    for i in a:
        if i % 2 == 0:
            cnt1 += 1
            tong1 += i
        else: 
            tong2 += i
            cnt2 += 1
    

    print(cnt1)
    print(cnt2)
    print(tong1)
    print(tong2)
