



class sv:
	def __init__(self ,ma, name , lop , ns , gpa):
		self.ma = str(ma)
		while len(self.ma) < 3:
			self.ma = '0' + self.ma
		self.ma = 'SV' + self.ma
		self.name = name
		self.lop = lop
		self.ns = ns
		self.gpa = gpa
	def chuan_hoa2(self):
		if self.ns[1] == '/':
			self.ns = '0' + self.ns
		if self.ns[4] == '/':
			self.ns = self.ns[0:3] + '0' + self.ns[3:]
	def __str__(self):
		return f'{self.ma} {self.name} {self.lop} {self.ns} {self.gpa:.2f}'





if __name__ == '__main__':
	n = int(input())
	a = []
	for i in range(n):
		ps = sv(i + 1, input() , input() , input(), float(input()))
		ps.chuan_hoa2()
		a.append(ps)
	for x in a:
		print(x)
	