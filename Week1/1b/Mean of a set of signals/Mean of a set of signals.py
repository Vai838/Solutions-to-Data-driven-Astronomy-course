# Write your mean_datasets function here


import numpy as np


def mean_datasets(file_names):
    count = 0
    for a_file in file_names:
        b = np.loadtxt(a_file, delimiter =',')
        if count == 0:
          c = b
        else:
           c = c + b
        count = count + 1  
    mean = np.round_(c/count , decimals=1 , out=None)
    return mean
    
    


    

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
