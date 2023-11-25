# Initialization
secret = 'water'
turns = len(secret)
guesses = ''


print("Let's play Guess the Word")
print(f"You have {turns} turns to guess the word!")
print('_ ' * len(secret))


while turns > 0:
 guess = input('Guess a letter: ')
 guess = guess.lower() 
 if guess in secret:
     guesses += guess
     for letter in secret:
         if letter in guesses:
             print('', letter, '', end='')
         else:
             print(' _ ', end='')
 else:
     print('Incorrect guess. Try again.')
     turns -= 1
     print(f"You have {turns} turns left.")


 if ''.join(guesses) == secret:
     print('Congratulations, you won!')
     break


print('End of Game')