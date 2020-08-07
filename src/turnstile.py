from engine import Engine
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import sample

'''Losses are counted as wins for the Perfect VP, 
therefore it's scores are not attainable in real life 
and it is a poor 
representation of the upper boundary of possible scores.
The VP defined through this gradient ascent model 
will replace the Perfect VP as an attainable method for 
achieving the best possible mean of scores.  

The player's choice to roll or stay will be evaluated
with two parameters: 
    Current Round Score     ---  [CRS]
    Number of In-Play Dice  ---  [NOD]

Each roll is a independent. Whether a player should roll
is determined by the outcome of that roll, which is 
unaffected by the number of rolls that player has
left in the current round.

The Custom VP is used to generate scores. A map of scores 
passed to the player. 

[COE] = {NOD:SCO} 

Each key represents the number of in-play dice, and 
values represent a score barrier between roll and stay. 
If the actual CRS is above COE[NOD], then the player 
will stay.

For example: 
    COE = {1:200,2:400,3:600,4:800,5:1100,6:1500,0:2500}
represents a complete COE, and:
    COE = {1:200,2:400,3:600,4:800,5:1100,6:'random',0:'random'}
represents a COE that is still being calculated. In this 
example, the best score boundaries for 1 through 5 in-play
dice have been calculated only. 

Each coefficient (1-0) is evaluated in turn.

I've named the [COE] after the coefficients of a general 
linear model becuase the process used here is based off 
of linear regression. 

The product is a matrix of mean scores for the [COE]s at 
within the ranges set. 

The target is a mean of scores closest to the Perfect VP, 
which is 657. To achieve this, the model uses the equation


'''


def gradient_shift():

    # Define local variables
    cycles = 0
    COE = {_:0 for _ in range(6)}
    COE['score'] = run_simulations(COE)

    # Start a CSV for recording each cycle's results
    f = open('../data/GAcycles.csv', 'w+') 
    f.write(f'Cycle,1,2,3,4,5,0,Mean_Score\n')
    
    # Features represent the pips on the dice. For example, 
    # if 3 dice are in play, use the score threshold at COE[3]
    for feature in [0,5,4,3,2,1]: 

        # Begin cycle
        print(f'feature = {feature}')
        COE_hat = COE.copy()  
        beta = 50 
        COE_hat[feature] = beta    
        COE_hat['score'] = run_simulations(COE)
        print(COE_hat)

        # Keep as long as the mean score is still increasing
        while COE_hat['score'] > COE['score'] or beta == 0:
            
            # Save COE_hat as actual coe, and record results
            COE = COE_hat.copy()
            cycles += 1
            f.write(f"{cycles},{COE[1]},{COE[2]},{COE[3]},{COE[4]},{COE[5]},{COE[0]},{COE['score']}\n")
            print(f'{COE}')

            # Increase beta-coefficient and test new COE_hat
            beta += 50
            COE_hat[feature] = beta
            COE_hat['score'] = run_simulations(COE_hat)




def run_simulations(COE, samples=80000, sims=80000):

    # Create local variables
    engine = Engine('custom', COE)
    mean_sum = 0

    # iter through number of sample means to take
    for _ in range(samples):

        # iter through number of simulations to run per sample
        score_sum = 0
        for _ in range(sims):

            # If the round wins, same score. Else, save 0.
            engine.play_round()
            if engine.state: score_sum += engine.round_points

        
        mean_sum += score_sum/sims 
    print(mean_sum/samples)
    
    return mean_sum/samples


            
        
if __name__ == '__main__':
    gradient_shift()
    pass
    # while R > prior:
    #         f.write(f'{COE.values()},{R}\n')
    #         print(COE)
    #         COE[variate] = COE[beta] + 50
    #         prior = R
    #         R = get_mean_score(COE)
    #     COE[beta] = COE[beta] - 50

        # Set range of score boundaries to test
        # boundaries = {
        #     1:range(0,201,50),
        #     2:range(250,451,50),
        #     3:range(450,651,50),
        #     4:range(700,901,50),
        #     5:range(1050, 1251, 50),
        #     6:range(1350, 1551, 50),
        #     0:range(2250, 2451,50)
        # }

    # for zero in range(2250, 2451,50):
    #     COE[0] = zero
    #     for one in range(0,201,50):
    #         COE[1] = one
    #         for two in range(250,451,50):
    #             COE[2] = two
    #             for three in range(450,651,50):
    #                 COE[3] = three
    #                 for four in range(700,901,50):
    #                     COE[4] = four
    #                     for five in range(1050, 1251, 50):
    #                         COE[5] = five
    #                         for six in range(1350, 1551, 50):
    #                             COE[6] = six
    #                             # Run simulation!
    #                             engine = Engine('custom', COE)
    #                             scores = np.array([])
    #                             for _ in range(8000):
    #                                 engine.play_round()
    #                                 if engine.state:
    #                                     scores = np.append(scores, engine.round_points)
    #                                 else:
    #                                     scores = np.append(scores, 0)
    #                             row = pd.DataFrame(COE, columns=[0,1,2,3,4,5,6], index=[0])  
    #                             row['mean'] = scores.mean()
    #                             df = pd.concat([df,row], sort=False, ignore_index=True)
    # df.to_csv('../data/turnstyle.csv')
                                
