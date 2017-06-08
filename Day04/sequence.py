'''sequence.py -- timing append verses making a list from a sequence

Mike Moran and Ben Rose
REU CMP Class June 2016 & 2017
Python3
'''
from datetime import datetime as dt

# time list comprehension
start = dt.now()
l = []
for i in range(1000000):    #that is 1,000,000 times!
    l.append(i)
end = dt.now()

print((end - start).total_seconds())


# time making a list from a sequence
start = dt.now()
l = [i for i in range(1000000)]
end = dt.now()

print((end - start).total_seconds())