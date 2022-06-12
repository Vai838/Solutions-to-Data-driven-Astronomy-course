# Write your calculate_mean function here.
'''
from numpy import mean
'''

def calculate_mean(a):
  #m = mean(a)
  m = sum(a)/len(a)
  return m

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calculate_mean` function with examples:
  mean = calculate_mean([1,2.2,0.3,3.4,7.9])
  print(mean)
  
 
