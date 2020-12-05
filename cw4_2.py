# zad 4.2 - ZWIĘKSZENIE OSTROŚCI

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy.signal # do splotów (krawędzie)

# do skali szarości

zad4_2 = np.array(Image.open('zad4_2.JPG'))/255.0
zad4_2 = np.mean(zad4_2, axis = 2)

#plt.imshow(zad4_2, cmap='gray')
#plt.clim(0, 0.7)
#plt.show()

# dobranie maski

mask = np.array([[ 0, -1,  0],
                 [-1,  4, -1],
                 [ 0, -1,  0]])


# filtracja obrazu

zad4_2_filtr = scipy.signal.convolve2d(zad4_2, mask, 'same') # krawędzie
zad4_2_ostry = zad4_2 + 25*(zad4_2_filtr)

# reprezentacja

plt.figure(figsize = (10, 5))

plt.subplot(1,2,1)
plt.imshow(zad4_2, cmap='gray')
plt.clim(0, 0.7)
plt.colorbar()
plt.title('[1] - obraz oryginalny')

plt.subplot(1,2,2)
plt.imshow(zad4_2_ostry, cmap='gray')
plt.clim(0, 0.7)
plt.colorbar()
plt.title('[2] - obraz [1] po zwiększeniu ostrości')

plt.show()