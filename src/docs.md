# Boxcar

The boxcar version of this game was developed by train hoppers in the 1920's (hence the name). It was played fast, with the players calling out slang terms for the different scores. For more information on the game, including how the dice are scored, check out the wikipedia page.

**https://en.wikipedia.org/wiki/Dice_10000**


## **1** *class* ***Dice*** ([bum.py](bum.py)) 
Represents dice used in the game.

**1.1** *attribute pip_value* - Number of pips showing on die.
**1.2** *attribute in_play* - True until the die has scored.
**1.3** *attribute show* - Indicates if die should be shown as rolling when human player is running the simulation.

**1.4** *method roll(self)* - Randomly changes pip value if die is still in play.
**1.5** *method freeze(self)* - Changes Die.in_play to false.
**1.6** *method pips(self)* - returns pip value if in play, or 0. Used by scoring algorithms.
**1.7** *method reset(self)* - Resets attributes to original state.  

## **2** *class* ***Score*** ([cabouse.py](cabouse.py))
Creates 6 dice upon instantiation, and manages them throughout the simulation. This script rolls the dice, calculates score, andsets dice.in_play to False when a score is achieved.  

**2.1** *attribute dice* - List of the six dice being used.
**2.2** *attribute points* - Number of points gained on the previous roll.

**2.3** *method roll(self)* - Triggers this objects main function: dice are rolled and the score calculated. Nothing is returned. Results should be accessed through the attributes.

## **3**  *class* ***Player*** ([coach.py](coach.py)])

This object houses the VPs that are used when playing the game. Desired VP or 'terminal' must be indicated when initialized.

**3.1** *method roll_or_stay(self, dice, score)* - Receives a list of dice and the current round score. Returns boolean indicating whether or not the player wishes to roll the dice.  

## **4** *class* ***Engine*** ([engine.py](engine.py))

The Engine class object drives the simulation. At instantiation, an engine will create the specified player and initialize a score object. This is where the round's score is kept, as well as the number of rolls still remaining. The function play_round triggers a round to execute. 


**4.1** *attribute round_points* - int of how many points were achieved on the previous roll. *Does not change to 0 when the round was lost.*
**4.2** *attribute state* boolean, indicating if the previous roll resulted in a successful outcome.

**4.3** *method play_round(self)* - Triggers a new round to be played and attributes to update. Does not take any arguments and returns None.


## **5** ***hopper*** ([hopper.py](hopper.py))

A Hopper is a type of traincar. It's steep sides allow for the transportation of large quantities of raw material, like coal. This class does the same for the Boxcar simulator. It containes functions for the other objects to use for displaying information to the terminal.

**5.1** *function log(str logstring)* - Prints str [logstring] to terminal in a user friendly way. Used for testing.
**5.2** *function clear()* - Clears terminal on both mac and linux.
**5.3** *function display_dice(dice)* - Receives a set of dice and displays pip values to terminal.
**5.4** *function display_rolling(dice)* - plays an animation of dice being rolled.
**5.5** *function display_win(dice, score)* - Shows a winning result.
**5.6** *function display_loss(dice)* - Shows a losing result.
**5.7** *function display_choice(dice, score)* - Displays info and asks human player to indicate roll or stay.

## **6** ***station*** ([station.py](station.py)) 

The functions in station.py are used via the terminal to run simulations and write the results to file.

**6.1** *function define_optimal_sample_size(start, stop, step)* - Arguments match those of Python's built-in Range() function. This function generates the data used to determine the number of similations needed. results are written to [batchtests.csv](../data/batchtests.csv)

**6.2** *function define_optimal_bootsize(start, stop, step)* - Arguments match those of Python's built-in Range() function. This function generates data used to determine minimum number of bootstraps needed for comparisons. Results are written to [boottests.csv](../data/batchtests.csv)

**6.3** *function take_sample(vp_name=str, n=int, filename=str) - This function is used to run simulations on specific VP's. Indicate name of VP as first arguments, or 'terminal' to record your own scores. N = the number of simulations to run. Results are written to a in [data](../data) with the filename specified. Do not add extension to filename; .csv will be added automatically.