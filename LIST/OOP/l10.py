class chung:
    def __init__(self, ma, ten, hang, masac):
        self.ma = ma
        self.ten = ten
        self.hang = hang
        self.masac = masac

    def __str__(self):
        return self.ma + ' ' + self.ten + ' ' + self.hang + ' ' + self.masac

    def get_ten(self):
        return self.ten


class xemay(chung):
    def __init__(self, ma, ten, hang, masac, tocdo, gia):
        super().__init__(ma, ten, hang, masac)
        self.tocdo = tocdo
        self.gia = gia

    def __str__(self):
        return super().__str__() + ' ' + str(self.tocdo) + ' ' + str(self.gia)
    def get_gia(self):
        return self.gia


class oto(chung):
    def __init__(self, ma, ten, hang, masac, maluc, gia):
        super().__init__(ma, ten, hang, masac)
        self.maluc = maluc
        self.gia = gia

    def __str__(self):
        return super().__str__() + ' ' + str(self.maluc) + ' ' + str(self.gia)
    def get_gia2(self):
        return self.gia

if __name__ == '__main__':
    n = int(input())
    res1, res2 = [], []
    for i in range(n):
        ma = input()
        ans = ma[:2]
        if ans == 'OT':
            ten = input()
            hang = input()
            masac = input()
            maluc = int(input())
            gia = int(input())
            p = oto(ma, ten, hang, masac, maluc, gia)
            res1.append(p)
        else:
            ten = input()
            hang = input()
            masac = input()
            tocdo = int(input())
            gia = int(input())
            z = xemay(ma, ten, hang, masac, tocdo, gia)
            res2.append(z)
    cd = input()
    print('DANH SACH OTO :')
    for x in res1:
        if x.get_ten() == cd:
            print(x)
    print('DANH SACH XE MAY :')
    for x in res2:
        if x.get_ten() == cd:
            print(x)