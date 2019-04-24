import turtle

# this is an example of a void function, a functions that does not return a value. In this
# case the function does something useful, that is making a square.
def draw_square(t):
    """ The function draw_square() makes a turtle t draw a square with sides of 20 units 
        long.
    """
    for i in range(4):
        t.forward(20)
        t.left(90) 

# set up screen
wn = turtle.Screen()      
wn.bgcolor("lightgreen")  # make the background green

# set up turtle
tess = turtle.Turtle()
tess.color("hotpink")
tess.width(3)


# Make a for loop that calls the function draw_square to draw five squares.
for i in range(5):
    tess.pendown()
    draw_square(tess)
    tess.penup()
    tess.forward(40)
    

wn.mainloop()             # wait for user to close window
