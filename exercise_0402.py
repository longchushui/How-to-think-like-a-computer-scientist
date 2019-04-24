import turtle

# this is an example of a void function, a functions that does not return a value. In this
# case the function does something useful, that is making a square.
def draw_square(t, sz):
    """ The function draw_square() makes a turtle t draw a square of size sz.
    """
    for i in range(4):
        t.forward(sz)
        t.left(90) 

# set up screen
wn = turtle.Screen()      
wn.bgcolor("lightgreen")  # make the background green

# set up turtle
tess = turtle.Turtle()
tess.color("hotpink")
tess.width(3)

# Set size to 20. The first square will have sides of 20 units long
size = 20

# Make a for loop that calls the function draw_square to draw five squares.
for i in range(5):
    draw_square(tess, size)   
    tess.penup()
    tess.right(135)
    tess.forward(14)
    tess.left(135)
    tess.pendown()
    size = size + 20


wn.mainloop()             # wait for user to close window
