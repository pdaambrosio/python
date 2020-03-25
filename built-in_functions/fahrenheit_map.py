#Method_1

#Lambda
def fahrenheit (T):
    return (9/5) * T + 32

temp=[9, 22, 40, 90, 120]

for t in temp:
    print (fahrenheit(t))

#Method_2_without_for

l=list(map(fahrenheit, temp))
print (l)

#Method_3_within_lambda

l2=list(map(lambda t:(9/5)*t + 32, temp))
print (l2)




