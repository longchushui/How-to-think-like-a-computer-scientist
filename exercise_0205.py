# The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
# A = P(1 + r/n)^nt
# Where:
# P = principal amount (inititial investment)
# r = annual nominal interest rate (as a decimal)
# n = number of times the intereset is compounded per year
# t = number of years
# see also: https://en.wikipedia.org/wiki/Compound_interest
# Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, 
# and assign to r the interest rate of 8%. Then have the program prompt the user for the number of years t that 
# the money will be compounded for. Calculate and print the final amount after t years.

p = 10000 # assign the amount of $10000 to p
n = 12    # assign the number of times the interest is compounded to 12
r = 0.08  # assign the interest rate r to 8%

# ask user for input and turn string into integer
t = int(input("The number of years the that the money will be compounded for: ")) 

# calculate the final amount
final_amount = p * (1 + r / n)**(n*t)

# show the final amount, note that t and final_amount are turned into strings
print("The final amount after " + str(t) + " years is: " + str(final_amount))
