import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('img.jpg')

# Get color values in array
blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]
gray = np.add(red * 0.2126, green * 0.7152, blue * 0.0722)
gray = gray.astype(int)

# Get the number of occurrences of each value for each color
blue_element, blue_occur = np.unique(blue, return_counts=True)
green_element, green_occur = np.unique(green, return_counts=True)
red_element, red_occur = np.unique(red, return_counts=True)
gray_element, gray_occur = np.unique(gray, return_counts=True)

# Operation in matplotlib to show results
fig = plt.figure(figsize=(10, 7))
fig.suptitle('Histogram')

ax1 = fig.add_subplot(2, 2, 1)
ax1.set_title("Red")
ax1.bar(red_element, red_occur, width=1, color='red')

ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title("Green")
ax2.bar(green_element, green_occur, width=1, color='Green')

ax3 = fig.add_subplot(2, 2, 3)
ax3.set_title("Blue")
ax3.bar(blue_element, blue_occur, width=1, color='Blue')

ax4 = fig.add_subplot(2, 2, 4)
ax4.set_title("Total")
ax4.bar(gray_element, gray_occur, width=1, color='Gray')

plt.show()
