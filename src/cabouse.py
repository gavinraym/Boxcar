from bum import Die
from hopper import log

class Score():
    def __init__(self):
        ''' -Creates 6 dice upon instantiation, and 
        manages them throughout the simulation. This 
        script rolls the dice, calculates score, and
        sets dice.in_play to False when a score is 
        achieved. 
        '''
        self.dice = [Die() for _ in range(6)]
        self.points = 0

        # Points awarded for sets differs depending on the number rolled
        self.points_dict = {
            1: [0, 100, 200, 1000, 2000, 3000, 4000],
            2: [0, 0, 0, 200, 400, 600, 800],
            3: [0, 0, 0, 300, 600, 900, 1200],
            4: [0, 0, 0, 400, 800, 1200, 1600],
            5: [0, 50, 100, 500, 1000, 1500, 2000],
            6: [0, 0, 0, 600, 1200, 1800, 2400]
        }
    
#==============================================================================

    # award_points gives the player points and adds dice to dice
    # [points]=int, [dice]=list
    def _award_points(self, points, dice_list):
        self.points += points
        for die in dice_list:
            die.freeze()

    def _roll_dice(self):
        # Dice that are no longer in play have a pip value of 0. If no dice are
        # left in play, gives the player 6 new dice.       
        if sum([_.pips() for _ in self.dice]) == 0:
            for die in self.dice:
                die.in_play = True
        # Gives new pip values to only dice with die.in_play == True
        for die in self.dice:
            die.roll()     

#==============================================================================

    # The points function receives the new set of dice, and directs the scoring
    # process.
    def roll(self):
        # Score is set to zero
        self.points = 0    
        # Dice receive new pip values for this round     
        self._roll_dice()

#==============================================================================

        #FULL RUN is scored with dice pips of [1][2][3][4][5][6]
        if [_.pips() for _ in self.dice] == [1,2,3,4,5,6]:
            self._award_points(800, self.dice)

#==============================================================================

        # THREE DOUBLES is scored with exactly two each of three pip values.
        # For example, [2][2][4][4][5][5]
        else:
            pips = [0]*7
            for die in self.dice:
                pips[die.pips()] += 1 
            if sorted(pips) == [0,0,0,0,2,2,2]:
                self._award_points(500, self.dice)

#==============================================================================

            # COUNTING points are given from duplicates of numbers
            else: 
                for pip_num in [1,2,3,4,5,6]:
                    used_dice = [_ for _ in self.dice if _.pips() == pip_num]
                    points = self.points_dict[pip_num][len(used_dice)]
                    if points:
                        self._award_points(points, used_dice)
                
#==============================================================================

if __name__ == '__main__':
    pass
    


