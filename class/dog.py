class Dog(object):
   species = 'mamífero'
   def __init__(self,raça,nome):
     self.raça = raça
     self.nome = nome
     self.num = len(self.species)

   def latir(self):
     print("Au Au")

class animal(Dog):
   def __init__(self):
     animal.__init__(self)
     print("Animal criado...")

gary = Dog('Pug','Gary')

print('Nome:', gary.nome, '| Raça:', gary.raça, '| Especie:',gary.species, '| Num:',gary.num)
print(gary.latir())
