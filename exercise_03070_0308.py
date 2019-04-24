# A drunk pirate makes a random turn and then takes 100 steps forward, makes another 
# random turn, takes another 100 steps, turns another random amount, etc. A social 
# science student records the angle of each turn before the next 100 steps are taken. 
# Her experimental data is [160, -43, 270, -97, -43, 200, -940, 17, -86]. 
# (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our 
# drunk friend.

import turtle                # so we can use the turtle module
wn = turtle.Screen()         # create a screen for the turtles
pirate = turtle.Turtle()     # create a turtle, assign to pirate

data = [160, -43, 270, -97, -43, 200, -940, 17, -86] # assign experimental data to data

for i in data:
    pirate.left(i)       # positive angles are counter-clockwise so use left()
    pirate.forward(100)
    
wn.mainloop()                # wait for user to close window

# Enhance your program above to also tell us what the drunk pirate’s heading is after 
# he has finished stumbling around. (Assume he begins at heading 0).

total = 0 # assign zero to total

# use a for loop to add up all angles
for i in data:        
    total = total + i
    
# to get the direction the drunk pirate is heading use modulo    
direction = total % 360 

print("The drunk pirate is heading after" + str(direction) + " degrees.")


