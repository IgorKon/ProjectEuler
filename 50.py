import datetime
import Utilities
from itertools import permutations

start_time = datetime.datetime.now()

max_i = 999999

a = Utilities.Eratosthenes(max_i)
                
stop_time = datetime.datetime.now()
print(stop_time - start_time)
