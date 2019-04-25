# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. 
# Write a function which is given the day number, and it returns the day name (a string).


def day_name(day_number):
    """ The function day_name() returns the day_name {Sunday-Saturday} given 
        the day_number {0-6}.
    """
    if day_number == 0:
        print("Sunday")
    elif day_number == 1:
        print("Monday")
    elif day_number == 2:
        print("Tuesday")
    elif day_number == 3:
        print("Wednesday")
    elif day_number == 4:
        print("Thursday")
    elif day_number == 5:
        print("Friday")
    elif day_number == 6:
        print("Saturday")
    else:
        print("Give a number between 0 and 6.")


