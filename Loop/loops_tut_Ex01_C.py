import random
hidden = random.randint(1, 20)
print("Hidden number:", hidden)
guess = int(input("Enter a guess (number between 1 and 20): "))
while guess != hidden:
   if guess < hidden:
       print("Guess is too low")
   else:
       print("Guess is too high")
   guess = int(input("Enter a guess (number between 1 and 20): "))
print("Your guess was correct")
