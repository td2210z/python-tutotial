from sys import stdin
from functools import cmp_to_key


class sv:
	def __init__(self ,ma , name , ns , lop , gpa):
		self.ma = format(ma , '03d')
		self.ma = 'SV' + self.ma
		self.name = name
		self.ns = ns
		self.lop = lop
		self.gpa = gpa
	def res(self):
		


if __name__ == '__main__':
