even_number = 0 
odd_number = 0
positive = 0 
negative = 0

for i in range(5):
    number = int(input())
    if number % 2 == 0:
        even_number += 1
    else:
        odd_number += 1

    if number > 0:
        positive += 1  
    elif number < 0:
        negative += 1

print('{} valor(es) par(es)'.format(even_number))
print('{} valor(es) impar(es)'.format(odd_number))
print('{} valor(es) positivo(s)'.format(positive))
print('{} valor(es) negativo(s)'.format(negative))
