# Write your load_fits function here.

from astropy.io import fits
import numpy as np

def load_fits(filename):
  hdulist = fits.open(filename)
  data = hdulist[0].data
  arg_max = np.argmax(data)
  max_pos = np.unravel_index(arg_max,data.shape)   #data.shape returns dimensions of the image in primary HDU
  return max_pos
  
if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

 
