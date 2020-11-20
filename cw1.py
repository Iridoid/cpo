import numpy as np
import matplotlib.pyplot as plt

maze = np.array([[0, 0, 1, 0, 2, 0],
                 [0, 0, 1, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0],
                 [1, 0, 1, 1, 1, 0],
                 [1, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 1, 0],
                 [3, 1, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0]])

entry_exit_pts = np.argwhere(maze > 1)
print(entry_exit_pts)
startPt, endPt = entry_exit_pts
print(startPt)
print(endPt)

plt.figure(figsize=(6, 6))
plt.imshow(maze)
plt.clim(0, 4)
plt.colorbar()
plt.show()

import numpy as np

# The list needs to be transformed into an array in order to use the np.where method
# arr = np.random.randint(5, size=(6, 6))
arr = np.array([[0, 0, 0, 1, 1, 3],
                [0, 0, 2, 1, 1, 0],
                [0, 0, 1, 1, 1, 1],
                [3, 0, 3, 1, 1, 1], ])

# Origin cell to make the search
x0, y0 = (1, 1)
targetValue = 3

# This is the keypoint of the problem: find the positions of the cells containing the searched value
positions = np.where(arr == targetValue)
x, y = positions

dx = abs(x0 - x)  # Horizontal distance
dy = abs(y0 - y)  # Vertical distance

# There are different criteria to compute distances
euclidean_distance = np.sqrt(dx ** 2 + dy ** 2)
manhattan_distance = abs(dx + dy)
my_distance = euclidean_distance  # Criterion choice
min_dist = min(my_distance)
print(min_dist)

min_pos = np.argmin(my_distance)  # This method will only return the first occurrence (!)
min_coords = x[min_pos], y[min_pos]
print(min_coords)