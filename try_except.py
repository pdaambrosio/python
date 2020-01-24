def ask():
   while True:
      try:
         n = int(input('Input an integer: '))
         print('Thanks, your number squared is: ', n**2)
         break
      except:
         print('An error occurred! Please try again!')
         continue

ask()
