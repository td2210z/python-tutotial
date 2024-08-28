
from functools import cmp_to_key

class p1:
	def __init__(self , ten , ns , dc):
		self.ten = ten
		self.ns = ns
		self.dc = dc
	def chuan_hoa(self):
		self.ten = self.ten.title()
		if self.ns[1] == '/':
			self.ns = '0' + self.ns
		if self.ns[4] == '/':
			self.ns = self.ns[0:3] + '0' + self.ns[3:]
	def get_name(self):
		return self.ten
	def __str__(self):
		return self.ten + ' ' + self.ns + ' ' + self.dc


class p2(p1):
	def __init__(self , ma ,ten , ns , dc , lop , gpa):
		p1.__init__(self , ten , ns , dc)
		self.ma = format(ma , '04d')
		self.lop = lop
		self.gpa = gpa
	def __str__(self):
		return self.ma + ' ' + p1.__str__(self) + ' ' + self.lop + ' ' + '{:.2f}'.format(self.gpa)


def ss(s):
	a = s.split()
	res = a[-1] + ' '
	res += ' '.join(a[:-1])
	return res

if __name__ == '__main__':
	n = int(input())
	a = []
	for i in range(n):
		p = p2(i + 1, input() , input() , input() , input() , float(input()))
		p.chuan_hoa()
		a.append(p)
	a.sort(key = lambda x : (ss(x.ten)))
	for x in a:
		print(x)
