#Zip

a=[1, 2, 3, 4, 5]
b=[6, 7, 8, 9, 10]

l=list(zip(a,b))
print (l)

for i in l:
    print(max(i))

c={'a':1, 'b':2, 'c':3}
d={'d':4, 'e':5, 'f':6}

l2=list(zip(c,d))
print (l2)
