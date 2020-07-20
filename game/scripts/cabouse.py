from bum import Die
from hopper import display
from hopper import log

class Score():
    def __init__(self):
        ''' -Takes in a list of dice of any size,
         
            -calculates points gained,
        
            -separates dice when used. 
        
        If [dice] is empty, the player should be awarded
        a brand new set of six dice to play with. 
        
        If [dice] is empty, the player has failed to points
        and should receive a game over. (no points received)'''
        self.dice = [Die() for _ in range(6)]
        self.points = 0
    
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

#=======FULL RUN is scored with dice pips of [1][2][3][4][5][6]
        if [_.pips() for _ in self.dice] == [1,2,3,4,5,6]:
            self._award_points(800, self.dice)

#=======THREE DOUBLES is scored with exactly two each of three pip values.
        # For example, [2][2][4][4][5][5]
        else:
            pips = [0]*7
            for die in self.dice:
                pips[die.pips()] += 1 
            if sorted(pips) == [0,0,0,0,2,2,2]:
                self._award_points(500, self.dice)

#===========COUNTING points are given from duplicates of numbers
                # Points awarded differs depending on the number
            else:
                # Count ones
                ones = [_ for _ in self.dice if _.pips() == 1]
                points = [0, 100, 200, 1000, 2000, 3000, 4000][len(ones)]
                if points: self._award_points(points, ones)

                # Count twos
                twos = [_ for _ in self.dice if _.pips() == 2]
                points = [0, 0, 0, 200, 400, 600, 800][len(twos)]
                if points: self._award_points(points, twos)

                # Count threes
                threes = [_ for _ in self.dice if _.pips() == 3]
                points = [0, 0, 0, 300, 600, 900, 1200][len(threes)] 
                if points: self._award_points(points, threes)

                # Count fours
                fours = [_ for _ in self.dice if _.pips() == 4]
                points = [0, 0, 0, 400, 800, 1200, 1600][len(fours)] 
                if points: self._award_points(points, fours)

                # Count fives
                fives = [_ for _ in self.dice if _.pips() == 5]
                points = [0, 50, 100, 500, 1000, 1500, 2000][len(fives)]
                if points: self._award_points(points, fives)

                # Count sixes
                sixes = [_ for _ in self.dice if _.pips() == 6]
                points =[0, 0, 0, 0, 600, 1200, 1800][len(sixes)]
                if points: self._award_points(points, sixes)

#==============================================================================

        # Ends roll by returning number of dice and points 
        n = len([_ for _ in self.dice if _.in_play])     
        return  n, self.points

#==============================================================================

    def reset_dice(self):
        self.dice = [Die() for _ in range(6)]
        self.points = 0

#==============================================================================

if __name__ == '__main__':
    
    sobj = Score()
    sobj.roll()
    log('\n')
    sobj.roll()
    


