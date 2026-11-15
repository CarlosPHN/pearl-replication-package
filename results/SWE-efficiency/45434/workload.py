import pandas as pd
import numpy as np
import timeit
import statistics

N = 1_000_000

def setup():
    global arr
    arr = pd.array(np.random.randint(0, 100, size=N), dtype="Int64")
    arr._mask[:N//10] = True

def workload():
    global arr
    arr._values_for_argsort()

runtimes = timeit.repeat(workload, number=10, repeat=100, setup=setup)
print("Mean:", statistics.mean(runtimes))
print("Std Dev:", statistics.stdev(runtimes))