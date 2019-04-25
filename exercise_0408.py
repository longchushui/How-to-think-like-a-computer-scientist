# Write a function area_of_circle(r) which returns the area of a circle of radius r.

def area_of_circle(r):
    """ The function area_of_circle() returns the area of a circle of radius r.
    """
    area = 3.1415 * (r * r)
    return area

# note that the answer is not formatted. In a later chapter it will be explained how to 
# format the answer so it will be rounded to two decimals before printing.
print(area_of_circle(10))

