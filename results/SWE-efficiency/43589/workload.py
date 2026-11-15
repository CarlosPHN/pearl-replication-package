import timeit
import statistics

from dateutil import tz
import pandas as pd
from time import time

dates = pd.date_range('2010-01-01', periods=1000, tz=tz.tzutc())
index = pd.MultiIndex.from_product([range(100), dates])
index2 = index.copy()

def workload():
    index.equals(index2)
    
runtimes = timeit.repeat(workload, number=5, repeat=25)

# Print runtime mean and std deviation.
print("Mean:", statistics.mean(runtimes))
print("Std Dev:", statistics.stdev(runtimes))
