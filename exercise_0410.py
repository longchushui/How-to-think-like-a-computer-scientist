# Extend your program from exercise_0409. Draw five stars, but between each, pick up the pen, 
# move forward by 350 units, turn right by 144, put the pen down, and draw the next star. 


import turtle

# function to set up window
def make_window(colr, ttle):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


# function to set up turtle
def make_turtle(colr, sz):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t


# function to draw a star
def draw_star(t):
    """ The function draw_star() makes turtle t draw a star with a length of 100 units 
        for each side.
    """
    for i in range(5):
        t.left(144)     
        t.forward(100) 
    

# Set up window
wn = make_window("lightgreen", "Five stars")

# set up turtle tess
tess = make_turtle("hotpink", 2)

for i in range(5):
    draw_star(tess)
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()


wn.mainloop()   # Wait for user to close window.


