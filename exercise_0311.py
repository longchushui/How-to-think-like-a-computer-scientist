#Write a program to draw a pentagram

# Try this on a piece of paper, moving and turning your cellphone as if it was a turtle. 
# Watch how many complete rotations your cellphone makes before you complete the star. 
# Since each full rotation is 360 degrees, you can figure out the total number of degrees 
# that your phone was rotated through. If you divide that by 5, because there are 
# five points to the star, you’ll know how many degrees to turn the turtle at each point.

#You can hide a turtle behind its invisibility cloak if you don’t want it shown. 
# It will still draw its lines if its pen is down. The method is invoked as 
# tess.hideturtle() . To make the turtle visible again, use tess.showturtle().

import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

tess.hideturtle() # make tess invisible

for i in range(5):
    tess.left(144)     # to complete the star you need two full rotations which is is 720
    tess.forward(100)  # degrees, divided by 5 (the five points to the star) you get 144

tess.showturtle() # make tess visible

wn.mainloop()
