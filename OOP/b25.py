



class nv1:
	def __init__(self , ma , name , gt , ns , dc , mst , nkhd):
		self.ma = format(ma , '05d')
		self.name=  name
		self.gt = gt
		self.ns = ns
		self.dc = dc
		self.mst = mst
		self.nkhd = nkhd
	def read2(self):
		if self.ns[1] == '/':
			self.ns = '0' + self.ns
		if self.ns[4] == '/':
			self.ns = self.ns[0:3] + '0' + self.ns[3:]
		if self.nkhd[1] == '/':
			self.nkhd = '0' + self.nkhd
		if self.nkhd[4] == '/':
			self.nkhd = self.nkhd[0:3] + '0' + self.nkhd[3:]
	def __str__(self):
		return f'{self.ma} {self.name} {self.gt} {self.ns} {self.dc} {self.mst} {self.nkhd}'


if __name__ == '__main__':
	n = int(input())
	a = []
	for i in range(n):
		p = nv1(i+1 , input() , input() , input() , input() , input(), input())
		p.read2()
		a.append(p)
	for x in a:
		print(x)
