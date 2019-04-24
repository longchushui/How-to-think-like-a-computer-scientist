import turtle


def draw_poly(t, n, sz):
    """ The function draw_poly() makes a turtle t draw a regular polygon with n corners
        of size sz.
    """
    for i in range(n):
        t.forward(sz)
        t.left(360/n) 


# set up screen
wn = turtle.Screen()      
wn.bgcolor("lightgreen")  # make the background green


# set up turtle
tess = turtle.Turtle()
tess.color("hotpink")
tess.width(3)


# Make a regular polygon with 8 sides of length 50.
draw_poly(tess, 8, 50)


wn.mainloop()             # wait for user to close window
