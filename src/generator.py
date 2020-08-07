from engine import Engine
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import sys

def run_simulations(sims=8000):
    COE = create_COE()
    # Create local variables
    engine = Engine('custom', COE)

    # iter through number of simulations to run per sample
    score_sum = 0
    for _ in range(sims):

        # If the round wins, same score. Else, save 0.
        engine.play_round()
        if engine.state: 
            score_sum += engine.round_points

    COE['score'] = int(round(score_sum/sims, 0))
    return COE

def create_COE():
    return {
        1: random.choice(range(0,300,50)),
        2: random.choice(range(50,500,50)),
        3: random.choice(range(200,700,50)),
        4: random.choice(range(400,900,50)),
        5: random.choice(range(600,1500,50)),
        0: random.choice(range(1000,2000,50))
    }

def run(n, path):
    f = open(path, 'w')
    for _ in range(n):
        COE = run_simulations()
        f.write(f"{COE[1]},{COE[2]},{COE[3]},{COE[4]},{COE[5]},{COE[0]},{COE['score']}\n")


if __name__ == '__main__':
    n = 1000
    path = '../data/samples.csv'
    if sys.argv[1]:
        n = int(sys.argv[1])
    if sys.argv[2]:
        path = f'../data/{sys.argv[2]}.csv'
    run(n,path)
