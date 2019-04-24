#Write a program to draw a face of a clock that looks something like this:

import turtle           # get the turtle module

# set up screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# set up turtle
tess = turtle.Turtle()
tess.color("blue")      # make tess blue
tess.shape("turtle")    # now tess looks like a turtle
tess.penup()            # and tess takes her pen up

# the for loop to make a clock
for i in range(12):
    tess.forward(120)
    tess.pendown()
    tess.forward(15)
    tess.penup()
    tess.forward(15)
    tess.stamp()
    tess.backward(150)
    tess.left(360/12)

wn.mainloop()           # the user can close the window
