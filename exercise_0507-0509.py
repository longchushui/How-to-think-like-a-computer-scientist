# Exercise 0507: Modify the turtle bar chart program so that the pen is up for the small 
# gaps between each bar.

# Exercise 0508: Modify the turtle bar chart program so that the bar for any value of 
# 200 or more is filled with red, values between [100 and 200) are filled with yellow, 
# and bars representing values less than 100 are filled with green.

# Exercise 0509: In the turtle bar chart program, what do you expect to happen if one 
# or more of the data values in the list is negative? Try it out. Change the program so 
# that when it prints the text value for the negative bars, it puts the text below the 
# bottom of the bar.

import turtle


def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           
    t.left(90)
    t.forward(height)     
    t.write(" " + str(height))
    t.right(90)
    t.forward(40)         
    t.right(90)
    t.forward(height)     
    t.left(90)
    t.end_fill()
    t.penup()            # added this line for exercise 0507     
    t.forward(10)
    t.pendown()          # added this line for exercise 0507


wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")


tess = turtle.Turtle()       # Create tess and set some attributes
#tess.color("blue", "red")   # commented this line for exercise 0508
tess.pensize(3)


xs = [48,117,200,240,160,260,220,-219]     # added a negative value for exercise 0509

for a in xs:
    if a < 100:                        # added this line for exercise 0508
        tess.color("blue", "green")    # added this line for exercise 0508
        draw_bar(tess, a)              # added this line for exercise 0508
    elif a < 200:                      # added this line for exercise 0508
        tess.color("blue", "yellow")   # added this line for exercise 0508
        draw_bar(tess, a)              # added this line for exercise 0508
    else:                              # added this line for exercise 0508
        tess.color("blue", "red")      # added this line for exercise 0508
        draw_bar(tess, a)

wn.mainloop()
