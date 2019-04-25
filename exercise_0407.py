# Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to 
# and including n. So sum_to(10) would be 1+2+3...+10 which would return the value 55.

def sum_to(n):
    """ The function sum_to() returns the sum of all integer numbers up to and including
        n. So sum_to(10 ) would be 1+2+3...+10 which returns the value 55.
    """
    sum = 0
    for i in range(n + 1): # add + 1 because python starts from zero
        sum = sum + i
    return sum

# Yes the function returns the value 55
print(sum_to(10))

