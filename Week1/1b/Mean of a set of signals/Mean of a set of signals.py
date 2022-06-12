# Write your mean_datasets function here


import numpy as np


def mean_datasets(a):
    print(a)
   # datasets =[]
   # for item in a:
   #   datasets.append(item)
   # print(datasets)
   # for something in datasets:
   #   first_element =[]
   #   b = np.loadtxt(something, delimiter =',')
   #   first_element.append(b[0,0])
   #   print(first_element)  
    contents =[]
    for afile in a:
        b = np.loadtxt(afile, delimiter =',')
        #print(b)
        contents.append(b)
    print(contents)
    
    


    

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
