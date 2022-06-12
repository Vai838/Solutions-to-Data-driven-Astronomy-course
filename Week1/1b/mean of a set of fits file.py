# Write your mean_fits function here:

from astropy.io import fits
import numpy as np

def mean_fits(file):
    count = 0
    for a_file in file:
        hdulist = fits.open(a_file)
        data = hdulist[0].data
        #hdulist.close()  --> this frees up the memory that file has taken up
        if count == 0:
          stack = data
        else:
           stack = stack + data
        count = count + 1  
    mean = stack/count
    return mean
  



if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
