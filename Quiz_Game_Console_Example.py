import os, sys, random, time # importing the libary's

def Main():
    print("What is 1+1?") # Displays On The Screen; "What is 1+1?"
    q1 = input("User: ") # Get The Users Input
    if q1 =="2": # If function, so if the input is 2 then...
        print("Correct!")
        time.sleep(1) # let the code wait for 1 second
    else: # if the input isn't 2 then...
        print("Lose!")
        time.sleep(1)
        Main() # got to Main()

Main() # Go to Main() ('start code')
