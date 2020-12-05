import numpy as np
import matplotlib.pyplot as plt
import skimage.color
from PIL import Image

# zad 3.1 - HDR

names = ["zad3_1.jpg", "zad3_2.jpg"]

images = [np.array(Image.open(fname)) for fname in names]

for i, im in enumerate(images):
  plt.figure(figsize=(8,8))
  plt.imshow(im)
  plt.title(names[i])
  plt.show()

images_f32 = [im/255.0 for im in images]

times = [1, 20]

im_hdr = images_f32[0] + images_f32[-1]*times[-1]
im_hdr = (im_hdr - np.min(im_hdr))/(np.max(im_hdr) - np.min(im_hdr))

im_hdr = np.zeros(images_f32[0].shape, dtype=np.float32)

for i, im in enumerate(images_f32):
  im_hdr = im_hdr + im*times[i]

im_hdr = (im_hdr - np.min(im_hdr))/(np.max(im_hdr) - np.min(im_hdr))

im_hdr = np.zeros(images_f32[0].shape, dtype=np.float32)
w_sum = np.zeros((images_f32[0].shape[0], images_f32[0].shape[1], 1))

for i, im in enumerate(images_f32):
  w = np.expand_dims(np.mean(im, axis=2), axis=2)
  im_hdr = im_hdr + im*w*times[i]
  w_sum = w_sum + w

im_hdr = im_hdr/w_sum

im_hdr = (im_hdr - np.min(im_hdr))/(np.max(im_hdr) - np.min(im_hdr))

plt.figure(figsize=(8,8))
plt.imshow(im_hdr**0.33)
plt.title("HDR")
plt.show()

# zad 3.2 - balans bieli

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
