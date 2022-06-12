# Write your list_stats function here.

import numpy as np

def list_stats(numbers):
  
  mean = sum(numbers)/len(numbers)
  
  numbers.sort()
  
  midvalue = len(numbers)//2
  
  if len(numbers)%2 == 0:
    median = (numbers[midvalue] + numbers[midvalue -1])/2
  else:
    median = numbers[midvalue]
  
  return median,mean


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)
