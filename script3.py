'''
Create a program that contains the following:

1. Multiplies a number to the power of another number
2. An if, elif and else statement
3. A for loop
4. A while loop
5. A dictionary
'''
number = 5

print "The number starts with a value of " + str(number)

print "Next, we will change the value of the number by cubing it, i.e. x to the 3rd power"

number = number**3

if number > 125:
    print "The number is greater than 125"
elif number <= 5:
    print "The number is less than or equal to 5"
else:
    print "Now the number is " + str(number)

print "Next, we'll change the value of the number by using a for loop"

for number in range(125, 1500, 100):
    print number

print "Now, we'll change the value of the number by using a while loop"

while number < 1500:
    number += 10
    print number

print "The final value of the number is " + str(number)    

print "Finally, we'll create a dictionary and then print the value of one of the key-value pairs"

my_dictionary = {'user1': 'me', 'user2': 'you'}

print "For the key 'user 1', the value is " + my_dictionary['user1']



    
