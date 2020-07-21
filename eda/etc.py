from scipy.stats import norm
import numpy as np


def bootstrap(x):
    # takes set of data and returns normal distribution.
    mean = []
    std = []
    for _ in range(5000):
        boot = np.random.choice(
                a=x,
                size=5000,
                replace=True)
        mean.append(boot.mean())
        std.append(boot.std())
    return norm(np.mean(mean), np.mean(std))