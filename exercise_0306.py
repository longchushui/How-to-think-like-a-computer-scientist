# Use for loops to make a turtle draw these regular polygons (regular means all sides the 
# same lengths, all angles the same):
#  An equilateral triangle
#  A square
#  A hexagon (six sides)
#  An octagon (eight sides)

import turtle                # so we can use the turtle module
wn = turtle.Screen()         # create a screen for the turtles
tess = turtle.Turtle()       # create a turtle, assign to tess

# make an equilateral triangle
for i in range(3):
    tess.forward(100)
    tess.left(360/3)         # to lazy to calculate the answer to 360/3


# make a square
for i in range(4):
    tess.forward(100)
    tess.left(360/4)


# make a hexagon (six sides)
for i in range(6):
    tess.forward(100)
    tess.left(360/6)
    

# make an octagon (eight sides)
for i in range(8):
    tess.forward(100)
    tess.left(360/8)
    
    
wn.mainloop()                # wait for user to close window
