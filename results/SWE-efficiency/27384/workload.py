
import timeit
import statistics

import pandas as pd
import numpy as np

N = 10 ** 5

def setup():
    global idx
    idx = pd.MultiIndex.from_product(
        [pd.date_range("1/1/2000", freq="T", periods=N // 2), ["a", "b"]]
    )

def workload():
    global idx
    idx.shape

runtimes = timeit.repeat(workload, number=1, repeat=100, setup=setup)

print("Mean:", statistics.mean(runtimes))
print("Std Dev:", statistics.stdev(runtimes))