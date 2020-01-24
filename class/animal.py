#/usr/bin/python

### heritage

class tested (object):
   def __init__(self):
     print ('Print tested created')

   def whoAmI (self):
     print ('I am i')

   def eat (self):
     print ('Eating')

class test2 (tested):
   def __init__(self):
     test2.__init__(self)
     print ('test2 created')

   def whoAmI2 (self):
     print ('I am test2')

   def walk (self):
     print ('walking')
