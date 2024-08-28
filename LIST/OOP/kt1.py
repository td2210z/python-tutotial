class person:
    def __init__(self, ten, ns, dc):
        self.ten = ten
        self.ns = ns
        self.dc = dc

    def ce1(self):
        self.ten = self.ten.title()
        if self.ns[1] == '/':
            self.ns = '0' + self.ns
        if self.ns[4] == '/':
            self.ns = self.ns[0:3] + "0" + self.ns[3:]

    def __str__(self):
        return self.ten + ' ' + self.ns + ' ' + self.dc


class student(person):
    def __init__(self, ma, ten, ns, dc, lop, gpa):
        person.__init__(self, ten, ns, dc)
        self.ma = format(ma, '04d')
        self.gpa = gpa
        self.lop = lop

    def __str__(self):
        return self.ma + ' ' + person.__str__(self) + ' ' + self.lop + ' '+ '{:.2f}'.format(self.gpa)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        ten = input()
        ns = input()
        lop = input()
        gpa = float(input())
        pos = 0
        for j in range(len(ns)):
            if ns[j].isalpha():
                pos = j
                break
        dc = ns[pos:]
        ns = ns[:pos]
        s = student(i + 1, ten, ns , dc , lop , gpa)
        s.ce1()
        print(s)
