import time
import os

#Asks the whether to set timer in hours,minutes or seconds
Unit_Time = input("Set timer as hour/min/sec: ")

#Asks user to set timer based on the unit they chose
if Unit_Time == "hour":
    Enter_Time = int(input("Enter time in in hours: "))
    Enter_Time = Enter_Time*3600

elif Unit_Time == "min":
    Enter_Time = int(input("Enter timer in in minutes: "))
    Enter_Time = Enter_Time*60

elif Unit_Time == "sec":
    Enter_Time = int(input("Enter timer in seconds: "))

else:
    print("Invalid input, please try again.")
                 
#Creates a timer that counts down from the time given by user. Makes use of Python range function step, which in this case subtracts 1 from the previous number, creating a count down effect
for x in range(Enter_Time, 0, -1):
    seconds = x % 60
    minutes = int(x/60)
    hours = int(x/ 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

#Prints string when timer counts to zero
print("Time's up!")

#Creates a sound that repeats three times once timer == 0
for i in range(3):
    os.system("afplay /System/Library/Sounds/Funk.aiff")

