def start():
    food = raw_input('What is your favorite food?').lower()
    food_quantity = int(raw_input('How many time a week do you eat your favorite food?'))
    if food_quantity > 1:
        print "Wow, you really love "  + food + " !"
    elif food_quantity == 1:
        print "Not bad."
    else:
        print "Are you sure that you love " + food + " ?"
        
start()    
    
