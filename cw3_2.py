# zad 3.2 - balans bieli

import numpy as np
import matplotlib.pyplot as plt
import skimage.color
from PIL import Image


im1 = np.array(Image.open('zad3_1.jpg'))
im1 = (im1 - np.min(im1)) / (np.max(im1) - np.min(im1))

im2 = np.array(Image.open('zad3_2.jpg'))
im2 = (im2 - np.min(im2)) / (np.max(im2) - np.min(im2))

plt.figure(figsize = (10, 5))
plt.subplot(1,2,1)
plt.imshow(im1)
plt.subplot(1,2,2)
plt.imshow(im2)
plt.show()


im1_hsv = skimage.color.rgb2hsv(im1)
mask = im1_hsv[:,:,1] < 0.8

plt.figure(figsize = (10, 5))
plt.subplot(1,2,1)
plt.imshow(im1_hsv[:,:,1])
plt.colorbar()

mask = im1_hsv[:,:,1] < 0.8
plt.subplot(1,2,2)
plt.imshow(mask)
plt.colorbar()
plt.show()

ind = np.argwhere(mask == 1)
rows = ind[:,0]
cols = ind[:,1]

white_pixels1 = im1[rows, cols, :]
white_pixels1.shape
white1 = np.mean(white_pixels1, axis = 0)
#white1.shape

white_pixels2 = im2[rows, cols, :]
white2 = np.mean(white_pixels2, axis = 0)

corr_factors_2 = white1/white2
corr_factors_2

im2_cpy = im2.copy()

im2_cpy[:,:,0] = im2_cpy[:,:,0]*corr_factors_2[0]
im2_cpy[:,:,1] = im2_cpy[:,:,1]*corr_factors_2[1]
im2_cpy[:,:,2] = im2_cpy[:,:,2]*corr_factors_2[2]


plt.figure(figsize = (10, 5))
plt.subplot(1,2,1)
plt.imshow(im2_cpy)
plt.subplot(1,2,2)
plt.imshow(im2*corr_factors_2)
plt.show()