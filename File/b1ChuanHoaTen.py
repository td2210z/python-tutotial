

f1 = open("input.txt" , "r")
f2 = open("output.txt" , "w")

for x in f1:
	res = x.split()
	ans = ' '.join(res).title()
	f2.write(ans+ '\n')
f1.close()
f2.close()
