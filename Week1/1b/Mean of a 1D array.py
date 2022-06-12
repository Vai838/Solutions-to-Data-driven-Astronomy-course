# Write your calc_stats function here.

import numpy as np

def calc_stats(a):
  data = []
  data = np.loadtxt(a , delimiter =',' )
  mean = np.round_(np.mean(data), decimals=1, out=None)
  median = np.round_(np.median(data), decimals=1, out=None)
  return(mean, median)
  
  

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data2.csv')
  print(mean)
