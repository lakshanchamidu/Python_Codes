import random
hidden = random.randint(1, 20)
print("Hidden number:", hidden)
guess = int(input("Enter a guess (number between 1 and 20): "))
while guess != hidden:
   print("Guess is not correct")
   guess = int(input("Enter a guess (number between 1 and 20): "))
print("Your guess was correct")
