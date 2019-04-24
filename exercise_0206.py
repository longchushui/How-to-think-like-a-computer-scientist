# You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm 
# go off? (Hint: you could count on your fingers, but this is not what we’re after. If you are tempted to count on 
# your fingers, change the 51 to 5100.)

# Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), 
# and ask for the number of hours to wait. Your program should output what the time will be on the clock when the alarm 
# goes off.

current_time = input("What is the current time?")
hours_wait = input("After how many hours shoudl the alarm go off?")

hours = hours_wait % 24
current_time + hours

print("The alarm will go off at" + "hours")
