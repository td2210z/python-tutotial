


from functools import cmp_to_key


class sv:
	def __init__(self , ma , name , ns , lop , gpa):
		self.ma = str(ma)
		while len(self.ma) < 3:
			self.ma = '0' + self.ma
		self.ma = 'SV' + self.ma
		self.name = name
		self.ns = ns
		self.lop = lop
		self.gpa = gpa
	def read1(self):
		if self.ns[1] == '/':
			self.ns = '0' + self.ns
		if self.ns[4] == '/':
			self.ns = self.ns[0:3] + '0' + self.ns[3:]
		res = self.name.split()
		ans = ' '.join(res).title()
		self.name = ans
	def __str__(self):
		return f'{self.ma} {self.name} {self.lop} {self.ns} {self.gpa:.2f}'


if __name__ == '__main__':
	n = int(input())
	a = []
	for i in range(n):
		p = sv(i + 1, input() , input() , input(), float(input()))
		p.read1()
		a.append(p)
	a.sort(key  = lambda x : -x.gpa)
	for x in a:
		print(x)
	
