import random

num_doubles = 0 

for _ in range(100):
   die1 = random.randint(1, 6) 
   die2 = random.randint(1, 6)
   if die1 == die2: 
       num_doubles += 1

print('Out of 100 you rolled', num_doubles, 'doubles')
