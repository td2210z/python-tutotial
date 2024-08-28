
from math import *

class sv:
	def __init__(self , name , ns , a , b , c):
		self.name = name
		self.ns = ns
		self.a = a
		self.b = b
		self.c = c
	
	def __str__(self):
		tong = a + b + c
		return f'{self.name} {self.ns} {tong:.1f}'
if __name__ == '__main__':
	name = input()
	ns = input()
	a = float(input())
	b = float(input())
	c = float(input())
	ress = sv(name , ns , a , b , c)
	print(ress)