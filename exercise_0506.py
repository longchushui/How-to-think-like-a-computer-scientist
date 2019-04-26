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
        grade = "F3"
    elif mark < 45:
        grade = "F2"
    elif mark < 50:
        grade = "F1 Supp"
    elif mark < 60:
        grade = "Third"
    elif mark < 70:
        grade = "Second"
    elif mark < 75:
        grade = "Upper Second"
    elif mark >= 75:
        grade = "First"
    return grade


# The list xs represents different marks.
xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]


# Test the function grade for all the elements in the list called xs:
for i in range(len(xs)):
    mark = xs[i]
    grades = grade(xs[i])
    print(str(mark) + " " +  grades)
