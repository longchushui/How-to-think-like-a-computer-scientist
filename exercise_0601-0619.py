# All of the exercises below should be added to a single file. In that file, you should 
# also add the test and test_suite scaffolding functions shown above, and then, as you 
# work through the exercises, add the new tests to your test suite. (If you open 
# the online version of the textbook, you can easily copy and paste the tests and the 
#fragments of code into your Python editor.)

# After completing each exercise, confirm that all the tests pass.

import sys    # needed for our test suite

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(turn_clockwise("N") == "E")   # tests for exercise 01
    test(turn_clockwise("W") == "N")   
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    test(day_name(3) == "Wednesday")   # tests for exercise 02
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_num("Friday") == 5)       # tests for exercise 03
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    test(day_add("Monday", 4) ==  "Friday") # tests for exercise 04
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday") # tests for exercise 05
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    test(days_in_month("February") == 28)    # tests for exercise 06
    test(days_in_month("December") == 31)
    test(days_in_month("February") == 28)    
    test(days_in_month("December") == 31)
    test(days_in_month("April") == 30)
    test(to_secs(2, 30, 10) == 9010)        # tests for exercise 07
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)   # tests for exercise 08
    test(to_secs(2.433,0,0) == 8758)
    test(hours_in(9010) == 2)                  # tests for exercise 09
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)
    test(compare(5, 4) == 1)                   # tests for exercise 11
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    test(hypotenuse(3, 4) == 5.0)              # tests for exercise 12
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    test(slope(5, 3, 4, 2) == 1.0)             # tests for exercise 13
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)
    test(is_even(2) == True)                   # tests for exercise 14
    test(is_even(3) == False)
    test(is_even(0) == True)
    test(is_even(-2) == True)
    test(is_odd(2) == False)                   # tests for exercise 15
    test(is_odd(3) == True)
    test(is_odd(0) == False)
    test(is_odd(-2) == False)
    test(is_factor(3, 12))                     # tests for exercise 16
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))




# Exercise 01: The four compass points can be abbreviated by single-letter strings as 
# “N”, “E”, “S”, and “W”. Write a function turn_clockwise that takes one of these four 
# compass points as its parameter, and returns the next compass point in the clockwise 
# direction.

def turn_clockwise(point):
    """ The function turn_clockwise() takes one of the four compass points {N, E, S and
        W} as its parameter and returns the next compass point in the clockwise direction.
    """
    if point == "N":
        return "E"
    elif point == "E":
        return "S"
    elif point == "S":
        return "W"
    elif point == "W":
        return "N"

# Exercise 02: Write a function day_name that converts an integer number 0 to 6 into the 
# name of a day. Assume day 0 is “Sunday”. Once again, return None if the arguments to 
# the function are not valid. 

def day_name(day_num):
    if day_num == 0:
        return "Sunday"
    elif day_num == 1:
        return "Monday"
    elif day_num == 2:
        return "Tuesday"
    elif day_num == 3:
        return "Wednesday"
    elif day_num == 4:
        return "Thursday"
    elif day_num == 5:
        return "Friday"
    elif day_num == 6:
        return "Saturday"

# Exercise 03: Write the inverse function day_num which is given a day name, and returns 
# its number

def day_num(day_name):
    if day_name == "Sunday":
        return 0
    elif day_name == "Monday":
        return 1
    elif day_name == "Tuesday":
        return 2
    elif day_name == "Wednesday":
        return 3
    elif day_name == "Thursday":
        return 4
    elif day_name == "Friday":
        return 5
    elif day_name == "Saturday":
        return 6
        
# Exercise 04: Write a function that helps answer questions like ‘“Today is Wednesday. 
# I leave on holiday in 19 days time. What day will that be?”’ So the function must take 
# a day name and a delta argument — the number of days to add — and should return the 
# resulting day name:

def day_add(day, n_days):
    """ The function day_add() takes two arguments, day and 
        the number of days to add (n_days). The functions returns the resulting day name.
    """
    n_days = (day_num(day) + (n_days % 7)) % 7
    return day_name(n_days)

# Exercise 05: Can your day_add function already work with negative deltas? For example, 
# -1 would be yesterday, or -7 would be a week ago:
# Yes the above functions can also work with negative deltas

# Exercise 06: Write a function days_in_month which takes the name of a month, and 
# returns the number of days in the month. Ignore leap years

def days_in_month(month):
    """ The function day_in_month() returns the number of days in the month given the
        argument month.
    """
    if month == "February":
        return 28
    elif (month == "January"
         or month == "March"
         or month == "May"
         or month == "July"
         or month == "August"
         or month == "October"
         or month == "December"):
        return 31
    elif (month == "April"
         or month == "May"
         or month == "June"
         or month == "September"
         or month == "November"):
        return 30


# Exercise 07: Write a function to_secs that converts hours, minutes and seconds to a 
# total number of seconds. 

def to_secs(hours, minutes, seconds):
    """ The functions to_secs() converts hours, minutes and seconds to a total number of
        seconds.
    """
    sec_h = hours * 60 * 60
    sec_m = minutes * 60
    return sec_h + sec_m + seconds

# Exercise 08: Extend to_secs so that it can cope with real values as inputs. It should 
# always return an integer number of seconds (truncated towards zero):

# Exercise 09: Write three functions that are the “inverses” of to_secs:
# 1) hours_in returns the whole integer number of hours represented by a total number of
#    seconds.
# 2) minutes_in returns the whole integer number of left over minutes in a total number 
#    of seconds, once the hours have been taken out.
# 3) seconds_in returns the left over seconds represented by a total number of seconds.
# You may assume that the total number of seconds passed to these functions is an integer.

def hours_in(seconds):
    return (seconds // 60) // 60
 
    
def minutes_in(seconds):
    sec_m = seconds - to_secs(hours_in(seconds), 0, 0)
    return sec_m // 60


def seconds_in(seconds):
    return seconds - to_secs(hours_in(seconds), minutes_in(seconds), 0)


# Exercise 11: Write a compare function that returns 1 if a > b, 0 if a == b, 
# and -1 if a < b

def compare(a, b):
    if a == b:
        return 0
    elif a < b:
        return -1
    elif a > b:
        return 1


# Exercise 12: Write a function called hypotenuse that returns the length of the 
# hypotenuse of a right triangle given the lengths of the two legs as parameters:

def hypotenuse(a, b):
    from math import sqrt
    return sqrt(a ** 2 + b ** 2)


# Exercise 13: Write a function slope(x1, y1, x2, y2) that returns the slope of the 
# line through the points (x1, y1) and (x2, y2).
# Then use a call to slope in a new function named intercept(x1, y1, x2, y2) that 
# returns the y-intercept of the line through the points (x1, y1) and (x2, y2)

def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
    

def intercept(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    return y1 - (m * x1)
    
    
# Exercise 14: Write a function called is_even(n) that takes an integer as an argument 
# and returns True if the argument is an even number and False if it is odd

def is_even(n):
    """ The function is_even(n) takes an integer as an argument and returns True if the
        argument is an even number and False if it is odd.
    """
    return n % 2 == 0

# Exercise 15: Now write the function is_odd(n) that returns True when n is odd and False 
# otherwise. Include unit tests for this function too.

def is_odd(n):
    """ The function is_odd(n) takes an integer as an argument and returns True if the
        argument is an odd number and False if it is even.
    """
    return n % 2 == 1
    
# Finally, modify it so that it uses a call to is_even to determine if its argument is 
# an odd integer, and ensure that its test still pass

def is_odd(n):
    """ The function is_odd(n) takes an integer as an argument and returns True if the
        argument is an odd number and False if it is even.
    """
    return not is_even(n)
    
# exercise 16: Write a function is_factor(f, n). 

def is_factor(f, n):
    return 0


# Exercise 08: Extend to_secs so that it can cope with real values as inputs. It should 
# always return an integer number of seconds (truncated towards zero):

test_suite()        # Here is the call to run the tests
