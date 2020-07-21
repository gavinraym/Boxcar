import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import seaborn as sea
from scipy.stats import norm, binom

def bootstrap(data, size=5000):
    # takes set of data and returns normal distribution.
    mean = []
    std = []
    for _ in range(size):
        boot = np.random.choice(
                data=x,
                size=5000,
                replace=True)
        mean.append(boot.mean())
        std.append(boot.std())
    return norm(np.mean(mean), np.mean(std))

def filter_losses(file):
    pass