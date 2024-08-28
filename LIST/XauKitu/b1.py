


if __name__ == '__main__':
    s = input()
    cnt1 , cnt2 = 0 , 0
    for x in s:
        if x.isdigit():
            cnt1 += 1
        elif x.isalpha():
            cnt2 += 1
    print(cnt1 , cnt2 , len(s) - cnt1 -cnt2)

