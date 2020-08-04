from engine import Engine
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import sample

'''The objective here is to use gradient ascent to 
improve the Perfect VP. Because losses are counted 
as wins for the Perfect VP, the scores it achieves are
not attainable in real life and therefore a poor 
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
    # Loops through each range of scores
    # Builds a CEO for each combo of scores
    # Runs run_sim once for each COE

    # We will expect the first prior to be the 
    # same mean of scores as the Random VP. So, 
    # to calculate alpha, in this case the size
    # of the step from the current coefficient
    # value to the next, is the prior / alpha
        # Even the Perfect VP has fluctuations of score
        # means around 2 points for 8,000 games tested.
        # because of this fluctuation, we can allow the 
        # game to determine when we are close enough to 
        # an accurate evaluation of our COE. 

def gradient_shift():
    cycles = 0
    count = list()
    COE = run_simulations({_:0 for _ in range(6)})
    f = open('../data/GAcycles.csv', 'w+') 
    f.write(f'Cycle,COE,R\n')
    f.close()
    f = open('../data/GAcoes.csv', 'w+') 
    f.write(f'Feature,Variate,COE\n')
    f.close()

    while cycles<1000 and len(count)<10:
        print(f'{cycles}')
        cycles += 1
        COE_hat = run_simulations(COE)
        COE_hat = score_COEs(COE)
        R = COE_hat['score'] - COE['score']
        if R > 0:
            COE = COE_hat.copy()
            count = [COE]
        elif R > -1:
            count.append(COE_hat.copy())
            
        print(f'R = {R}\ncurrent COE = {COE_hat}\ncount list ={len(count)}\n\n')
        f = open('../data/GAcycles.csv', 'a')
        f.write(f'{cycles},{COE_hat},{R}\n')
        f.close()
    print(count)

def score_COEs(COE):
    f = open('../data/GAcoes.csv', 'a') 
    for (feature, variate) in get_tests(COE):
        COE_hat = COE.copy()
        COE_hat[feature] = variate 
        
        run_simulations(COE_hat) 
        if COE_hat['score'] > COE['score']:
            COE = COE_hat.copy()
        f.write(f"{feature},{variate},{COE}\n")
    f.close()
    return COE

def get_tests(COE):
    # Set range of score boundaries to test    
    tests = list()
    for feature in range(6):
        n = max(COE[feature]-150, 0)
        steps = range(n,n+251, 50)
        #steps = [n-200, n-100, n-50, n, n+50, n+100, n+200]       
        for variate in steps:
            tests.append((feature, variate)) 
    return sample(tests, len(tests))

def run_simulations(COE):
    engine = Engine('custom', COE)
    score = 0
    for count in range(100):
        means = list()
        for _ in range(2000):
            engine.play_round()
            if engine.state:
                means.append([engine.round_points])
            else:
                means.append([0])
        score = (score*count + np.mean(means))/(count+1)
    COE['score'] = score
    return COE


            
        
if __name__ == '__main__':
    
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
                                
