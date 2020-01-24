# Escreva uma função Python que recebe uma lista e retorna uma nova lista com elementos exclusivos da primeira lista.

unique_list=([1,1,1,1,2,2,3,3,3,3,4,5])

def unique_list(l):
   return list(set(l))

print(unique_list)
