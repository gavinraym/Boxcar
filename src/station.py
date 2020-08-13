from engine import Engine
import csv
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from hopper import clear
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
    
    f = open('../data/batchtests.csv', 'w+')
    f.write(f'size,mean_score\n')
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
            f.write(f'{n},{int(np.mean(results))}\n')
            clear()
            print(f'Generating samples... test #{int(n/stop*100)}.{int(sample/250*100)}% done')
    f.close()

def take_sample(vp_name='perfect', n=100, file_name='sample'):
    # Writes n number of scores + outcomes to file using 
    # the specified VP.
    file_name = file_name or vp_name
    engine = Engine(vp_name)
    f = open(f'../data/{file_name}.csv', 'w+')
    f.write('score\n')
    for _ in range(n):
        engine.play_round()
        f.write(f'{engine.round_points}\n')

if __name__ == '__main__':
    clear()
    num =input('''Menu:\n
    1)  Generate sample of scores from any VP, or play with 'terminal'.
    2)  Run tests needed to define the optimal number of samples. (ch.2)

    Please input a number
    ''')
    if num == '1':
        vp_name=input('Which VP? (or use terminal to play yourself.)
        n = int(input('How many games?'))
        file_name = input('Save under what name?')
        take_sample(vp_name, n, file_name)
    if num == '2':
        define_optimal_sample_size()
    



