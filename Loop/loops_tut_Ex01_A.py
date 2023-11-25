hidden = 6
guess = int(input("Enter a guess (number between 1 and 20): "))
while guess != hidden:
   print("Guess is not correct")
   guess = int(input("Enter a guess (number between 1 and 20): "))
print("Your guess was correct")


