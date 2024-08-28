
from math import *

class sv1:
	def __init__(self , masv , name , lop , ns , gpa):
		self.masv = masv
		self.name = name
		self.lop = lop
		self.ns = ns
		self.gpa = gpa
	def chuan_hoa(self):
	    if self.ns[1] == '/':
	       self.ns = '0' + self.ns
	    if self.ns[4] == '/':
	       self.ns = self.ns[0:3] + "0" + self.ns[3:]
	def __str__(self):
		return f'{self.masv} {self.name} {self.lop} {self.ns} {self.gpa:.1f}'



if __name__ == '__main__':
	name = input()
	lop = input()
	ns = input()
	gpa = float(input())
	s = sv1('SV001' , name , lop , ns , gpa)
	s.chuan_hoa()
	print(s)