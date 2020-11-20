# HDR

import numpy as np
import matplotlib.pyplot as plt
import skimage.color
from PIL import Image

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