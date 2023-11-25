while True:
   n = input("Please enter an integer: ")
   try:
       n = int(n)
       break 
   except ValueError:
       print("Requires a valid integer! Please try again.")
print("You successfully entered an integer.")
