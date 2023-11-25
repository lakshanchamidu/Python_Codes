print("part A=================================================================================")
for number in range(3) :
	print("-------------------------------------------")
	print("Outer loop iteration " + str(number))
# Inner loop
for another_number in range(4):
	print("****************************")
	print("In inner loop iteration " + str(another_number))

print("part B=================================================================================")
for x in range(1,4):
    for y in range(1,4):
        print('*', end='')
    print()


print("part C=================================================================================")
for x in range(1, 4):
   for y in range(1, x+1): 
       print('*', end='')
   print()

