# Write a void function draw_equitriangle(t, sz) which calls draw_poly from the 
# previous question to have its turtle draw a equilateral triangle.

import turtle

def draw_poly(t, n, sz):
    """ The function draw_poly() makes a turtle t draw a regular polygon with n corners
        of size sz.
    """
    for i in range(n):
        t.forward(sz)
        t.left(360/n) 

def draw_equitriangle(t, sz):
    """ The function draw_equitriangle() calls the function draw_poly() to make turtle t
        draw a equitriangle of size sz.
    """
    draw_poly(t, 3, sz)

# set up screen
wn = turtle.Screen()      
wn.bgcolor("lightgreen")  # make the background green


# set up turtle tess
tess = turtle.Turtle()
tess.color("blue")
tess.width(2)

# draw a triangle with equal sizes that are each 50 units long.
draw_equitriangle(tess, 50)

wn.mainloop()             # wait for user to close window
