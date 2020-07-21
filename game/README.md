# Boxcar

The boxcar version of this game was developed by train hoppers in the 1920's (hence the name). It was played fast, with the players calling out slang terms for the different scores. For more information on the game, including how the dice are scored, check out hte wikipedia page.

**https://en.wikipedia.org/wiki/Dice_10000**

## 1.1 class Engine 

Requires two initializers: coach object and save file. The Engine object will play through a round of Boxcar when play_round is called. Results of the round are printed to the save file.

## 2.1 class Coach (player)

This object houses the various players that are used when playing the game. One player must be selected at instantiation, and will be used throughout it's life. Coach recieves a set of dice and a score with roll_or_stay() function, and returns a boolean, True == roll, False == stay. Designating the player as 'Terminal' will allow a human player to make this decision.



This virtual version of the game includes several virtual players of the game. It will play through a specified number of rounds