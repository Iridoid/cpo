# poprawa kontrastu

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_image(filename):
  im = np.array(Image.open(filename)).mean(axis=2)/255
  return im

def draw_image(im):
  plt.figure(figsize=(6,6))
  plt.imshow(im, cmap='gray')
  plt.clim(0, 1)
  plt.colorbar()
  plt.show()

def addContrast(im):
  im_mod = (im - np.min(im)) / (np.max(im) - np.min(im))
  return im_mod

zad2_1 = load_image("zad2_1.jpg")
#draw_image(zad2_1)

zad2_1contrast = addContrast(zad2_1)
draw_image(zad2_1contrast)