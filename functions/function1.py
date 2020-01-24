def is_prime (num):
   """
   Check if this number is prime.
   """
   for n in range(2,num):
     if num % n==0:
       return('no prime')
       break
   else: # if this module never equals zero, it is prime
       return('prime')

t=is_prime(7)

print(t)
