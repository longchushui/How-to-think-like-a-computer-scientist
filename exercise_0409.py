# Write a void function to draw a star, where the length of each side is 100 units. (Hint: You should turn the turtle 
# by 144 degrees at each point.)

import turtle


# function to draw a star
def draw_star(t):
    """ The function draw_star() makes turtle t draw a star with a length of 100 units 
        for each side.
    """
    for i in range(5):
        t.left(144)     
        t.forward(100) 
