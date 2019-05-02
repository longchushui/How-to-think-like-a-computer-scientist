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
    test(count_odd([1, 3, 4, 6]) == 2)  # tests for exercise 1
    test(count_odd([2, 4, 6]) == 0)
    test(sum_even([2, 2, 6]) == 10)     # tests for exercise 2
    test(sum_even([2, 2, 1, 3, 6]) == 10)
    test(sum_even([3, 1, 1, 3, 6]) == 6)
    test(sum_even([3, 1, 1, 3]) == 0)
    test(sum_negative([-1, -2, -3, 0, 1, 2, 3]) == -6)  # tests for exercise 3
    test(sum_negative([0, 1, 2, 3]) == 0)               
    test(count_words(["a", "the", "fives", "lists"]) == 2)# tests for exercise 4
    test(sum_all([1, 1, 3, 4]) == 5)       # tests for exercise 5
    test(sum_all([1, 1, 3, 3]) == 8)      
    test(sum_all([2, 2, 4]) == 0)       
    test(count_word(["a", "is", "sam", "the"]) == 3)       # tests for exercise 6  
    test(count_word(["a", "is", "the"]) == 3)
    test(count_word(["sam", "the", "is"]) == 1) 
    test(is_prime(11))                                     # tests for exercise 10                      
    test(not is_prime(35))
    test(is_prime(19911121))

# Exercise 1: Write a function to count how many odd numbers are in a list.

def count_odd(xs):
    """ The function count_odd(xs) returns how many odd numbers there are in a list xs.
    """
    count = 0
    for i in xs:
        if i % 2 == 1:
            count += 1
    return count


# Exercise 2: Sum up all the even numbers in a list.

def sum_even(xs):
    """ The function sum_even(xs) sums up all the even numbers in a list.
    """
    sum = 0
    for i in xs:
        if i % 2 == 0:
            sum += i
    return sum
    

# Exercise 3: Sum up all the negative numbers in a list.

def sum_negative(xs):
    sum = 0
    for i in xs:
        if i < 0:
            sum += i
    return sum
    

# Exercise 4: Count how many words in a list have length 5

def count_words(xs):
    """ The function count_words(xs) count how many words in a list s have a length of
        5. 
    """
    count = 0
    for i in xs:
        if len(i) == 5:
            count += 1
    return count
    

# Exercise 5: Sum all the elements in a list up to but not including the first even 
# number. (Write your unit tests. What if there is no even number?)

def sum_all(xs):
    """ The function sum_all(xs) sums all the elements in a list up to but not including
        the first even number.
    """
    return xs

# Exercise 6: Count how many words occur in a list up to and including the first 
# occurrence of the word “sam”. (Write your unit tests for this case too. What if “sam” 
# does not occur?)

def count_word(xs):
    """ The function count_words(xs) counts how many words occur in a list up to and 
        including the first occurenece of the word "sam".
    """
    count = 0
    for i in xs:
        if i != "sam":
            count += 1
        elif i == "sam":
            count += 1
            break
    return count


# Exercise 7: Add a print function to Newton’s sqrt function that prints out better each 
# time it is calculated. Call your modified function with 25 as an argument and record 
# the results.

def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print(better)  # add print function that prints out better each time
        if abs(approx - better) < 0.001:
            return better
        approx = better


# Exercise 9: Write a function print_triangular_numbers(n) that prints out the first 
# n triangular numbers. 

def print_triangular_numbers(n):
    for i in range(1, n + 1):
        tn = (i * (i + 1))/ 2
        print(i, int(tn))


# Exercise 10: Write a function, is_prime, which takes a single integer argument and 
# returns True when the argument is a prime number and False otherwise.

def is_prime(n):
    """ The function is_prime(n) takes a single integer argument b and returns True when 
        the argument is a prime number and False otherwise.
    """
    sqrt = int(n ** 0.5)    # determine square root and take integer
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True
    


# Exercise 11: Revisit the drunk pirate problem from the exercises in chapter 3. This 
# time, the drunk pirate makes a turn, and then takes some steps forward, and repeats 
# this. Our social science student now records pairs of data: the angle of each turn, 
# and the number of steps taken after the turn. Her experimental data is [(160, 20), 
# (-43, 10), (270, 8), (-43, 12)]. Use a turtle to draw the path taken by our drunk 
# friend.

path = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

wn = turtle.Screen() # set up screen
arrr = turtle.Turtle() # set up turtle

def draw_something(path, t):
    for (turn, steps) in path:
        t.left(turn)
        t.forward(steps)

draw_something(path, arrr)


# Exercise 12: Many interesting shapes can be drawn by the turtle by giving a list of 
# pairs like we did above, where the first item of the pair is the angle to turn, and the
# second item is the distance to move forward. Set up a list of pairs so that the turtle 
# draws a house with a cross through the centre, as show here. This should be done 
#without going over any of the lines / edges more than once, and without lifting your pen.

path2 = [(90, 100), (-90, 100), (225, 141), (135, 100), (90, 100), (45, 71), (90, 71), (90, 141)]

house = turtle.Turtle()     # set up turtle
draw_something(path2, house)

wn.mainloop() # wait for user to close screen

    
test_suite()        # Here is the call to run the tests
