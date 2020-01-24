# Escreva uma função que verifica se um número está em um determinado intervalo (inclusive o máximo e mínimo)

def ran_check(num,low,high):
   if num in list(range(low,high+1)):
     print (" %s is in the range" %str(num))
   else:
     print ("The number is outside the range")
