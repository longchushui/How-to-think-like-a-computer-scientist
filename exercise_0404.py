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
tess.color("blue")
tess.width(3)


# Make a pretty figure, consisting of 20 squares
for i in range(20):
    draw_poly(tess, 4, 100)  # draw a square
    tess.left(360/20)       


wn.mainloop()             # wait for user to close window
