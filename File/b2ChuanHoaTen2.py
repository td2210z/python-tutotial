f1 = open("input.txt" , "r")
f2 = open("output.txt" ,"w")

tmp= ''
data = f1.read()
a = []
for j in range(len(data)):
	if data[j] != ',':
		tmp += data[j]
	else:
		a.append(tmp)
		tmp =''
a.append(tmp)

for x in a:
	tmp = x.split()
	res = ' '.join(tmp).title()
	f2.write(res + ',')
f1.close()
f2.close()

