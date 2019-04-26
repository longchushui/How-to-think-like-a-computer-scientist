# Write a function find_hypot which, given the length of two sides of a right-angled 
# triangle, returns the length of the hypotenuse. (Hint: x ** 0.5 will return the 
# square root.)

def find_hypot(a, b):
    """ The function find_hypot(), will return the length of the hypotenuse given the
        two sides, a and b, of a right-angled triangle.
    """
    ht = ((a ** 2) + (b ** 2)) ** 0.5
    return ht
