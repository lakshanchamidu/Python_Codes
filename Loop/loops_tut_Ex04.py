total = 0

for i in range(5): 
   n = input("Please enter a number: ")
   try:
       n = int(n) 
       total += n
   except ValueError: 
       print("Requires a valid integer! Please try again.")

print("The total of the numbers entered is", total)
