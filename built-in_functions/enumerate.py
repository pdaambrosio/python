#Method_1

l=['a', 'b', 'c', 'd', 'e', 'f']
c=0

for i in l:
    print(c, ':' ,i)
    c+=1

#Method_2

for n in enumerate(l):
    print(n)

for m, o in enumerate(l):
    print(m, ':' ,o)
