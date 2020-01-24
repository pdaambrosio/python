#/usr/bin/python

class circle(object):
   pi=3.14
   def __init__(self, raio=1):
     self.raio = raio

   def area(self):
     return self.raio ** 2 * self.pi

   def defRaio(self, raio):
     self.raio = raio
 
   def obtainRaio(self):
     return self.raio
