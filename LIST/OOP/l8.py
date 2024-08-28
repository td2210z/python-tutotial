class chung:
    def __init__(self, ma, ten, hang, masac):
        self.ma = ma
        self.ten = ten
        self.hang = hang
        self.masac = masac

    def __str__(self):
        return self.ma + ' ' + self.ten + ' ' + self.hang + ' ' + self.masac

    def get_ma(self):
        return self.ma


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
    
    print('DANH SACH OTO :')
    res1.sort(key = lambda x : (-x.get_gia2() , x.get_ma()))
    for x in res1:
        print(x)
    print('DANH SACH XE MAY :')
    res2.sort(key = lambda x : (-x.get_gia() , x.get_ma()))
    for x in res2:
        print(x)