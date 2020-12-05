# zad 4.1 - REDUKCJA SZUMU

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy.signal # do splotów (krawędzie)


# do skali szarości

zad4_1 = np.array(Image.open('zad4_1.png'))/255.0
zad4_1 = np.mean(zad4_1, axis = 2)

#plt.figure(figsize = (6, 6))
#plt.imshow(zad4_1, cmap='gray')
#plt.show()

# dobranie maski

mask = np.ones((5,5))
#mask

# filtracja obrazu

zad4_1_filtr = scipy.signal.convolve2d(zad4_1, mask, 'same')    # zachowanie rozmiaru (512x512)

#plt.figure(figsize = (10, 5))

#plt.subplot(1,2,1)
#plt.imshow(zad4_1, cmap='gray')
#plt.colorbar()

#plt.subplot(1,2,2)
#plt.imshow(zad4_1_filtr, cmap='gray')
#plt.colorbar()
#plt.show()

# porównanie rozmiarów obrazów wyjściowego i zmodyfikowanego (po zastosowaniu filtra)

print('Rozmiary obrazów:')
print(f'Wyjściowy: {zad4_1.shape}')
print(f'Po zastosowaniu filtra: {zad4_1_filtr.shape}')

# redukcja szumu

zad4_1_szum = zad4_1 + np.random.normal(size = zad4_1.shape)*0.05

mask = np.ones((5,5))
zad4_1_filtr_szum = scipy.signal.convolve2d(zad4_1_szum, mask, 'same') # krawędzie

# reprezentacja

plt.figure(figsize = (10, 5))

plt.subplot(1,2,1)
plt.imshow(zad4_1_szum, cmap='gray')
plt.title('[1] - obraz oryginalny z wygenerowanym szumem')

plt.subplot(1,2,2)
plt.imshow(zad4_1_filtr_szum, cmap='gray')
plt.title('[2] - obraz końcowy po nałożeniu filtra na [1]')

plt.show()