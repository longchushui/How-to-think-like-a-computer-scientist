# Write a function which is given an exam mark, and it returns a string — the grade for 
# that mark — according to this scheme:
#  Mark   Grade
#  >= 75  First
# [70-75) Upper Second
# [60-70) Second
# [50-60) Third
# [45-50) F1 Supp
# [40-45) F2
#  < 40   F3

# Each condition is of the function grade() is checked in order. If the first is false, 
# the next is checked, and so on. If one of them is true, the corresponding branch executes, 
# and the statement ends. Even if more than one condition is true, only the first true 
# branch executes.
# The else statement is not used here, since the else statement is optional

def grade(mark):
    """ The function grade() returns the grade for a given mark.
    """
    if mark < 40:
        print("F3")
    elif mark < 45:
        print("F2")
    elif mark < 50:
        print("F1 Supp")
    elif mark < 60:
        print("Third")
    elif mark < 70:
        print("Second")
    elif mark < 75:
        print("Upper Second")
    elif mark >= 75:
        print("First") 
