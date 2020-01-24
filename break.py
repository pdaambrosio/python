#/usr/bin/python

x=1
lista=[]

while True:
	lista += [x]
	x += 1
	if x > 20:
		break
print(lista)
