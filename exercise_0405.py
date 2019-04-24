import turtle


# set up screen
wn = turtle.Screen()      
wn.bgcolor("lightgreen")  # make the background green


# set up turtle tess
tess = turtle.Turtle()
tess.color("blue")
tess.width(2)

# set up turtle alex
alex = turtle.Turtle()
alex.color("blue")
alex.width(2)

size = 10

# Make a pretty figure, consisting of 20 squares
for i in range(100):
    tess.forward(size) 
    tess.right(90) 
    size = size + 2 


size = 10    # set size to 10

# move alex to the correct location
alex.penup()
alex.forward(250)
alex.pendown()
   
# Make a pretty figure, consisting of 20 squares
for i in range(100):
    alex.forward(size) 
    alex.right(91) 
    size = size + 2        


wn.mainloop()             # wait for user to close window
