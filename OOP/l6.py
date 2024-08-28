

class gb1:
	def __init__(self , ma , ten , ns , dc):
		self.ma = ma
		self.ten = ten
		self.ns = ns
		self.dc = dc
	def per_mu(self):
		self.ten =self.ten.title()
		if self.ns[1] == '/':
			self.ns = '0' + self.ns
		if self.ns[4] == '/':
			self.ns = self.ns[0:3] + '0' + self.ns[3:]
	def get_dc(self):
		return self.ma
	def __str__(self):
		return self.ma + ' ' + self.ten + ' ' + self.ns + ' ' + self.dc


class gv1(gb1):
	def __init__(self , ma , ten , ns , dc , khoa , luong , lop):
		gb1.__init__(self , ma , ten , ns , dc)
		self.khoa = khoa
		self.luong = luong
		self.lop = lop
	def __str__(self):
		return gb1.__str__(self) + ' ' + self.khoa + ' ' + str(self.luong) + ' ' + self.lop
	def get_luong(self):
		return self.luong
	def lay_lp(self):
		return self.lop



class sv1(gb1):
    def  __init__(self , ma , ten , ns , dc , lop , gpa):
    	gb1.__init__(self , ma , ten , ns , dc)
    	self.lop = lop
    	self.gpa = gpa
   
    def __str__(self):
    	return gb1.__str__(self) + ' ' + self.lop + ' ' + '{:.2f}'.format(self.gpa)
    def get_gpa(self):
    	return self.gpa
   def lay_lp2(self):
		return self.lop	


if __name__ == '__main__':
	n = int(input())
	res1 , res2 = [] , []
	for i in range(n):
		ma = input()
		ans = ma[:2]
		if ans =='GV':
			ten = input()
			ns = input()
			dc = input()
			khoa = input()
			luong = int(input())
			lop = input()
			p = gv1(ma , ten , ns , dc , khoa , luong , lop)
			p.per_mu()
			res1.append(p)
		else:
			ten = input()
			ns = input()
			dc = input()
			lop= input()
			gpa = float(input())
			z = sv1(ma , ten , ns , dc , lop , gpa)
			z.per_mu()
			res2.append(z)
	ans = input()
	print('DANH SACH GIAO VIEN PHU TRACH LOP ' + res + ' :')
	for x in res1:
		if x.lay_lp() == ans:
			print(x)
	print('DANH SACH SINH VIEN PHU TRACH LOP ' + res + ' :')
	for x in res2:
		if x.lay_lp2() == ans:
			print(x)

