from engine import Engine
import csv
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def define_optimal_sample_size(start, stop, step):
    # Generates samples of sizes defined by args
    # WILL CRASH YOUR COMPUTER IF RUN IN SINGLE GO!
    # Start with (500, 250, 3000) and increase beg
    # and end slowly.
    #
    # !Manually add [size,mean] to top of the file!
    f = open('../data/batchtests.csv', 'a')
    engine = Engine('perfect')
    # First loop: Ranges of sample sizes to test
    for n in range(start, stop, step):
        f.write(f'size,mean\n')
        # Second loop: tests each sample size 250 times.
        # This results in 250 light blue dots on the graph
        for sample in range(250):
            results = list()
            # Third loop runs simulation n times and stores
            # the mean of thos simulations.
            for _ in range(n):
                engine.play_round()
                results.append(engine.round_points)
            f.write(f'{n}, {int(np.mean(results))}\n')
            print(f'{n}, {sample}')


def define_optimal_bootsize(start, stop, step):
    # Generates bootstrapped data for values in 
    # defined range. It saves the mean and std for
    # each sample. This function will not crash your
    # computer.
    
    data = pd.read_csv('../data/perfect.csv')['score']
    f = open('../data/boottests.csv', 'w+')
    f.write('size,mean,std\n')
    # First loop: how many samples to take with replacement
    for n in range(start, stop, step):
        # Second loop: recording 250 values for comparison
        for _ in range(250):
            sample = np.random.choice(data, n, replace=True)
            f.write(f'{n},{np.mean(sample)},{np.std(sample)}\n')
            print(f'{n},{_}')


def take_sample(vp_name='perfect', n=8000, filename=None):
    # Writes n number of scores + outcomes to file using 
    # the specified VP.
    filename = filename or vp_name
    engine = Engine(vp_name)
    f = open(f'../data/{filename}.csv', 'w+')
    f.write('score,outcome\n')
    for _ in range(n):
        engine.play_round()
        f.write(f'{engine.round_points},{engine.state}\n')

if __name__ == '__main__':
    pass
