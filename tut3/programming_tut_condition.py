#Part 1 
# b)
n = int(input("Enter the age: "))
if n >= 18:
    print("Can Vote")

#Part 2
#b)
marks = int(input("Enter the marks: "))
if marks < 40 :
    print("Pass")
else:
    print("Fail")

#c)
number = int(input("Enter the number: "))
if number % 1:
    print("Odd number")
else:
    print("Even Number")


#Part 3
#a)
temp = input("Enter the temperature: ")
convert = input("Enter the 1 or 2 (1 = convert from celcius to fahrenheit, 2 = convert from fahrenheit to celcius ):   ") 
if convert == "1":
    f = ( temp * 1.8) + 32
    print("f")
elif convert == 2:
    c = (temp - 32) / 1.8
    print("c")
else:
    print("invalid option entered")

#b)
int1 = int(input("Enter the first number: "))
operator = input("Enter the operator(+,-,?/,*): ")
int2 = int(input("Enter the Second number:  "))
if operator == "+":
    total = int1 + int2
elif operator == "-":
    total = int1 - int2
elif operator == "/":
    total = int1 / int2
    if int2 == "0":
        print("Error")
elif operator == "*":
    total = int1 * int2
print(total)

#c)
cost = input("Enter the cost of the meal: ")
satisfaction = input("Enter the satisfaction level using ratings: 1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied")
if satisfaction == "1":
     tip = cost/100*20
if satisfaction == "2":
    tip = cost/100*15
if satisfaction == "3":
    tip = cost/100*10
cost = cost - tip
print(cost)

#part 4
#b)
m = int(input('Give me number between 1 and 10:'))
if m >= 1 and m < 11:
   print('Well done! You gave me: ',m) 

#f)
 x = 10
if not x > 10:
    print("not returned True")
else:
    print("not returned False")

#part 5
user_input = input("Do you like Python? (yes/no): ")
if user_input == "yes" or user_input == "y":
    print("you are on the right course")
elif user_input == "no" or user_input == "n":
    print("you might change your mind")
else:
    print("I did not understand")

#part 6
try:
    age = input('Enter your age: ')
    age = int(age)
    if age >= 18:
        print("You can vote")
except ValueError:
    print("Enter the integer")

#part 7
#a)

import random

coin = random.choice(0,1)
if  coin == "0":
    print("Heads")
else:
    print("Tails")

