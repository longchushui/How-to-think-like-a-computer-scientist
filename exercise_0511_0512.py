# Write a function is_rightangled which, given the length of three sides of a triangle, 
# will determine whether the triangle is right-angled. Assume that the third argument to 
# the function is always the longest side. It will return True if the triangle is 
# right-angled, or False otherwise.

def is_rightangled(a, b, c):
    """ The function is_rightangled() will return True if the triangle is right-angled,
        false otherwise. The third argument -c-  represents the longest side.
    """
    return abs(c ** 2) == abs(a ** 2) + abs(b ** 2)
    
# Extend the above program so that the sides can be given to the function in any order.

def is_rightangled(a, b, c):
    """ The function is_rightangled() will return True if the triangle is right-angled,
        false otherwise. The values a, b and c represent the length of the sides of the
        triangle.
    """
    if max(a, b, c) == a:
        return abs(a ** 2) == abs(b ** 2) + abs(c ** 2)
    elif max(a, b, c) == b:
        return abs(b ** 2) == abs(a ** 2) + abs(c ** 2)
    else:
        return abs(c ** 2) == abs(a ** 2) + abs(b ** 2)
