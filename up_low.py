# Escreva uma função Python que aceita uma string e calcule o número de maiúsculas e minúsculas.


def up_low(s):
  up=0
  low=0
  for i in s:
    if i.isupper():
      up+=1
      print('Number of uppercase characters:'+up)
    elif i.islower:
      low+=1
      print('Number of lowercase characters:'+low)
    else:
      pass

up_low('Teste')

#print('Number of lowercase characters:'+low)
#print('Number of uppercase characters:'+up)
