# korekcja gamma

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_image(filename):
  im = np.array(Image.open(filename)).mean(axis=2)/255
  return im

def draw_image(im):
  #plt.figure(figsize=(12,9))
  plt.figure(figsize=(6,6))
  plt.imshow(im, cmap='gray')
  plt.clim(0, 1)
  plt.colorbar()
  plt.show()

def gammaCorrection(im):
    return im**(1/2)

zad2_2 = load_image("zad2_2.jpg")
#draw_image(zad2_2)

zad2_2gamma = gammaCorrection(zad2_2)
draw_image(zad2_2gamma)