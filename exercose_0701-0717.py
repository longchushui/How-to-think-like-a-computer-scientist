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
    
test_suite()        # Here is the call to run the tests
