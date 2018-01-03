'''Make a program that does the following:
    a. Prints something
    b. Assigns a variable
    c. Performs a math function
    d. Uses an if statement
'''
#user="Drew"

#years="42"

tupA = ("Drew", "42")

userAge= tupA[0] + "\'s age is " + tupA[1] + " years old."

print userAge

if int(tupA[1]) > 40:
    print tupA[0] + " is getting old!"

dogYears = int(tupA[1]) * 7

print "That is " + str(dogYears) + " in dog years."
