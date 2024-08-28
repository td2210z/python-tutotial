class hs:
    def __init__(self, name, email, sdt, toan, li, hoa):
        self.name = name
        self.email = email
        self.sdt = sdt
        self.toan = toan
        self.li = li
        self.hoa = hoa
    
    def get_diem(self):
        return self.toan + self.li + self.hoa
    
    def to_string(self):
        return self.name + '\n' + self.email + '\n' + self.sdt + '\n' + str(self.toan + self.li + self.hoa) + '\n'


f1 = open("input.txt", "r")
f2 = open("output.txt", "w")

data = []
for x in f1:
    data.append(x[:-1])

a = []
for i in range(0, len(data), 4):
    ten = data[i]
    email = data[i+1]
    sdt = data[i+2]
    toan, li, hoa = map(int, data[i+3].split())
    pos = hs(ten, email, sdt, toan, li, hoa)
    a.append(pos)

a.sort(key=lambda x: -x.get_diem())

for x in a:
    if x.get_diem() >= 27:
        f2.write(x.to_string())

f1.close()
f2.close()
