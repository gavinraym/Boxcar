from os import system, name
import time
    


    ## A Hopper is a type of traincar. It's steep sides allow for
    ## the transportation of large quantities of raw material,
    ## like coal. This class does the same for the boxcar game.
    ## It containes functions for the other objects to use.

#==============================================================================

def display(txt, t=0): 
    # This function clears the terminal and prints a new line.
    # It also stalls the program for t=time in seconds. 

    # Evaluates type of operating system because mac and linux use
    # different commands.
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
    print(f'\r{txt}')
    # Time stall is at end. Each function calling clear() 
    # can determine how long the program should pause
    # after it is called.
    time.sleep(t)

#==============================================================================

def log(logstring):
    print(f'log: {logstring}')





    

  