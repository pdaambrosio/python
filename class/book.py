#/usr/bin/python

class book (object):
   def __init__(self, title, author, pages):
     print ('The book was created.')
     self.title = title
     self.author = author
     self.pages = pages

   def __str__(self):
     return 'Title {a}'.format(a=self.title)

   def __len__(self):
     return self.pages

   def __del__(self):
     print ('Book deleted')
