from engine import Engine
from coach import Player
import csv
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from hopper import clear
import random
'''
This script is used via the terminal to run simulations and 
write the results to file.
'''

def define_optimal_sample_size(start=500, stop=7000, step=500):
    # Generates samples of sizes defined by args

    # To help computers with less memory, this function can be run
    # in stages. , after running the first set of tests, change the
    # 'w+' in the next line to 'a', and comment out the following 
    # line (f.write(f'mean_score\n')). Then run fuction with smaller
    # batch sizes (like: start=2500, stop=5000)
    
    
    engine = Engine('perfect')
    # First loop: Ranges of sample sizes to test
    for n in range(start, stop, step):
        
        # Second loop: tests each sample size 25 times.
        # This results in 25 light blue dots on the graph
        for sample in range(25):
            results = list()
            # Third loop runs simulation n times and stores
            # the mean of those simulations.
            for _ in range(n):
                engine.play_round()
                results.append(engine.round_points)
            f = open('../data/batchtests.csv', 'a')
            f.write(f'{n},{int(np.mean(results))}\n')
            f.close()
            clear()
            print(f'Generating samples... test #{int(n/stop*100)}.{int(sample/250*100)}% done')
    f.close()

def run_test(vp_name='perfect', n=4000, t=200, file_name=None):
    file_name = file_name or vp_name
    engine = Engine(vp_name)
    for _ in range(t):
        score_sum = 0
        for _ in range(n):
            engine.play_round()
            score_sum += engine.round_points
        f = open(f'../data/{file_name}.csv', 'w+')
        f.write(f'{score_sum/n}\n') 
        f.close()

def take_sample(vp_name='perfect', n=100, file_name='sample'):
    # Writes n number of scores + outcomes to file using 
    # the specified VP.
    engine = Engine(vp_name)
    for _ in range(n):
        engine.play_round()
        f = open(f'../data/{file_name}.csv', 'a') 
        f.write(f'{engine.round_points}\n')
        f.close()  

def generate(n=10000, file_name='gen_data'):
    for _ in range(n):
        # Create a new COE randomly
        COE = {
        1: random.choice(range(50,750,50)),
        2: random.choice(range(50,750,50)),
        3: random.choice(range(50,1000,50)),
        4: random.choice(range(450,2000,50)),
        5: random.choice(range(900,3500,50)),
        0: random.choice(range(1500, 6000,50))
        }
        engine = Engine('custom', COE=COE)
        # iter through number of simulations to run per sample
        score_sum = 0
        for _ in range(8000):
            # Save the score to score sum
            engine.play_round()
            score_sum += engine.round_points
        # Determine mean score, and record
        mean = int(round(score_sum/8000, 0))
        f = open(f'../data/{file_name}.csv', 'a')
        f.write(f"{COE[1]},{COE[2]},{COE[3]},{COE[4]},{COE[5]},{COE[0]},{mean}\n")
        f.close()
        clear()
        print(f'{_} of {n} completed.')

def score_custom(coe):
    engine = Engine('custom', COE=coe)
    score_sum = 0
    for _ in range(8000):
        # Save the score to score sum
        engine.play_round()
        score_sum += engine.round_points
    # Determine mean score, and return
    return int(round(score_sum/8000, 0))

def create_AI_training_data(n=500):
    engine = Engine('generate_AI_data')
    for _ in range(n):
        engine.play_round()


if __name__ == '__main__':
    clear()
    num =input('''Menu:\n
    1)  Play via the terminal. (ch.1)
    2)  Generate scores from AI. (ch.2)
    3)  Define the optimal number of samples. (ch.2)
    4)  Run test of mean score on each AI. (ch.3)
    5)  Use randomized algorithms to generate data (ch.4)
    6)  Create training data for AI

    Please input a number
    ''')
    if num == '1':
        name= input("What is the player's name?")
        n = input('How many games do you want to play? (200 recommended)')
        take_sample('terminal', n=int(n), file_name=name)
    if num == '2':
        take_sample()
    if num == '3':
        define_optimal_sample_size()
    if num == '4':
        for vp in Player()._funcs.keys():
            if vp not in ['custom', 'terminal']:
                run_test(vp)
    if num == '5':
        generate()
    if num == '6':
        create_AI_training_data()

        
        
    


