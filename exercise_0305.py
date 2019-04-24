# Assume you have the assignment: xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# a) Write a loop that prints each of the numbers on a new line.

for i in xs:
    print(i)
    
# b) Write a loop that prints each number and its square on a new line.

for i in xs:
    j = i * i
    print(i, j) # not any formatting, since that is not explained yet


# c) Write a loop that adds all the numbers from the list into a variable called total. 
#    You should set the total variable to have the value 0 before you start adding them up, 
#    and print the value in total after the loop has completed.

total = 0 # set the total variable to 0

for i in xs:
    total = total + i

print(total) # print the value in total after the loop has completed

# d) Print the product of all the numbers in the list. (product means all multiplied 
#    together)

product = 1 # set the value to one

for i in xs:
    product = product * i 
    
print(product)
